# Inspo for this project: # https://theswanstation.net/
# cd OneDrive/Desktop/projects/terminalgame in terminal to go to terminal game directory 
# type 'pipenv shell', then hit enter in terminal to start virtual environment 
# python3 swanstation.py to run script
# pipenv install <libraryname> eg pipenv install sys in terminal to install libraries in virtual environments
# colorama for styling https://pypi.org/project/colorama/
# import those libraries here: 
import random # module that generates random numbers 
import time # for all things time operations eg dates, time stamps
import sys # runtime environment
from colorama import Fore, Style, init # for styling

init()

sys.stdout.write(Fore.GREEN +"\n Every 108 minutes, the button must be pushed. From the moment the alarm sounds, \n you will have four minutes to enter the code into the microcomputer processor. \n Either you or your partners must input the code.\n It is highly recommended that you and your partners take alternating shifts. \n In this manner you will all stay fresh and alert. \n Congratulations! Until your replacements arrive, \n the future of the project is in your hands. \n On behalf of the Degroots, Alvar Hanso, \n and all of us at the Dharma Initiative, thank you. \n Namaste. And good luck. \n The code you have to enter to reset the timer is 4 8 15 16 23 42 (including spaces).\n")

currentcountdown = 0 
    
correctcode = '4 8 15 16 23 42'
    
numberstypedbyuser = input("Please enter the correct code here: ")

# use strip() just in case the user adds a few too many spaces before and after 
if correctcode.strip() == numberstypedbyuser.strip(): 
    print("The countdown has been reset for another 108 minutes.")
else: 
    print("The code was incorrect. Self destruction will commence shortly.")
    
# stdout - standard output is used to display output directly to the screen console
# sys.stdout.write() prints text to the console
# The carriage return '\r' will send the cursor to the beginning of the line, where it 
# can overwrite the existing text.
# This allows the countdown to continue counting down in place
# Otherwise, it will keep printing out an updated countdown 
# with each iteration. 
currentcountdown = 0
for currentcountdown in range(6480, 0, -1):  # 108 minutes * 60 seconds = 6480 seconds
    minutes = currentcountdown // 60  # Calculate minutes without any decimals
    seconds = currentcountdown % 60   # Calculate seconds. Remainder of a division. 
    sys.stdout.write("\r")  # Move cursor to the start of the line
    sys.stdout.write(Style.BRIGHT + "{:2d}:{:2d} remaining.".format(minutes, seconds))  # Format as mm:ss
    sys.stdout.flush()  # updates the counter immediately, in place 
    time.sleep(1) # pause my loop for 1 second to create a real-time countdown effect.
