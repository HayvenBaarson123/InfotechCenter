import random

# Weather conditions with alarm time and speed
weather_responses = {
    "snowing": (30, 60), "blizzard": (60, 50),
    "rainy": (10, 70), "windy": (60, 75), "icy": (60, 55)
}

weatherAlert = random.choice(list(weather_responses.keys()))
alarm_time, speed = weather_responses.get(weatherAlert, (None, None))

# Output based on weather condition
print(f"\n**********************************\nWeather Branch - Developer: Hayven Baarson")
if alarm_time:
    print(f"\nThe National Weather Service has updated your alarm by {alarm_time} minutes because it is {weatherAlert} outside.")
    print(f"VRS has been initiated allowing us to go {speed} MPH.")
else:
    print(f"\nThe National Weather Service is calling for {weatherAlert} sky outside, drive safe!")
    print("\nVRS has been Deactivated allowing us to go however fast you want.")
