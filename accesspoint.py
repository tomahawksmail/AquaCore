import subprocess

host = '192.168.150.5'
def startAP(): #hotspot
    subprocess.run(f'sudo create_ap -g {host} -n wlan0 AquaCore orangepi --no-virt'.split(),check=True)

def stopAP(): #hotspot
    subprocess.run(f'sudo create_ap --stop wlan0'.split(),check=True)

def checkwifi():
    result = subprocess.check_output(['iw', 'dev','wlan0','link'], encoding='utf8')
    if not("Not connected" in result):
        return True
    return False

def connect_to_wifi(ssid, password):
    try:
        # Check if the network is already in the list of known networks
        check_command = f"nmcli connection show '{ssid}'"
        result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"Already connected to {ssid}")
        else:
            # Connect to the Wi-Fi network
            connect_command = f"nmcli device wifi connect '{ssid}' password '{password}'"
            subprocess.run(connect_command, shell=True, check=True)
            print(f"Connected to {ssid}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Replace 'your_ssid' and 'your_password' with your Wi-Fi credentials
#connect_to_wifi('test', 'your_password')





