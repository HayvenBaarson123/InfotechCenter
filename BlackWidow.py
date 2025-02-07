#Libraries HERE
import sys
import time


print("\nWelcome Branch - Developer: Hayven Baarson")


print("\nWelcome to InfoTechCenter v1.0\n")

x = 0
ellipsis = 0

while x != 20:
    x+=1
    message = ("InfoTech Center System Booting" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r" + message)
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:

        print("\n\Operating System Booted Up - Retina Scanned - Access Granted\n")