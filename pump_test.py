#Note need to pip3 install adafruit-circuitpython-motorkit

import time
import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())

#run motors for # seconds
kit.motor1.throttle = 1.0

time.sleep(5.9)

kit.motor1.throttle = 0
