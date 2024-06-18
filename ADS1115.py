import time
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115(address=0x54, busnum=1)

GAIN = 8
delay = 1
def analogportsread():
    value = 0
    try:
        val = adc.read_adc(3, gain=GAIN, data_rate=128) * (5.0 / 327670) * 100
    except Exception as E:
        print(E)
        val = 0
    else:
        print(val)


if __name__ == '__main__':
    try:
        while True:
            analogportsread()
            time.sleep(delay)
    except KeyboardInterrupt:
        adc.stop_adc()
        print("Keyboard interrupt")
