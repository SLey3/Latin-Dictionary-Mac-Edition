# VARIABLE DEFINITIONS
userInput = ""

# IMPORTS
from time import sleep
import functionRef
import os

# START OF APPLICATION AND MAIN LOOP
os.system('clear')
print("Welcome, this a app that is still under development for Latin I. This app will be updated weekly.") ; sleep(2.5)
print("This is mean't only for Latin I currently.") ; sleep(1.5)
print("Please note that this app is only mean't for Latin I vocab words and not focused on sentences and stuff further than that.") ; sleep(1.8) 
os.system('clear')
print("Do you want a tutorial on using this app?") ; sleep(1.0)
responce = input()
os.system('clear')
if(responce == "Yes" or responce == "yes"):
    functionRef.tutorial()
    os.system('clear')
else:
    print("skipping tutorial.") ; sleep(0.5)
    os.system('clear')

while(userInput != "Quit"):
    userInput = functionRef.userInstructions(userInput)

# EXITING STAGE OF THE APPLICATION
os.system('clear')