# Import necessary libraries
import sys  # sys is used to access system-specific parameters and functions
import time  # time is used to handle time-related tasks such as pauses (sleep)

# Display a welcome message with the developer's name
print("\nWelcome Branch - Developer: Hayven Baarson")

# Display the version of the software being run
print("\nWelcome to InfoTechCenter v1.0\n")

# Initialize variables
x = 0  # Counter for the number of iterations
ellipsis = 0  # Variable to control the number of dots in the loading message

# Loop that will run 20 times
while x != 20:
    x += 1  # Increment counter x by 1 on each iteration
    message = ("InfoTech Center System Booting" + "." * ellipsis)  # Prepare the message with increasing dots
    ellipsis += 1  # Increase the number of dots to create a "loading" effect
    sys.stdout.write("\r" + message)  # Output the message on the same line, overwriting the previous one
    time.sleep(0.5)  # Wait for 0.5 seconds before the next iteration

    # Reset ellipsis back to 0 after 4 dots for a repeating pattern
    if ellipsis == 4:
        ellipsis = 0

    # When the loop has run 20 times, print the final message
    if x == 20:
        print("\nOperating System Booted Up - Retina Scanned - Access Granted\n")
