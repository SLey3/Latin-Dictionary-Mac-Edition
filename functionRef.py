#IMPORTS
from time import sleep
import os
import LatinRef

#FUNCTIONS
def help():
    print("list of commands\n"
          + "help = Display of commands\n"
          + "list = list of all the Latin I vocabulary\n"
          + "tutorial = tutorial on how to use this app and some other stuff for Latin beginners\n"
          + "Quit = exits the main program to the exit credits and then exits the app\n") ; sleep(2.0)
    input("Press enter to exit.")
    clear = lambda: os.system('clear')
    clear()

    
def userInstructions(userInput):
    if userInput == "help" or userInput == "Help":
        os.system("clear")
        help()
    elif userInput == "list" or userInput == "List":
        os.system("clear")
        words()
    elif userInput == "tutorial" or userInput == "Tutorial":
        os.system("clear")
        tutorial()
    elif userInput == "salve" or userInput == "Salve":
        os.system("clear")
        LatinRef.salve()
        input("Press enter to exit.")
    elif userInput == "vale" or userInput == "Vale":
        os.system("clear")
        LatinRef.vale()
        input("Press enter to exit.")
    elif userInput == "et" or userInput == "Et":
        os.system("clear")
        LatinRef.et()
        input("Press enter to exit.")
    elif userInput == "est" or userInput == "Est":
        os.system("clear")
        LatinRef.est()
        input("Press enter to exit.")
    elif userInput == "in" or userInput == "In":
        os.system("clear")
        LatinRef.In()
        input("Press enter to exit.")
    elif userInput == "sunt" or userInput == "Sunt":
        os.system("clear")
        LatinRef.sunt()
        input("Press enter to exit.")
    elif userInput == "non" or userInput == "Non":
        os.system("clear")
        LatinRef.non()
        input("Press enter to exit.")
    elif userInput == "insula" or userInput == "Insula":
        os.system("clear")
        LatinRef.insula()
        input("Press enter to exit.")
    elif userInput == "sed" or userInput == "Sed":
        os.system("clear")
        LatinRef.sed()
        input("Press enter to exit.")
    elif userInput == "oppidum" or userInput == "Oppidum":
        os.system("clear")
        LatinRef.oppidum()
        input("Press enter to exit.")
    elif userInput == "quoque" or userInput == "Quoque":
        os.system("clear")
        LatinRef.quoque()
        input("Press enter to exit.")
    elif userInput == "canis" or userInput == "Canis":
        os.system("clear")
        LatinRef.canis()
        input("Press enter to exit.")
    elif userInput == "coquus" or userInput == "Coquus":
        os.system("clear")
        LatinRef.coquus()
        input("Press enter to exit.")
    elif userInput == "filia" or userInput == "Filia":
        os.system("clear")
        LatinRef.filia()
        input("Press enter to exit.")
    elif userInput == "filius" or userInput == "Filius":
        os.system("clear")
        LatinRef.filius()
        input("Press enter to exit.")
    elif userInput == "hortus" or userInput == "Hortus":
        os.system("clear")
        LatinRef.hortus()
        input("Press enter to exit.")
    elif userInput == "mater" or userInput == "Mater":
        os.system("clear")
        LatinRef.mater()
        input("Press enter to exit.")
    elif userInput == "pater" or userInput == "Pater":
        os.system("clear")
        LatinRef.pater()
        input("Press enter to exit.")
    elif userInput == "servus" or userInput == "Servus":
        os.system("clear")
        LatinRef.servus()
        input("Press enter to exit.")
    elif userInput == "via" or userInput == "Via":
        os.system("clear")
        LatinRef.via()
        input("Press enter to exit.")
    elif userInput == "amicus" or userInput == "Amicus":
        os.system("clear")
        LatinRef.amicus()
        input("Press enter to exit.")
    elif userInput == "ancilla" or userInput == "Ancilla":
        os.system("clear")
        LatinRef.ancilla()
        input("Press enter to exit.")
    elif userInput == "cena" or userInput == "Cena":
        os.system("clear")
        LatinRef.cena()
        input("Press enter to exit.")
    elif userInput == "cibus" or userInput == "cibus":
        os.system("clear")
        LatinRef.cibus()
        input("Press enter to exit.")
    elif userInput == "intro" or userInput == "Intro":
        os.system("clear")
        LatinRef.intro()
        input("Press enter to exit.")
    elif userInput == "saluto" or userInput == "Saluto":
        os.system("clear")
        LatinRef.saluto()
        input("Press enter to exit.")
    elif userInput == "porto" or userInput == "Porto":
        os.system("clear")
        LatinRef.porto()
        input("Press enter to exit.")
    elif userInput == "video" or userInput == "Video":
        os.system("clear")
        LatinRef.video()
        input("Press enter to exit.")
    elif userInput == "dominus" or userInput == "Dominus":
        os.system("clear")
        LatinRef.dominus()
        input("Press enter to exit.")
    elif userInput == "laetus" or userInput == "Laetus":
        os.system("clear")
        LatinRef.laetus()
        input("Press enter to exit.")
    elif userInput == "mercator" or userInput == "Mercator":
        os.system("clear")
        LatinRef.mercator()
        input("Press enter to exit.")
    elif userInput == "audio" or userInput == "Audio":
        os.system("clear")
        LatinRef.audio()
        input("Press enter to exit.")
    elif userInput == "dico" or userInput == "Dico":
        os.system("clear")
        LatinRef.dico()
        input("Press enter to exit.")
    elif userInput == "unus" or userInput == "Unus":
        os.system("clear")
        LatinRef.unus()
        input("Press enter to exit.")
    elif userInput == "duo" or userInput == "Duo":
        os.system("clear")
        LatinRef.duo()
        input("Press enter to exit.")
    elif userInput == "tres" or userInput == "Tres":
        os.system("clear")
        LatinRef.tres()
        input("Press enter to exit.")
    elif userInput == "quattuor" or userInput == "Quattuor":
        os.system("clear")
        LatinRef.quattuor()
        input("Press enter to exit.")
    elif userInput == "quinque" or userInput == "Quinque":
        os.system("clear")
        LatinRef.quinque()
        input("Press enter to exit.")
    elif userInput == "sex" or userInput == "Sex":
        os.system("clear")
        LatinRef.sex()
        input("Press enter to exit.")
    elif userInput == "septem" or userInput == "Septem":
        os.system("clear")
        LatinRef.septem()
        input("Press enter to exit.")
    elif userInput == "octo" or userInput == "Octo":
        os.system("clear")
        LatinRef.octo()
        input("Press enter to exit.")
    elif userInput == "novem" or userInput == "Novem":
        os.system("clear")
        LatinRef.novem()
        input("Press enter to exit.")
    elif userInput == "decem" or userInput == "Decem":
        os.system("clear")
        LatinRef.decem()
        input("Press enter to exit.")
    elif userInput == "ad" or userInput == "Ad":
        os.system("clear")
        LatinRef.ad()
        input("Press enter to exit.")
    elif userInput == "ecce" or userInput == "Ecce":
        os.system("clear")
        LatinRef.ecce()
        input("Press enter to exit.")
    elif userInput == "magnus" or userInput == "Magnus":
        os.system("clear")
        LatinRef.magnus()
        input("Press enter to exit.")
    elif userInput == "parvus" or userInput == "Parvus":
        os.system("clear")
        LatinRef.parvus()
        input("Press enter to exit.")
    elif userInput == "ambulo" or userInput == "Ambulo":
        os.system("clear")
        LatinRef.ambulo()
        input("Press enter to exit.")
    elif userInput == "iratus" or userInput == "Iratus":
        os.system("clear")
        LatinRef.iratus()
        input("Press enter to exit.")
    elif userInput == "quis" or userInput == "Quis":
        os.system("clear")
        LatinRef.quis()
        input("Press enter to exit.")
    elif userInput == "quid" or userInput == "Quid":
        os.system("clear")
        LatinRef.quid()
        input("Press enter to exit.")
    elif userInput == "cur" or userInput == "Cur":
        os.system("clear")
        LatinRef.cur()
        input("Press enter to exit.")
    elif userInput == "ubi" or userInput == "Ubi":
        os.system("clear")
        LatinRef.ubi()
        input("Press enter to exit.")
    elif userInput == "sum" or userInput == "Ubi":
        os.system("clear")
        LatinRef.sum()
        input("Press enter to exit.")
    elif userInput == "eheu" or userInput == "Eheu":
        os.system("clear")
        LatinRef.eheu()
        input("Press enter to exit.")
    elif userInput == "pecunia" or userInput == "Pecunia":
        os.system("clear")
        LatinRef.pecunia()
        input("Press enter to exit.")
    elif userInput == "ego" or userInput == "Ego":
        os.system('clear')
        LatinRef.ego()
        input("Press enter to exit.")
    elif userInput == "tu" or userInput == "Tu":
        os.system('clear')
        LatinRef.tu()
        input("Press enter to exit.")
    elif userInput == "habeo" or userInput == "Habeo":
        os.system('clear')
        LatinRef.habeo()
        input("Press enter to exit.")
    elif userInput == "respondeo" or userInput == "Respondeo":
        os.system('clear')
        LatinRef.respondeo()
        input("Press enter to exit.")
    elif userInput == "venio" or userInput == "Venio":
        os.system('clear')
        LatinRef.venio()
        input("Press enter to exit.")
    elif userInput == "rideo" or userInput == "Rideo":
        os.system('clear')
        LatinRef.rideo()
        input("Press enter to exit.")
    elif userInput == "quod" or userInput == "Quod":
        os.system('clear')
        LatinRef.quod()
        input("Press enter to exit.")
    elif userInput == "ex" or userInput == "Ex":
        os.system('clear')
        LatinRef.ex()
        input("Press enter to exit.")
    elif userInput == "voco" or userInput == "Voco":
        os.system('clear')
        LatinRef.voco()
        input("Press enter to exit.")
    elif userInput == "clamo" or userInput == "Clamo":
        os.system('clear')
        LatinRef.clamo()
        input("Press enter to exit.")
    elif userInput == "specto" or userInput == "Specto":
        os.system('clear') 
        LatinRef.specto()
        input("Press enter to exit.")
    elif userInput == "taberna" or userInput == "Taberna":
        os.system('clear')
        LatinRef.taberna()
        input("Press enter to exit.")   
    elif userInput == "laboro" or userInput == "Laboro":
        os.system('clear')
        LatinRef.laboro()
        input("Press enter to exit.")
    elif userInput == "femina" or userInput == "Femina":
        os.system('clear')
        LatinRef.femina()
        input("Press enter to exit.")
    elif userInput == "vir" or userInput == "Vir":
        os.system('clear')
        LatinRef.vir()
        input("Press enter to exit.")
    elif userInput == "puer" or userInput == "Puer":
        os.system('clear')
        LatinRef.puer()
        input("Press enter to exit.")
    elif userInput == "puella" or userInput == "Puella":
        os.system('clear')
        LatinRef.puella()
        input("Press enter to exit.")
    elif userInput == "multus" or userInput == "Multus":
        os.system('clear')
        LatinRef.multus()
        input("Press enter to exit.")
    elif userInput == "urbs" or userInput == "Urbs":
        os.system('clear')
        LatinRef.multus()
        input("Press enter to exit.")
    elif userInput == "agricola" or userInput == "Agricola":
        os.system('clear')
        LatinRef.agricola()
        input("Press enter to exit.")
    elif userInput == "curro" or userInput == "Curro":
        os.system('clear')
        LatinRef.curro()
        input("Press enter to exit.")
    elif userInput == "hodie" or userInput == "Hodie":
        os.system('clear')
        LatinRef.hodie()
        input("Press enter to exit.")
    elif userInput == "iuvenis" or userInput == "Iuvenis":
        os.system('clear')
        LatinRef.iuvenis()
        input("Press enter to exit.")
    elif userInput == "meus" or userInput == "Meus":
        os.system('clear')
        LatinRef.meus()
        input("Press enter to exit.")
    elif userInput == "Senex" or userInput == "Senex":
        os.system('clear')
        LatinRef.senex()
    elif userInput == "sto" or userInput == "Sto":
        os.system('clear')
        LatinRef.sto()
        input("Press enter to exit.")
    elif userInput == "optimus" or userInput == "Optimus":
        os.system('clear')
        LatinRef.optimus()
        input("Press enter to exit.")
    elif userInput == "volo" or userInput == "Volo":
        os.system('clear')
        LatinRef.volo()
        input("Press enter to exit.")
    elif userInput == "fortis" or userInput == "Fortis":
        os.system('clear')
        LatinRef.fortis()
        input("Press enter to exit.")
        

    else:
        os.system("clear")
        print("Thats not a command.") ; sleep(1.5)

    clear = lambda: os.system('clear')
    clear()   
    return input('\nType in your command or any Latin word to review or learn. Enter your responce: ')

