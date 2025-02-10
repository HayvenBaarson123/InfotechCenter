print("\n**********************************\n")

print("Weather Branch - Developer: Hayven Baarson\n")

#Import Libraries HERE!
import random
from time import sleep

# Weather Function to determine the weather
def weather():
    weatherForecastList = ["snowing", "a blizzard" ,"icy" ,"rainy" ,"windy" ,"sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert=="snowing":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because"
              " it is", weatherAlert, "outside.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated your alarm by 60 minutes because"
              "it is a"), weatherAlert, "outside"
vehicleResponseSystem()