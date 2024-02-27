import time
from datetime import datetime
from subprocess import Popen, PIPE
import pymysql
import os

from dotenv import load_dotenv

dotenv_path = '/home/orangepi/AquaCore/.env'
load_dotenv(dotenv_path)
connection = pymysql.connect(host=os.environ.get('HOST'),
                             user=os.environ.get('USER'),
                             password=os.environ.get('PASSWORD'),
                             database=os.environ.get('DATABASE'))

Popen(["gpio", "mode", "6", "in"]) #Button
Popen(["gpio", "mode", "6", "down"]) #Button

### R2 ###
Popen(["gpio", "mode", "19", "out"]) #01 CO2
Popen(["gpio", "mode", "14", "out"]) #02 O2
Popen(["gpio", "mode", "12", "out"]) #03 UV
Popen(["gpio", "mode", "11", "out"]) #04 Heater
### U9 ###
Popen(["gpio", "mode", "2", "out"])  #01
Popen(["gpio", "mode", "5", "out"])  #02

### R1 ###
Popen(["gpio", "mode", "10", "out"]) #01
Popen(["gpio", "mode", "13", "out"]) #02
Popen(["gpio", "mode", "15", "out"]) #03
Popen(["gpio", "mode", "16", "out"]) #04
Popen(["gpio", "mode", "25", "out"]) #05
Popen(["gpio", "mode", "24", "out"]) #06
### U10 ###
Popen(["gpio", "mode", "26", "out"]) #01
Popen(["gpio", "mode", "27", "out"]) #02



### PWM ###



###gpio readall###
def readGPIO():
    result = []
    readall = (Popen(["gpio", "readall"], stdout=PIPE).communicate()[0].decode('UTF-8').split("\n"))
    for i in range(3, 23, 1):
        l = readall[i].replace("|"," ").split()
        result.append(l)
    return result

def gpioON(num):
    Popen(["gpio", "write", str(num), "down"])

def gpioOFF(num):
    Popen(["gpio", "write", str(num), "up"])




def getStatusFromDB():
    SQLrequest = """SELECT * FROM status"""
    try:
        connection.connect()
        with connection.cursor() as cursor:
            cursor.execute(SQLrequest)
        status = cursor.fetchone()
        cursor.close()
        connection.close()
        return status
    except Exception as E:
        print(E)

def turnRelay():
    status = getStatusFromDB()
    Relay2 = {0:12,  #1
              1:14,  #2
              2:19,  #3
              3:11}  #4

    for i in Relay2:
        value = Relay2[i]
        if status[i] == 'checked':
            gpioON(value)
        elif status[i] == 'unchecked':
            gpioOFF(value)



def checktime():
    SQLrequest = """SELECT * FROM options"""
    try:
        connection.connect()
        with connection.cursor() as cursor:
            cursor.execute(SQLrequest)
        status = cursor.fetchone()



        # if datetime.strptime(status[6], '%H:%M').time() <= datetime.now().time():
        #     gpioON(12)


        cursor.close()
        connection.close()
        return status
    except Exception as E:
        print(E)



if __name__ == "__main__":
    while True:
        turnRelay()
        checktime()
        time.sleep(0.5)


