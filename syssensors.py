import psutil
import sys
import datetime

if not hasattr(psutil.Process, "cpu_num"):
    sys.exit("platform not supported")


def cpuload():
    num_cpus = psutil.cpu_count()
    cpus_percent = psutil.cpu_percent(percpu=True)
    cpu_load = []
    for _ in range(num_cpus):
        cpu_load.append(cpus_percent.pop(0))
    cpu_load.insert(0, datetime.now())
    cpufreq = int(psutil.cpu_freq()[0])
    cpu_load.append(cpufreq)
    return cpu_load

# Обработчик оперативки, возвращает список RAM
def memload():
    virtual_memory = psutil.virtual_memory()
    RAM = list(virtual_memory)
    RAM.insert(0, datetime.now())
    return RAM

# Обработчик температуры, возвращает список temp
def temperature():
    temp = []
    if not hasattr(psutil, "sensors_temperatures"):
        sys.exit("platform not supported")
    temps = psutil.sensors_temperatures()
    if not temps:
        sys.exit("can't read any temperature")
    for name, entries in temps.items():
        for entry in entries:
            temp.append(datetime.now())
            temp.append(entry.current)
            return temp

print(cpuload(), memload(), temperature())