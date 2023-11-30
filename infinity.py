# https://opi-gpio.readthedocs.io/en/latest/api-documentation.html
import OPi.GPIO as GPIO
import pymysql
import time
from datetime import datetime

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)



GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button

                   ### R1 ###
                                                          # 1 pin
                                                          # 2 pin
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)        # 3 pin
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)        # 4 pin
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)        # 5 pin
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)        # 6 pin
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)        # 7 pin
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)        # 8 pin
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)        # 9 pin
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)        #10 pin

                   ### R2 ###
                                                          # 1 pin
                                                          # 2 pin
GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)        # 3 pin
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)        # 4 pin
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)        # 5 pin
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)        # 6 pin
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)        # 7 pin
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)        # 8 pin

                  ### PWM ###
pwm1 = GPIO.PWM(32, 10000)        # 1 pin
pwm2 = GPIO.PWM(33, 10000)        # 2 pin
pwm3 = GPIO.PWM(7, 10000)         # 3 pin
pwm4 = GPIO.PWM(16, 10000)        # 4 pin

# if GPIO.input(channel):
#     print('Input was HIGH')
# else:
#     print('Input was LOW')
# while GPIO.input(channel) == GPIO.LOW:
#     time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things


def run():
    print(GPIO.RPI_INFO)
    print(GPIO.RPI_INFO['P1_REVISION'])
    print(GPIO.VERSION)
    while True:
        pass



if __name__ == '__main__':
    run()