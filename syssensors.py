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
    data.append(int(psutil.virtual_memory()[10]))  # slab





    return data


# # Обработчик оперативки, возвращает список RAM
def memload():
    virtual_memory = psutil.virtual_memory()
    RAM = list(virtual_memory)
    RAM.insert(0, datetime.now())
    return RAM
#
# # Обработчик температуры, возвращает список temp
# def temperature():
#     temp = []
#     if not hasattr(psutil, "sensors_temperatures"):
#         sys.exit("platform not supported")
#     temps = psutil.sensors_temperatures()
#     if not temps:
#         sys.exit("can't read any temperature")
#     for name, entries in temps.items():
#         for entry in entries:
#             temp.append(datetime.now())
#             temp.append(entry.current)
#             return temp
#

def insert_data_to_SQL():
    cpu = load()
    print(cpu)
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