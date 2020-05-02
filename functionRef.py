# IMPORTS
from time import sleep
import os

#FUNCTIONS
def clear():
    os.system('clear')
def help():
    print("list of commands\n"
          + "help = Display of commands\n"
          + "list = list of all the Latin I vocabulary\n"
          + "tutorial = tutorial on how to use this app and some other stuff for Latin beginners\n"
          + "Quit = exits the main program to the exit credits and then exits the app\n") ; sleep(2.0)
    input("Press enter to exit.")
    clear()

def words():
    wordList = ["salve" , "vale" , "et" , "est" , "in" , "sunt" , "non" , "insula" , "sed" , "oppidum"
                , "quoque" , "canis" , "coquus" , "filia" , "filius" , "hortus" , "mater" , "pater" , "servus" , "via" , "amicus" , "ancilla" , "cena" , "cibus"
                , "intro" , "saluto" , "porto" , "video" , "dominus" , "laetus" , "mercator" , "audio" , "dico" , "unus" , "duo" , "tres" , "quattuor" , "quinque"
                , "sex" , "septem" , "octo" , "novem" , "decem" , "ad" , "ecce" , "magnus" , "parvus" , "ambulo" , "iratus" , "quis" , "quid" , "cur" , "ubi" ,
                "sum" , "eheu" , "pecunia" , "ego" , "tu" , "habeo" , "respondeo" , "venio" , "rideo" , "quod" , "ex" , "voco" , "clamo" , "specto" , "taberna"
                , "laboro" , "clamor" , "femina" , "vir", "puer" , "puella" , "multus" , "urbs" , "agricola" , "curro" , "hodie" , "iuvenis" , "meus" , "senex" , "sto" ,
                "optimus" , "volo" , "fortis" , "emo" , "pulso" , "bonus" , "malus" , "festino" , "per" , "pugno" , "scribo" , "tuus" , "erat" , "paro" , "cum" , "facio" ,
                "heri" , "ingens" , "nihil" , "omnis" , "vendo" , "navis" , "prope" , "rogo" , "terreo" , "inquit" , "tamen" , "eum" , "eam" , "duco" , "saepe" , "interficio" ,
                "habito" , "silva" , "statim" , "totus" , "pessimus" , "cupio" , "celeriter" , "do" , "iterum" , "pulcher" , "dies" , "fero" , "homo" , "maneo" , "medius" , "mox" , 
                "ostendo" , "trado" ,  "nomen" , "accipio" , "frater" , "soror" , "invenio" , "pax" , "bellum" , "nos" , "quam" , "semper" , "taceo" , "stultus" , "callidus" , "uxor" ,
                 "suus" , "solus" , "nuntio" , "magister" , "discipulus" , "doceo" , "subito" , "quaeso" , "capio" , "nunc" , "tum" , "credo" , "de" , "noster" , "placet" , "civis" , "lego"
                 , "sollicitus" , "mons" , "mirabilis" , "templum" , "mitto" , "sentio" , "tandem" , "iam" , "terra" , "custodio" , "fortiter" , "fugio" , "igitur" , "tristis" , "iubeo" , "deleo" , "displodo" , "aeger" , "alter" , "fessus" , "ignavus" , "nolo" , "-ne" , "traho" , "hic" , "ille" , "possum" , "-que" , "ceteri" , "novus" , "se" , "vita" , "attonitus" , "facilis" , "apud" , "decorus" , "ipse" , "iste" , "necesse" , "quamquam" , "deus"] 

    print("List:") ; sleep(2.0)
    print('\n'.join(map(str, wordList))) ; sleep(2.0)
    input("Press enter to exit.")
    clear()

def tutorial():
    print("Are you new to Latin?")
    new = str.lower(input())
    if new == "yes":
        new = True
    else:
        new = False
    clear()
    print("Starting tutorial.") ; sleep(1.0)
    print("If you need help with the app itself just say: help or Help to see all of the avaliable commands you could do.") ; sleep(1.5)
    print("The { } means that the other meaning is present but the Nominative, Dative, and Accusative meanings are also there.") ; sleep(1.5)
    print("In order to quit you have to input: Quit") ; sleep(1.5)
    if new == True:
        print("If you're new to Latin the ''v'' is spelled as a ''w''. For example: Salve would be Salwe.") ; sleep(1.5)
        print("There are a present, imperfect and perfect tenses.") ; sleep(1.5)
        print("The present tense is the what it means, your using the present tence like habeo which is have.") ; sleep(1.5)
        print("The imperfect tense works like the past tense, meaning that habeo in the imperfect tence would be habebam which means was having") ; sleep(1.5)
        print("The perfect tense works kind of similar to the past tence since instead of using the ''ba'' its using ''bui'' for the case for habui which means haved. But for most latin words it would be ''vi''") ; sleep(1.5)
        input("Press enter to exit.")
        print("Exiting Tutorial") ; sleep(1.0)
        clear()
    else:
        input("Press enter to exit.")
        print("Exiting Tutorial") ; sleep(1.0)
        clear()