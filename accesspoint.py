import subprocess

host = '192.168.150.5'
def startAP(): #hotspot
    subprocess.run(f'sudo create_ap -g {host} -n wlan0 AquaCore orangepi --no-virt'.split(),check=True)
def checkwifi():
    result = subprocess.check_output(['iw', 'dev','wlan0','link'], encoding='utf8')
    if not("Not connected" in result):
        return True
    return False





