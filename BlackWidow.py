import random
from time import sleep

print("\n******************************************************\n")
print("Gasoline Branch - Developer: Hayven Baarson\n")


def get_gas_level_and_station():
    gas_level_list = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    gas_station_list = ["Shell", "Marathon", "Speedway", "Circle K", "7/11", "Wesco", "Meijer", "WaWa"]

    # Choose random values for gas level and station
    gas_level = random.choice(gas_level_list)
    if gas_level in ["Empty", "Low", "Quarter Tank"]:
        miles_to_station = round(random.uniform(1, 50), 1)
    else:
        miles_to_station = None  # No need to show miles for Half, Three Quarter, or Full Tank

    station = random.choice(gas_station_list)

    return gas_level, miles_to_station, station


def gas_level_alert():
    gas_level, miles_to_station, station = get_gas_level_and_station()

    # Handle each gas level case
    if gas_level == "Empty":
        print("****WARNING - YOU ARE OUT OF GAS****\n")
        sleep(3.25)
        print("Calling AAA")
    elif gas_level == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station.\n")
        sleep(3.25)
        print(f"The closest gas station is {station}, which is {miles_to_station} miles away.\n")
    elif gas_level == "Quarter Tank":
        print("Your tank is on a Quarter Tank, checking GPS for the closest gas station\n")
        sleep(3.25)
        print(f"The closest gas station is {station}, which is {miles_to_station} miles away.\n")
    elif gas_level == "Half Tank":
        print("You're at half a tank, which is plenty to get to your destination.\n")
    elif gas_level == "Three Quarter Tank":
        print("You're at Three Quarter tank, which is plenty to get to your destination.\n")
    else:
        print("Your gas tank is FULL!")


gas_level_alert()
