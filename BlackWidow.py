import random
from time import sleep

# Printing initial information about the developer and the program
print("\n******************************************************\n")
print("Gasoline Branch - Developer: Hayven Baarson\n")


def get_gas_level_and_station():
    # List of possible gas levels
    gas_level_list = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    # List of available gas stations
    gas_station_list = ["Shell", "Marathon", "Speedway", "Circle K", "7/11", "Wesco", "Meijer", "WaWa"]

    # Choose a random gas level from the list
    gas_level = random.choice(gas_level_list)

    # Determine the miles to the closest station based on gas level
    if gas_level in ["Empty", "Low", "Quarter Tank"]:
        miles_to_station = round(random.uniform(1, 50), 1)  # Generate a random distance between 1 and 50 miles
    else:
        miles_to_station = None  # No need to provide miles if the tank is at Half, Three Quarter, or Full

    # Choose a random gas station from the list
    station = random.choice(gas_station_list)

    # Return the gas level, miles to station (if applicable), and the chosen station
    return gas_level, miles_to_station, station


def gas_level_alert():
    # Get the current gas level, miles to the station, and the station name
    gas_level, miles_to_station, station = get_gas_level_and_station()

    # Handle each possible gas level situation
    if gas_level == "Empty":
        print("****WARNING - YOU ARE OUT OF GAS****\n")
        sleep(3.25)  # Pause for dramatic effect
        print("Calling AAA")  # Simulate calling for roadside assistance
    elif gas_level == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station.\n")
        sleep(3.25)  # Pause for dramatic effect
        print(f"The closest gas station is {station}, which is {miles_to_station} miles away.\n")
    elif gas_level == "Quarter Tank":
        print("Your tank is on a Quarter Tank, checking GPS for the closest gas station\n")
        sleep(3.25)  # Pause for dramatic effect
        print(f"The closest gas station is {station}, which is {miles_to_station} miles away.\n")
    elif gas_level == "Half Tank":
        print("You're at half a tank, which is plenty to get to your destination.\n")
    elif gas_level == "Three Quarter Tank":
        print("You're at Three Quarter tank, which is plenty to get to your destination.\n")
    else:
        print("Your gas tank is FULL!")  # If the tank is full, no concern about running out of gas


# Call the function to simulate the alert process
gas_level_alert()
