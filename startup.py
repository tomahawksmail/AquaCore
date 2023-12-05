from flask import Flask, render_template, request, redirect, flash
import os
from dotenv import load_dotenv
import pymysql
import time
import subprocess

host = '192.168.50.1'
port = 80
apoint = Flask(__name__)

load_dotenv()
connection = pymysql.connect(host=os.environ.get('HOST'),
                             user=os.environ.get('USER'),
                             password=os.environ.get('PASSWORD'),
                             database=os.environ.get('DATABASE'))

version = os.environ.get('VERSION')
apoint.secret_key = os.environ.get('SECRET_KEY')

@apoint.route("/", methods=['POST', 'GET'])
def ap():
    return render_template('ap.html', version=version)

def stopAP(): #hotspot
    print("Stopping AP...")
    subprocess.call('ls -la', shell=True)
    # subprocess.run(['systemctl', "stop", "hostapd", "dnsmasq", "dhcpcd"],check=True)
    # subprocess.run(['nmcli','radio', 'wifi', 'on'],check=True)
    time.sleep(1)

def startAP(): #hotspot
    subprocess.run('create_ap -g 192.168.50.1 -n wlan0 AquaCore orangepi --no-virt'.split(),check=True)

def safeSSID():
    pass


def checkwifi():
    result = subprocess.check_output(['iw', 'dev','wlan0','link'], encoding='utf8')
    # print(">>"+str(result))
    if not("Not connected" in result):
        return True
    return False


if __name__ == "__main__":
    time.sleep(5)
    if checkwifi():
        print("connected")
    else:
        print("creating AP")
        startAP()
        apoint.run(debug=True, host=host, port=port, threaded=True)

