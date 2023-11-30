import time
import os
import pymysql
import psutil
import sys
from dotenv import load_dotenv


load_dotenv()
connection = pymysql.connect(host=os.environ.get('HOST'),
                             user=os.environ.get('USER'),
                             password=os.environ.get('PASSWORD'),
                             database=os.environ.get('DATABASE'))

if not hasattr(psutil.Process, "cpu_num"):
    sys.exit("platform not supported")


def load():
    data = []


    data.append(int(psutil.cpu_freq()[0]))
    # data.append(int(psutil.cpu_freq()[1]))
    # data.append(int(psutil.cpu_freq()[2]))

    data.append(int(psutil.cpu_percent(percpu=True)[0]))
    data.append(int(psutil.cpu_percent(percpu=True)[1]))
    data.append(int(psutil.cpu_percent(percpu=True)[2]))
    data.append(int(psutil.cpu_percent(percpu=True)[3]))

    data.append(int(psutil.virtual_memory()[0]/1048576))  #total
    data.append(int(psutil.virtual_memory()[1]/1048576))  # available
    data.append(int(psutil.virtual_memory()[2]))  # percent
    data.append(int(psutil.virtual_memory()[3]/1048576))  # used
    data.append(int(psutil.virtual_memory()[4]/1048576))  # free
    data.append(int(psutil.virtual_memory()[5]/1048576))  # active
    data.append(int(psutil.virtual_memory()[6]/1048576))  # inactive
    data.append(int(psutil.virtual_memory()[7]/1048576))  # buffers
    data.append(int(psutil.virtual_memory()[8]/1048576))  # cached
    data.append(int(psutil.virtual_memory()[9]/1048576))  # shared
    data.append((psutil.virtual_memory()[10]))  # slab

    data.append(psutil.sensors_temperatures().get('cpu_thermal')[0][1])  # cpu_thermal_cur
    # data.append(psutil.sensors_temperatures().get('cpu_thermal')[0][2])  # cpu_thermal_high
    # data.append(psutil.sensors_temperatures().get('cpu_thermal')[0][3])  # cpu_thermal_crit
    data.append(psutil.sensors_temperatures().get('gpu_thermal')[0][1])  # gpu_thermal_cur
    # data.append(psutil.sensors_temperatures().get('gpu_thermal')[0][2])  # gpu_thermal_high
    # data.append(psutil.sensors_temperatures().get('gpu_thermal')[0][3])  # gpu_thermal_crit
    data.append(psutil.sensors_temperatures().get('ve_thermal')[0][1])  # ve_thermal_cur
    data.append(psutil.sensors_temperatures().get('ddr_thermal')[0][1])  # gpu_thermal_cur

    data.append(psutil.net_io_counters()[0])  # net_bytes_sent
    data.append(psutil.net_io_counters()[1])  # net_bytes_recv
    data.append(psutil.net_io_counters()[2])  # net_packets_sent
    data.append(psutil.net_io_counters()[3])  # net_packets_recv
    data.append(psutil.net_io_counters()[4])  # net_errin
    data.append(psutil.net_io_counters()[5])  # net_errout
    data.append(psutil.net_io_counters()[6])  # net_dropin
    data.append(psutil.net_io_counters()[7])  # net_dropout

    data.append(psutil.disk_io_counters()[0])  # disk_read_count
    data.append(psutil.disk_io_counters()[1])  # disk_write_count
    data.append(psutil.disk_io_counters()[2])  # disk_read_bytes
    data.append(psutil.disk_io_counters()[3])  # disk_write_bytes
    data.append(psutil.disk_io_counters()[4])  # disk_read_time
    data.append(psutil.disk_io_counters()[5])  # disk_write_time
    data.append(psutil.disk_io_counters()[8])  # disk_busy_time

    data.append(psutil.disk_usage("/")[0]/1048576)  # disk_usage_total, Mb
    data.append(psutil.disk_usage("/")[1]/1048576)  # disk_usage_used, Mb
    data.append(psutil.disk_usage("/")[2]/1048576)  # disk_usage_free, Mb
    data.append(psutil.disk_usage("/")[3])  # disk_usage_percent, %

    return data

def get_uptime():
    num_cpus = psutil.cpu_count()
    uptime = (time.time() - psutil.boot_time()) / 60
    return num_cpus, uptime


def insert_data_to_SQL():
    data = load()

    SQLrequest = """
    insert into psutil (Dttm, scpufreq_cur, cpus_percent_0, cpus_percent_1, cpus_percent_2, 
    cpus_percent_3, RAM_total, RAM_available, RAM_percent, RAM_used, RAM_free, RAM_active, RAM_inactive, RAM_buffers, 
    RAM_cached, RAM_shared, RAM_slab, cpu_thermal_cur, gpu_thermal_cur, ve_thermal_cur, ddr_thermal_cur, net_bytes_sent, net_bytes_recv, 
    net_packets_sent, net_packets_recv, net_errin, net_errout, net_dropin, net_dropout, disk_read_count, 
    disk_write_count, disk_read_bytes, disk_write_bytes, disk_read_time, disk_write_time, disk_busy_time, 
    disk_usage_total, disk_usage_used, disk_usage_free, disk_usage_percent) 
    values
    (now(), %s, %s, %s, %s, %s, %s, %s, %s, %s, 
     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        connection.connect()
        with connection.cursor() as cursor:
            cursor.execute(SQLrequest, data)
            connection.commit()
        cursor.close()
        connection.close()
    except Exception as E:
        print(E)

if __name__ == "__main__":
    insert_data_to_SQL()