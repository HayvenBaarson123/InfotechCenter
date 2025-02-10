# Print initial message with a separator
print("\n**********************************\n")

# Print developer information
print("Weather Branch - Developer: Hayven Baarson\n")

# Import required libraries
import random  # For generating random weather condition
from time import sleep  # For adding delays if needed (though not used in this code)

# Weather function to determine the weather condition
def weather():
    # List of possible weather conditions
    weatherForecastList = ["snowing", "blizzard" ,"icy" ,"rainy" ,"windy" ,"sunny"]
    
    # Randomly choose one weather condition from the list
    weatherCondition = random.choice(weatherForecastList)
    
    # Return the chosen weather condition
    return weatherCondition

# Call the weather function and store the result in the variable 'weatherAlert'
weatherAlert = weather()

# Vehicle response system based on weather conditions
def vehicleResponseSystem():
    # Check if the weather is snowing
    if weatherAlert == "snowing":
        # Update alarm time based on snowing weather
        print("\nThe National Weather Service has updated your alarm by 30 minutes because"
              " it is", weatherAlert, "outside.")
    # Check if the weather is a blizzard
    elif weatherAlert == "blizzard":
        # Update alarm time for blizzard conditions
        print("\nThe National Weather Service has updated your alarm by 60 minutes because"
              " it is a", weatherAlert, "outside")
    # Check if the weather is rainy
    elif weatherAlert == "rainy":
        # Update alarm time for rainy conditions
        print("\nThe National Weather Service has updated your alarm by 10 minutes because"
              " it is a", weatherAlert, "outside")
    # Check if the weather is windy
    elif weatherAlert == "windy":
        # Update alarm time for windy conditions
        print("\nThe National Weather Service has updated your alarm by 60 minutes because"
              " it is a", weatherAlert, "outside")
    # Check if the weather is icy
    elif weatherAlert == "icy":
        # Update alarm time for icy conditions
        print("\nThe National Weather Service has updated your alarm by 60 minutes because"
              " it is a", weatherAlert, "outside")
    else:
        # If the weather is sunny, notify the user to drive safe
        print("\nThe National Weather Service is calling for", weatherAlert, "sky outside, drive safe!")
        
# Call the vehicleResponseSystem function to execute the weather alert system
vehicleResponseSystem()
