
import sys  # sys is used to access system-specific parameters and functions
import time  # time is used to handle time-related tasks such as pauses (sleep)
import random

# ANSI escape sequences for coloring
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
MAGENTA = "\033[35m"
WHITE = "\033[97m"
BLUE = "\033[34m"

# Display a welcome message with the developer's name
print(f"{CYAN}{BOLD}\nWelcome Branch - Developer: Hayven Baarson{RESET}")

# Display the version of the software being run
print(f"{GREEN}{BOLD}\nWelcome to InfoTechCenter v1.0\n{RESET}")

# Initialize variables
x = 0  # Counter for the number of iterations
ellipsis = 0  # Variable to control the number of dots in the loading message

# Loop that will run 20 times
while x != 20:
    x += 1  # Increment counter x by 1 on each iteration
    message = f"{YELLOW}InfoTech Center System Booting" + "." * ellipsis  # Prepare the message with increasing dots
    ellipsis += 1  # Increase the number of dots to create a "loading" effect
    sys.stdout.write("\r" + message)  # Output the message on the same line, overwriting the previous one
    time.sleep(0.5)  # Wait for 0.5 seconds before the next iteration

    # Reset ellipsis back to 0 after 4 dots for a repeating pattern
    if ellipsis == 4:
        ellipsis = 0

    # When the loop has run 20 times, print the final message
    if x == 20:
        print(f"{GREEN}\n\nOperating System Booted Up - Retina Scanned - Access Granted\n{RESET}")

# Weather conditions with alarm time and speed
weather_responses = {
    "snowing": (30, 60), "blizzard": (60, 50),
    "rainy": (10, 70), "windy": (60, 75), "icy": (60, 55)
}

weatherAlert = random.choice(list(weather_responses.keys()))
alarm_time, speed = weather_responses.get(weatherAlert, (None, None))

# Output based on weather condition
print(f"\n{MAGENTA}**********************************{RESET}")
print(f"{CYAN}Weather Branch - Developer: Hayven Baarson{RESET}")
if alarm_time:
    print(f"\n{RED}The National Weather Service has updated your alarm by {alarm_time} minutes because it is {weatherAlert} outside.{RESET}")
    print(f"{WHITE}VRS has been initiated allowing us to go {speed} MPH.{RESET}")
else:
    print(f"\n{RED}The National Weather Service is calling for {weatherAlert} sky outside, drive safe!{RESET}")
    print("\nVRS has been Deactivated allowing us to go however fast you want.")
