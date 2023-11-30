import os
import time
import subprocess

host = '192.168.50.1'
port = 80


def stopAP(): #hotspot
    print("Stopping AP...")
    subprocess.call('ls -la', shell=True)
    # subprocess.run(['systemctl', "stop", "hostapd", "dnsmasq", "dhcpcd"],check=True)
    # subprocess.run(['nmcli','radio', 'wifi', 'on'],check=True)
    time.sleep(1)

# def startAP(): #hotspot
#     subprocess.run('nmcli radio wifi off'.split(),check=True)
#     subprocess.run('rfkill unblock wlan'.split(),check=True)
#     subprocess.run(['systemctl', "restart", "hostapd", "dnsmasq", "dhcpcd"], check=True)
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

