import csv
import pump_ctrl
from time import sleep

RECIPE_FILE = "pump_data/recipelist.csv"

# Return the list of drink names from the recipe file
def get_drink_list():
    with open(RECIPE_FILE, mode='r') as file:
        reader = csv.reader(file)
        return [row[0] for row in reader]

# Make a drink using specific amounts for each pump
def make_drink(pump1_amt=0, pump2_amt=0, pump3_amt=0, pump4_amt=0):
    pump_ctrl.actuate_pump(1, pump1_amt)
    sleep(0.25)
    pump_ctrl.actuate_pump(2, pump2_amt)
    sleep(0.25)
    pump_ctrl.actuate_pump(3, pump3_amt)
    sleep(0.25)
    pump_ctrl.actuate_pump(4, pump4_amt)
    sleep(0.25)

# Make a drink based on the name from the recipe file
def make_drink_from_list(drink_name):
    try:
        with open(RECIPE_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Check if the drink name matches
                if row[0].strip().lower() == drink_name.strip().lower():
                    # Extract ingredient amounts
                    pump1_amt = float(row[1])
                    pump2_amt = float(row[2])
                    pump3_amt = float(row[3])
                    pump4_amt = float(row[4])
                    # Use make_drink to create the drink
                    make_drink(pump1_amt, pump2_amt, pump3_amt, pump4_amt)
                    print(f"Successfully made {drink_name}!")
                    return
            # If no match found, raise an error
            raise ValueError(f"Drink '{drink_name}' not found in the recipe list.")
    except FileNotFoundError:
        print(f"Error: {RECIPE_FILE} not found. Please ensure the file exists.")
    except Exception as e:
        print(f"Error: {e}")
