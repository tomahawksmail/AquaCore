import time
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

GAIN = 1
delay = 1
def analogportsread():
    value = 0
    try:
        volts = adc.read_adc(3, gain=GAIN, data_rate=128)
        temp = 21
        averageVoltage = median(volts)
        compensationCoefficient = 1.0 + 0.02 * (temp - 25.0)

        compensationVolatge = averageVoltage / compensationCoefficient
        tds = compensationVolatge * 0.000125
        val = adc.read_adc(3, gain=GAIN, data_rate=128)*5*1.686/65535
    except Exception as E:
        print(E)
        tds = 0
    else:
        print(tds)


if __name__ == '__main__':
    try:
        while True:
            analogportsread()
            time.sleep(delay)
    except KeyboardInterrupt:
        adc.stop_adc()
        print("Keyboard interrupt")
