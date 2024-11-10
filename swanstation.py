# type 'pipenv shell', then hit enter in terminal to start virtual environment 
# pipenv install <libraryname> eg pipenv install sys in terminal to install libraries in virtual environments
# cd OneDrive/Desktop/projects/terminalgame in terminal to go to terminal game directory 
# python3 swanstation.py to run script


import random 
import time
import sys
from colorama import Fore, Style, init

init()


# https://theswanstation.net/
# https://docs.python.org/3/library/curses.html#module-curses 

print("\n Every 108 minutes, the button must be pushed. From the moment the alarm sounds, \n you will have four minutes to enter the code into the microcomputer processor. \n Either you or your partners must input the code.\n It is highly recommended that you and your partners take alternating shifts. \n In this manner you will all stay fresh and alert. \n Congratulations! Until your replacements arrive, \n the future of the project is in your hands. \n On behalf of the Degroots, Alvar Hanso, \n and all of us at the Dharma Initiative, thank you. \n Namaste. And good luck. \n The code you have to enter to reset the timer is 4 8 15 16 23 42 (including spaces).")

currentcountdown = 0 

while currentcountdown: 
    print("You can only enter the code once the countdown is reached")
    
correctcode = '4 8 15 16 23 42'
    
numberstypedbyuser = input("Please enter the correct code here:")

# use strip() just in case the user adds a few too many spaces before and after 
if correctcode.strip() == numberstypedbyuser.strip(): 
    print("The countdown has been reset for another 108 minutes")
else: 
    print('The code was incorrect. Self destruction will commence shortly.')
    
# stdout - standard output is used to display output directly to the screen console
# sys.stdout.write() prints text to the console
# The carriage return '\r' will send the cursor to the beginning of the line, where it 
# can overwrite the existing text.
# This allows the countdown to continue counting down in place
# Otherwise, it will keep printing out an updated countdown 
# with each iteration. 
for currentcountdown in range(6480, 0, -1): #108 minutes * 60 seconds = 6480 seconds, no skipping 0, count backwards -1
    sys.stdout.write("\r") 
    sys.stdout.write("{:d} seconds remaining.".format(currentcountdown))   
    sys.stdout.flush()
    time.sleep(1)

'''
How to add colour to terminal game. Need to check the following libraries for suitability. 

print(Fore.RED + "This is red text")
print(Fore.GREEN + "This is green text")
print(Style.RESET_ALL + "Back to default text")
Style.BRIGHT or Style.DIM

pip install termcolor.
from termcolor import colored
print(colored("This is blue text", "blue"))
print(colored("This is yellow text on a red background", "yellow", "on_red"))   

import sys
remaining_seconds = 125  # Example value

# need to update timer format for better readability? 
minutes = remaining_seconds // 60  
seconds = remaining_seconds % 60   

sys.stdout.write("{:d} minutes and {:02d} seconds remaining.".format(minutes, seconds))

2 minutes and 05 seconds remaining.

from blessed import Terminal

term = Terminal()
print(term.red("This is red text"))
print(term.bold("This is bold text"))
print(term.blink("This is blinking text"))


 Termcolor
 Run pip install termcolor.
Usage:
python
from termcolor import colored

print(colored("This is blue text", "blue"))
print(colored("This is yellow text on a red background", "yellow", "on_red"))
'''