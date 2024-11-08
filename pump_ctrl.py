import time
import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())


#TODO Calculates how long pump should run to get 
def convert_floz_to_time():
    return

#Dispense liquid from chosen pump for t amount of time
def actuate_pump(pump, t):
    if pump == 1:
        kit.motor1.throttle = 1.0
        time.sleep(t)
        kit.motor1.throttle = 0.0
    elif pump == 2:
        kit.motor2.throttle = 1.0
        time.sleep(t)
        kit.motor2.throttle = 0.0
    elif pump == 3:
        kit.motor3.throttle = 1.0
        time.sleep(t)
        kit.motor3.throttle = 0.0
    elif pump == 4:
        kit.motor4.throttle = 1.0
        time.sleep(t)
        kit.motor4.throttle = 0.0
    else:
        raise ValueError(f"Invalid pump value: {pump}. Please choose a pump between 1 and 4.")
    
def actuate_all_pump(t=6):  #default is 6sec
    kit.motor1.throttle = 1.0
    kit.motor2.throttle = 1.0
    kit.motor3.throttle = 1.0
    kit.motor4.throttle = 1.0

    time.sleep(t)

    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    
#   add functions as needed
class PumpCtrl:
    def control(self):
        return None