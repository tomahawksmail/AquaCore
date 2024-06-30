import time
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

GAIN = 1
delay = 1


# SPECIFICATION
# Signal Conversion Board (Transmitter) V2
# Supply Voltage: 3.3~5.5V
# Output Voltage: 0~3.0V
# Measurement Accuracy: ±0.1@25℃

# pH Probe

# Detection Range: 0~14
# Temperature Range: 5~60°C
# Zero Point: 7±0.5
# Response Time: <2min
# Internal Resistance: <250MΩ
# Probe Life: >0.5 years (depending on the frequency of use)



def getTemp():
    pass

def getTDS():
    value = 0
    TDS_massive = []
    try:
        for i in range(10):
            volts = adc.read_adc(3, gain=GAIN, data_rate=128)
            TDS_massive.append(volts)
        averageVoltage = sum(TDS_massive) / len(TDS_massive)
        print(averageVoltage)


        temp = 21

        compensationCoefficient = 1.0 + 0.02 * (temp - 25.0)

        compensationVolatge = averageVoltage / compensationCoefficient
        tds = compensationVolatge * 0.000125
        # val = adc.read_adc(3, gain=GAIN, data_rate=128) * 5 * 1.686 / 65535
    except Exception as E:
        print(E)
        tds = 0
    else:
        print(tds)

def getPH():
    pass




if __name__ == '__main__':
    try:
        while True:
            getTDS()
            time.sleep(delay)
    except KeyboardInterrupt:
        adc.stop_adc()
        print("Keyboard interrupt")
