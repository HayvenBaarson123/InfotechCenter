print("\n**********************************\n")

print("Weather Branch - Developer: Hayven Baarson\n")

#Import Libraries HERE!
import random
from time import sleep

# Weather Function to determine the weather
def weather():
    weatherForecastList = ["snowing", "blizzard" ,"ice" ,"rainy" ,"windy" ,"sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition
    
print(weather())

