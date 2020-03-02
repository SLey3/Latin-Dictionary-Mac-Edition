#IMPORTS
from time import sleep
import os
import csv
clear = lambda: os.system('clear') #makes it so that we do not have to write "os.system('clear')" a million times and makes the code easier to read


#FUNCTIONS
def help():
    print("list of commands\n"
          + "help = Display of commands\n"
          + "list = list of all the Latin I vocabulary\n"
          + "tutorial = tutorial on how to use this app and some other stuff for Latin beginners\n"
          + "quit = exits the main program to the exit credits and then exits the app\n") ; sleep(2.0)
    input("Press enter to exit.")
    clear()

    
def userInstructions(userInput): #made things efficient using string.lower so that we do not have to write "Help or help" because the input is converted into lowercase
    if userInput == "":
        clear()
    elif str.lower(userInput) == "help":
        clear()
        help()
    elif str.lower(userInput) == "list":
        clear()
        words()
    elif str.lower(userInput) == "tutorial":
        clear()
        tutorial()
    else:
        clear()
        valid = False
        csv_file = csv.reader(open('LatinDictRef.csv', 'r'))
        for line in csv_file:
            if line[0] == str.lower(userInput):
                valid = True
                return input(f"Word: {line[0]}\n Definitions: {line[1]}, {line[2]}\n Plural: {line[3]}\n Present Form: {line[4]}\n Imperfect Form: {line[5]}\n Perfect Form: {line[6]}\n Grammatical Gender: {line[7]}\n\n Press enter to exit.")
            else:
                clear() 
        if not valid:
            print(f"'{userInput}' is not a supported command or word.")
        else:
            valid = False

    return input('\nType in your command or any Latin word to review or learn. Enter your response: ')

def words():
    csvSheet = csv.reader(open("LatinDictRef.csv", 'r'))
    
    print("Word List:") ; sleep(2.0)
    for line in csvSheet:
        print(line[0])
    input("Press enter to exit.")
    clear()


def tutorial():
    print("Are you new to Latin? (yes/no)")
    new = str.lower(input())
    if new == "yes":
        new = True
    else:
        new = False
    clear()
    print("Starting tutorial.") ; sleep(1.0)
    print("If you need help with the app itself just say: help or Help to see all of the avaliable commands you could do.") ; sleep(1.5)
    print("In order to quit you have to input: Quit") ; sleep(1.5)
    if new: #removed "== true" because it is unecessary
        print("If your new to latin the ''v'' is spelled as a ''w''. For example: Salve would be Salwe.") ; sleep(1.5)
        print("There is a present, imperfect and perfect tense.") ; sleep(1.5)
        print("The present tense is the what it means, your using the present tense like habeo which is have.") ; sleep(1.5)
        print("The imperfect tense works like the past tense, meaning that habeo in the imperfect tense would be habebam which means was having") ; sleep(1.5)
        print("The perfect tense works kind of similar to the past tense since instead of using the ''ba'' its using ''bui'' for the case for habui which means haved. But for most latin words it would be ''vi''") ; sleep(1.5)
        input("Press enter to exit.")
        clear()
    else:
        input("Press enter to exit.")
        clear()
