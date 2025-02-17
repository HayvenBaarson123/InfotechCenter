print("\n******************************************************\n")
print("Gasoline Branch - Developer: Hayven Baarson")

import random
from time import sleep

def gasLevelGauge():
  gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
  return random.choice(gasLevelList)
  

def gasStation():
  gasStationsList = ["Shell","Marathon","Speedway","Circle K","7/11","Wesco","Meijer","WaWa"]
  return random.choice(gasStationsList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.006751,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("****WARNING - YOU ARE OUT OF GAS****\n")
        sleep(3.25)
        print("Calling AAA")
    elif gasLevelIndicator == "Low":
        print("your gas tank is extremly low, checking GPS for the closest gas station")
        sleep(3.25)
        print("The closest gas station is", gasStation(), "which is", milesToGasStationLow, "miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your tank is on a Quarter Tank, checking GPS for the closest gas station")
        sleep(3.25)
        print("The closest gas station is", gasStation(), "which is", milesToGasStationQuarterTank, "miles away")
    elif gasLevelIndicator == "Half Tank":
        print("Your at half a tank, witch is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your at Three Quarter tank, witch is plenty to get to your destination.")
    else:
        print("Your gas tank is FULL!")
gasLevelAlert()
