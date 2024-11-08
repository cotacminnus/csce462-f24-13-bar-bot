#Note need to pip3 install adafruit-circuitpython-motorkit

import time
import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())
'''
for i in range(1):
    print("Running motor 1")
    kit.motor1.throttle = 1.0
    time.sleep(0.5)
    kit.motor1.throttle = 0
    print("Stopping motor 1")
    time.sleep(0.5)
    
    print("Running motor 2")
    kit.motor2.throttle = 1.0
    time.sleep(0.5)
    kit.motor2.throttle = 0
    print("Stopping motor 2")
    time.sleep(0.5)
    
    print("Running motor 3")
    kit.motor3.throttle = 1.0
    time.sleep(0.5)
    kit.motor3.throttle = 0
    print("Stopping motor 3")
    time.sleep(0.5)
    
    print("Running motor 4")
    kit.motor4.throttle = 1.0
    time.sleep(0.5)
    kit.motor4.throttle = 0
    print("Stopping motor 4")
    time.sleep(0.5)
'''
#run motors for # seconds
kit.motor1.throttle = 1.0
kit.motor2.throttle = 1.0
kit.motor3.throttle = 1.0
kit.motor4.throttle = 1.0

time.sleep(2)

kit.motor1.throttle = 0
kit.motor2.throttle = 0
kit.motor3.throttle = 0
kit.motor4.throttle = 0