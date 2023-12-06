from flask import Flask, render_template, redirect
import os
from dotenv import load_dotenv
import pymysql
import time
import subprocess
import threading

host = 'http://192.168.150.5'
port = 81

apoint = Flask(__name__)

load_dotenv()
connection = pymysql.connect(host=os.environ.get('HOST'),
                             user=os.environ.get('USER'),
                             password=os.environ.get('PASSWORD'),
                             database=os.environ.get('DATABASE'))

version = os.environ.get('VERSION')
# apoint.secret_key = os.environ.get('SECRET_KEY')


# @apoint.route('/')
# def Index():
#     return render_template('ap.html', message="Once connected you'll find IP address @ <a href='https://snaptext.live/{}' target='_blank'>snaptext.live/{}</a>.")
#
# # Captive portal when connected with iOS or Android
# @apoint.route('/generate_204')
# def redirect204():
#     return redirect(host, code=302)
#
# @apoint.route('/hotspot-detect.html')
# def applecaptive():
#     return redirect(host, code=302)



def startAP(): #hotspot
    subprocess.run(f'sudo create_ap -g {host} -n wlan0 AquaCore orangepi --no-virt'.split(),check=True)




def checkwifi():
    result = subprocess.check_output(['iw', 'dev','wlan0','link'], encoding='utf8')
    # print(">>"+str(result))
    if not("Not connected" in result):
        return True
    return False





