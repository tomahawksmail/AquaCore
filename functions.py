from main import connection, session
from datetime import datetime
import psutil
import time
from subprocess import Popen, PIPE, run

def log(event):
    try:
        connection.connect()
        with connection.cursor() as cursor:
            SQLrequest = """insert into loging (User, Event, Datetime) values (%s, %s, %s)"""
            cursor.execute(SQLrequest, (session['user'], event, datetime.now()))
            connection.commit()
    except Exception as E:
        log(E)
        cursor.close()
        connection.close()

def getDatatoOptions():
    SQLrequest = """SELECT * FROM options"""
    status = """SELECT * FROM status"""
    try:
        connection.connect()
        with connection.cursor() as cursor:
            cursor.execute(SQLrequest)
        options = cursor.fetchone()
        with connection.cursor() as cursor:
            cursor.execute(status)
        status = cursor.fetchall()[0]
        result = (options, status)
        cursor.close()
        connection.close()
    except Exception as E:
        log(E)
    return result

def setDataOptions(formoptions):
    try:
        connection.connect()
        with connection.cursor() as cursor:
            for i in formoptions:
                SQL = f"UPDATE `options` SET {i[0]} = '{i[1]}'"
                print(SQL)
                event = f"SET {i[0]} = {i[1]}"
                log(event)
                cursor.execute(SQL)
                connection.commit()
            cursor.close()
        connection.close()
    except Exception as E:
        log(E)

def setDataStatus(formstatus):
    try:
        connection.connect()
        with connection.cursor() as cursor:
            for i in formstatus:
                SQL = f"UPDATE `status` SET {i[0]} = '{'checked' if i[1] == 'on' else 'unchecked'}'"
                cursor.execute(SQL)
                connection.commit()
            cursor.close()
        connection.close()
    except Exception as E:
        log(E)

def get_core_data():
    SQLrequest = """SELECT HOUR(Dttm), AVG(cpus_percent_0), AVG(cpus_percent_1), 
                    AVG(cpus_percent_2), AVG(cpus_percent_3) 
                    FROM psutil WHERE 
                    (Dttm >= NOW() - INTERVAL 1 DAY) 
                    GROUP BY HOUR(Dttm) """
    try:
        connection.connect()
        with connection.cursor() as cursor:
            cursor.execute(SQLrequest)
        data = cursor.fetchall()
        cursor.close()
        connection.close()

    except Exception as E:
        log(E)
    return data

def get_temp_data():
    SQLrequest = """SELECT HOUR(Dttm), round(AVG(cpu_thermal_cur),1), round(AVG(gpu_thermal_cur), 1),
                    round(AVG(ve_thermal_cur),1), round(AVG(ddr_thermal_cur), 1)
                    FROM psutil WHERE 
                    (Dttm >= NOW() - INTERVAL 1 DAY) 
                    GROUP BY HOUR(Dttm)"""
    try:
        connection.connect()
        with connection.cursor() as cursor:
            cursor.execute(SQLrequest)
        data = cursor.fetchall()
        cursor.close()
        connection.close()

    except Exception as E:
        log(E)
    return data


def get_RAM_data():
    SQLrequest = """SELECT HOUR(Dttm), round(AVG(RAM_available),0), round(AVG(RAM_used), 0),
                    round(AVG(RAM_free),0), round(AVG(RAM_active), 0),
                    round(AVG(RAM_inactive),0), round(AVG(RAM_buffers), 0),
                    round(AVG(RAM_cached),0), round(AVG(RAM_shared), 0),
                    round(AVG(RAM_slab),0)
                    FROM psutil WHERE 
                    (Dttm >= NOW() - INTERVAL 1 DAY) 
                    GROUP BY HOUR(Dttm)"""
    try:
        connection.connect()
        with connection.cursor() as cursor:
            cursor.execute(SQLrequest)
        data = cursor.fetchall()
        cursor.close()
        connection.close()

    except Exception as E:
        log(E)
    return data

def get_cur_data():
    cpu_count = psutil.cpu_count()  # cpu_count
    uptime = int((time.time() - psutil.boot_time()) / 60)  # uptime
    cur_freq = int(psutil.cpu_freq()[0])
    cpu_perc_load = int((psutil.cpu_percent(percpu=True)[0] + psutil.cpu_percent(percpu=True)[1] +
                         psutil.cpu_percent(percpu=True)[2] + psutil.cpu_percent(percpu=True)[3]) / 4)
    RAM_total = int(psutil.virtual_memory()[0]/1000000)


    cmd_output = Popen(["iwconfig", "wlan0"], stdout=PIPE)

    WIFIcmd = (cmd_output.communicate()[0].decode('UTF-8')).split("\n")
    WIFI = []
    WIFI.append(WIFIcmd[0].replace('     ', ' ').replace('ESSID', ', SSID').replace(':', ': '))
    WIFI.append("Frequency: " + WIFIcmd[1].split(" ")[12].replace("Frequency:", "") + " GHz")
    WIFI.append('MAC ' + WIFIcmd[1].split(" ")[17])
    WIFI.append(WIFIcmd[2].replace('          ', ''))
    WIFI.append(WIFIcmd[5].replace('          ', '').split('  ')[0])
    WIFI.append(int(WIFIcmd[5].replace('          ', '').split('  ')[1].split("=")[1].split(" ")[0]))



    cpu_thermal_cur = round(psutil.sensors_temperatures().get('cpu_thermal')[0][1], 1)
    gpu_thermal_cur = round(psutil.sensors_temperatures().get('gpu_thermal')[0][1], 1)
    ve_thermal_cur  = round(psutil.sensors_temperatures().get( 've_thermal')[0][1], 1)
    ddr_thermal_cur = round(psutil.sensors_temperatures().get('ddr_thermal')[0][1], 1)

    net = []
    net.append(round(psutil.net_io_counters()[0]/1024))  # net_bytes_sent
    net.append(round(psutil.net_io_counters()[1]/1024))  # net_bytes_recv
    net.append(psutil.net_io_counters()[2])  # net_packets_sent
    net.append(psutil.net_io_counters()[3])  # net_packets_recv
    net.append(psutil.net_io_counters()[4])  # net_errin
    net.append(psutil.net_io_counters()[5])  # net_errout
    net.append(psutil.net_io_counters()[6])  # net_dropin
    net.append(psutil.net_io_counters()[7])  # net_dropout

    disk = []
    disk.append(int(psutil.disk_usage("/")[1]/1048576))  # disk_usage_used, Mb
    disk.append(int(psutil.disk_usage("/")[2]/1048576))  # disk_usage_free, Mb

    disku = []
    disku.append(psutil.disk_io_counters()[0])
    disku.append(psutil.disk_io_counters()[1])
    disku.append(psutil.disk_io_counters()[2])
    disku.append(psutil.disk_io_counters()[3])
    disku.append(psutil.disk_io_counters()[4])
    disku.append(psutil.disk_io_counters()[5])
    disku.append(psutil.disk_io_counters()[8])

    RAM_cur = []
    RAM_cur.append(int(psutil.virtual_memory()[2])) #Used
    RAM_cur.append(100 - int(psutil.virtual_memory()[2])) #free


    return cpu_count, uptime, cur_freq, RAM_total, cpu_thermal_cur, gpu_thermal_cur, ve_thermal_cur, ddr_thermal_cur, net, cpu_perc_load, WIFI, disk, disku, RAM_cur



