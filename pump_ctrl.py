import time
import board
from adafruit_motorkit import MotorKit
import csv

# Motors run at 1.8 LPM, additional testing may be required
kit = MotorKit(i2c=board.I2C())

# File path for the storage CSV
STORAGE_FILE = "pump_data/storage.csv"

# Reads storage levels from storage.csv
def read_storage():
    with open(STORAGE_FILE, mode='r') as file:
        reader = csv.reader(file)
        return [float(entry) for entry in next(reader)]

# Writes updated storage levels back to storage.csv
def write_storage(storage_levels):
    with open(STORAGE_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(storage_levels)

#Changes storage values during runtime
def refill_storage(amt_1, amt_2, amt_3, amt_4):
    with open(STORAGE_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(amt_1,amt_2,amt_3,amt_4)


# Calculates how long pump should run to dispense x amount of liquid
def convert_mL_to_sec(milliliters):
    return (milliliters / 30.0) - .1

# Dispenses liquid from the selected pump for the given amount
def actuate_pump(pump, amount):
    # Read current storage levels
    #storage_levels = read_storage()
    
    # Validate the pump number
    #if pump < 1 or pump > 4:
        #raise ValueError(f"Invalid pump value: {pump}. Please choose a pump between 1 and 4.")
    
    # Check if there is enough liquid in the selected pump
    #if storage_levels[pump - 1] < amount:
       # raise ValueError(f"Not enough liquid in Pump {pump}. Available: {storage_levels[pump - 1]} mL, Requested: {amount} mL")
    
    # Update the storage levels
    #storage_levels[pump - 1] -= amount
    #write_storage(storage_levels)
    
    # Actuate the pump
    t = convert_mL_to_sec(amount)
    motor = getattr(kit, f"motor{pump}")
    motor.throttle = 1.0
    time.sleep(t)
    motor.throttle = 0.0

    #print(f"Pump {pump} dispensed {amount} mL. Remaining: {storage_levels[pump - 1]} mL.")
