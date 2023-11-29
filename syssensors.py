import time
import os
import pymysql
import psutil
import sys
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()
# connection = pymysql.connect(host=os.environ.get('HOST'),
#                              user=os.environ.get('USER'),
#                              password=os.environ.get('PASSWORD'),
#                              database=os.environ.get('DATABASE'))

if not hasattr(psutil.Process, "cpu_num"):
    sys.exit("platform not supported")


def load():
    data = []
    num_cpus = psutil.cpu_count()
    uptime = (time.time() - psutil.boot_time()) / 60

    data.append(datetime.now())

    data.append(int(psutil.cpu_freq()[0]))
    data.append(int(psutil.cpu_freq()[1]))
    data.append(int(psutil.cpu_freq()[2]))

    data.append(int(psutil.cpu_percent(percpu=True)[0]))
    data.append(int(psutil.cpu_percent(percpu=True)[1]))
    data.append(int(psutil.cpu_percent(percpu=True)[2]))
    data.append(int(psutil.cpu_percent(percpu=True)[3]))

    data.append(int(psutil.virtual_memory()[0]))  #total
    data.append(int(psutil.virtual_memory()[1]))  # available
    data.append(int(psutil.virtual_memory()[2]))  # percent
    data.append(int(psutil.virtual_memory()[3]))  # used
    data.append(int(psutil.virtual_memory()[4]))  # free
    data.append(int(psutil.virtual_memory()[5]))  # active
    data.append(int(psutil.virtual_memory()[6]))  # inactive
    data.append(int(psutil.virtual_memory()[7]))  # buffers
    data.append(int(psutil.virtual_memory()[8]))  # cached
    data.append(int(psutil.virtual_memory()[9]))  # shared
    data.append((psutil.virtual_memory()[10]))  # slab

    data.append(psutil.sensors_temperatures().get('cpu_thermal')[0][1])  # cpu_thermal_cur
    data.append(psutil.sensors_temperatures().get('cpu_thermal')[0][2])  # cpu_thermal_high
    data.append(psutil.sensors_temperatures().get('cpu_thermal')[0][3])  # cpu_thermal_crit
    data.append(psutil.sensors_temperatures().get('gpu_thermal')[0][1])  # gpu_thermal_cur
    data.append(psutil.sensors_temperatures().get('gpu_thermal')[0][2])  # gpu_thermal_high
    data.append(psutil.sensors_temperatures().get('gpu_thermal')[0][3])  # gpu_thermal_crit
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

    data.append(psutil.disk_usage("/")[0])  # disk_usage_total
    data.append(psutil.disk_usage("/")[1])  # disk_usage_used
    data.append(psutil.disk_usage("/")[2])  # disk_usage_free
    data.append(psutil.disk_usage("/")[3])  # disk_usage_percent

    return data, num_cpus, uptime

def insert_data_to_SQL():
    data = load()
    print(data)
    # print(cpu)
    # SQLrequest = """SELECT * FROM loging ORDER BY id DESC LIMIT 30"""
    # try:
    #     connection.connect()
    #     with connection.cursor() as cursor:
    #         cursor.execute(SQLrequest)
    #     log = cursor.fetchall()
    #     cursor.close()
    #     connection.close()
    # except Exception as E:
    #     log(E)

if __name__ == "__main__":
    insert_data_to_SQL()