def words():
    wordList = ["salve" , "vale" , "et" , "est" , "in" , "sunt" , "non" , "insula" , "sed" , "oppidum"
                , "quoque" , "canis" , "coquus" , "filia" , "filius" , "hortus" , "mater" , "pater" , "servus" , "via" , "amicus" , "ancilla" , "cena" , "cibus"
                , "intro" , "saluto" , "porto" , "video" , "dominus" , "laetus" , "mercator" , "audio" , "dico" , "unus" , "duo" , "tres" , "quattuor" , "quinque"
                , "sex" , "septem" , "octo" , "novem" , "decem" , "ad" , "ecce" , "magnus" , "parvus" , "ambulo" , "iratus" , "quis" , "quid" , "cur" , "ubi" ,
                "sum" , "eheu" , "pecunia" , "ego" , "tu" , "habeo" , "respondeo" , "venio" , "rideo" , "quod" , "ex" , "voco" , "clamo" , "specto" , "taberna"
                , "laboro" , "clamor" , "femina" , "vir", "puer" , "puella" , "multus" , "urbs" , "agricola" , "curro" , "hodie" , "iuvenis" , "meus" , "senex" , "sto" ,
                "optimus" , "volo" , "fortis" , "emo" , "pulso" , "bonus" , "malus" , "festino" , "per" , "pugno" , "scribo" , "tuus" , "paro" , "cum" , "facio" ,
                "heri" , "ingens" , "nihil" , "omnis" , "vendo" , "navis" , "prope" , "rogo" , "terreo" , "inquit" , "tamen" , "eum" , "eam" , "duco" , "saepe" , "interficio" ,
                "habito" , "silva" , "statim" , "totus" , "pessimus" , "cupio" , "celeriter" , "do" , "iterum" , "pulcher" , "dies" , "fero", "homo" , "maneo" , "medius" , "mox" , "ostendo" , "trado" , "nomen" , "accipio" , "frater" , "soror" , "invenio" , "pax" , "bellum" , "nos" , "quam" , "semper" , "taceo" , "stultus" , "callidus" , "uxor" , "suus" , "solus" , "nuntio" , "magister" , "discipulus" , "doceo" , "subito" , "quaeso" , "capio" , "nunc" , "tum" , "credo" , "de" , "noster" , "placet" , "civis" , "lego"] 

    print("List:") ; sleep(2.0)
    print('\n'.join(map(str, wordList))) ; sleep(2.0)
    input("Press enter to exit.")
    clear = lambda: os.system('clear')
    clear()

def tutorial():
    print("Are you new to Latin?")
    new = input()
    if new == "yes" or new == "Yes":
        new = True
    else:
        new = False
    os.system('clear')
    print("Starting tutorial.") ; sleep(1.0)
    print("If you need help with the app itself just say: help or Help to see all of the avaliable commands you could do.") ; sleep(1.5)
    print("In order to quit you have to input: Quit") ; sleep(1.5)
    if new == True:
        print("If your new to latin the ''v'' is spelled as a ''w''. For example: Salve would be Salwe.") ; sleep(1.5)
        print("There is a present, imperfect and perfect tence.") ; sleep(1.5)
        print("The present tence is the what it means, your using the present tence like habeo which is have.") ; sleep(1.5)
        print("The imperfect tence works like the past tence, meaning that habeo in the imperfect tence would be habebam which means was having") ; sleep(1.5)
        print("The perfect tence works kind of similar to the past tence since instead of using the ''ba'' its using ''bui'' for the case for habui which means haved. But for most latin words it would be ''vi''") ; sleep(1.5)
        input("Press enter to exit.")
        clear = lambda: os.system('clear') 
        clear()
    else:
        input("Press enter to exit.")
        clear = lambda: os.system('clear')
        clear()















        
