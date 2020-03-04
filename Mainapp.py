# VARIABLE DEFINITIONS
userInput = ""

# IMPORTS
from time import sleep
import functionRef
import os
clear = lambda: os.system('clear') #makes it so that we do not have to write "os.system('clear)" a million times and makes the code easier to read

# START OF APPLICATION AND MAIN LOOP
clear()
print("Welcome, this an app that is still under development for Latin I. This app will be updated weekly.") ; sleep(2.5)
print("This is meant only for Latin I currently.") ; sleep(1.5)
print("Please note that this app is only meant for Latin I vocab words and is not focused on sentences and stuff further than that.") ; sleep(1.8) 
clear()
print("Do you want a tutorial on using this app? (yes/no)") ; sleep(1.0)
response = input() 
clear()
if(str.lower(response) == "yes"): #str.lower makes it so that we do not have to worry about the user's input being uppercase because the user's input will be converted into lowercase (using str.lower for "response = input() causes bugs"
    functionRef.tutorial()
    clear()
else:
    print("skipping tutorial.") ; sleep(0.5)
    clear()

while(str.lower(userInput) != "quit"): #quit should be entirely lowercase because all of the other commands are and it makes the dictionary less confusing
    userInput = functionRef.userInstructions(userInput)

# EXITING STAGE OF THE APPLICATION
clear()
