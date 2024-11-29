import csv
import pump_ctrl
from time import sleep

RECIPE_FILE = "pump_data/recipelist.csv"

# Return the list of drink names from the recipe file
def get_drink_list():
    with open(RECIPE_FILE, mode='r') as file:
        reader = csv.reader(file)
        return [row[0] for row in reader]

# Load recipes from the recipe file
def load_recipes():
    recipes = {}
    with open(RECIPE_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            drink, *amounts = row
            recipes[drink.lower()] = [float(amount) for amount in amounts]
    return recipes

# Get available drinks based on storage levels
def get_available_drinks(recipes):
    storage_levels = pump_ctrl.read_storage()
    available_drinks = []
    for drink, amounts in recipes.items():
        if all(storage_levels[i] >= amounts[i] for i in range(len(amounts))):
            available_drinks.append(drink)
    return available_drinks

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

# Make a drink based on its name
def make_drink_from_list(drink_name, recipes):
    drink_name = drink_name.lower()
    if drink_name not in recipes:
        raise ValueError(f"Drink '{drink_name}' not found in the recipe list.")

    amounts = recipes[drink_name]
    for pump, amount in enumerate(amounts, start=1):
        if amount > 0:
            pump_ctrl.actuate_pump(pump, amount)

    print(f"Successfully made {drink_name}!")
