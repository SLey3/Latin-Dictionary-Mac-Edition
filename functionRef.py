# IMPORTS
from time import sleep
import os
import LatinRef

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

    
def userInstructions(userInput):
    if userInput == "help" or userInput == "Help":
        clear()
        help()
    elif userInput == "list" or userInput == "List":
        clear()
        words()
    elif userInput == "tutorial" or userInput == "Tutorial":
        clear()
        tutorial()
    elif userInput == "salve" or userInput == "Salve":
        clear()
        LatinRef.salve()
        input("Press enter to exit.")
    elif userInput == "vale" or userInput == "Vale":
        clear()
        LatinRef.vale()
        input("Press enter to exit.")
    elif userInput == "et" or userInput == "Et":
        clear()
        LatinRef.et()
        input("Press enter to exit.")
    elif userInput == "est" or userInput == "Est":
        clear()
        LatinRef.est()
        input("Press enter to exit.")
    elif userInput == "in" or userInput == "In":
        clear()
        LatinRef.In()
        input("Press enter to exit.")
    elif userInput == "sunt" or userInput == "Sunt":
        clear()
        LatinRef.sunt()
        input("Press enter to exit.")
    elif userInput == "non" or userInput == "Non":
        clear()
        LatinRef.non()
        input("Press enter to exit.")
    elif userInput == "insula" or userInput == "Insula":
        clear()
        LatinRef.insula()
        input("Press enter to exit.")
    elif userInput == "sed" or userInput == "Sed":
        clear()
        LatinRef.sed()
        input("Press enter to exit.")
    elif userInput == "oppidum" or userInput == "Oppidum":
        clear()
        LatinRef.oppidum()
        input("Press enter to exit.")
    elif userInput == "quoque" or userInput == "Quoque":
        clear()
        LatinRef.quoque()
        input("Press enter to exit.")
    elif userInput == "canis" or userInput == "Canis":
        clear()
        LatinRef.canis()
        input("Press enter to exit.")
    elif userInput == "coquus" or userInput == "Coquus":
        clear()
        LatinRef.coquus()
        input("Press enter to exit.")
    elif userInput == "filia" or userInput == "Filia":
        clear()
        LatinRef.filia()
        input("Press enter to exit.")
    elif userInput == "filius" or userInput == "Filius":
        clear()
        LatinRef.filius()
        input("Press enter to exit.")
    elif userInput == "hortus" or userInput == "Hortus":
        clear()
        LatinRef.hortus()
        input("Press enter to exit.")
    elif userInput == "mater" or userInput == "Mater":
        clear()
        LatinRef.mater()
        input("Press enter to exit.")
    elif userInput == "pater" or userInput == "Pater":
        clear()
        LatinRef.pater()
        input("Press enter to exit.")
    elif userInput == "servus" or userInput == "Servus":
        clear()
        LatinRef.servus()
        input("Press enter to exit.")
    elif userInput == "via" or userInput == "Via":
        clear()
        LatinRef.via()
        input("Press enter to exit.")
    elif userInput == "amicus" or userInput == "Amicus":
        clear()
        LatinRef.amicus()
        input("Press enter to exit.")
    elif userInput == "ancilla" or userInput == "Ancilla":
        clear()
        LatinRef.ancilla()
        input("Press enter to exit.")
    elif userInput == "cena" or userInput == "Cena":
        clear()
        LatinRef.cena()
        input("Press enter to exit.")
    elif userInput == "cibus" or userInput == "cibus":
        clear()
        LatinRef.cibus()
        input("Press enter to exit.")
    elif userInput == "intro" or userInput == "Intro":
        clear()
        LatinRef.intro()
        input("Press enter to exit.")
    elif userInput == "saluto" or userInput == "Saluto":
        clear()
        LatinRef.saluto()
        input("Press enter to exit.")
    elif userInput == "porto" or userInput == "Porto":
        clear()
        LatinRef.porto()
        input("Press enter to exit.")
    elif userInput == "video" or userInput == "Video":
        clear()
        LatinRef.video()
        input("Press enter to exit.")
    elif userInput == "dominus" or userInput == "Dominus":
        clear()
        LatinRef.dominus()
        input("Press enter to exit.")
    elif userInput == "laetus" or userInput == "Laetus":
        clear()
        LatinRef.laetus()
        input("Press enter to exit.")
    elif userInput == "mercator" or userInput == "Mercator":
        clear()
        LatinRef.mercator()
        input("Press enter to exit.")
    elif userInput == "audio" or userInput == "Audio":
        clear()
        LatinRef.audio()
        input("Press enter to exit.")
    elif userInput == "dico" or userInput == "Dico":
        clear()
        LatinRef.dico()
        input("Press enter to exit.")
    elif userInput == "unus" or userInput == "Unus":
        clear()
        LatinRef.unus()
        input("Press enter to exit.")
    elif userInput == "duo" or userInput == "Duo":
        clear()
        LatinRef.duo()
        input("Press enter to exit.")
    elif userInput == "tres" or userInput == "Tres":
        clear()
        LatinRef.tres()
        input("Press enter to exit.")
    elif userInput == "quattuor" or userInput == "Quattuor":
        clear()
        LatinRef.quattuor()
        input("Press enter to exit.")
    elif userInput == "quinque" or userInput == "Quinque":
        clear()
        LatinRef.quinque()
        input("Press enter to exit.")
    elif userInput == "sex" or userInput == "Sex":
        clear()
        LatinRef.sex()
        input("Press enter to exit.")
    elif userInput == "septem" or userInput == "Septem":
        clear()
        LatinRef.septem()
        input("Press enter to exit.")
    elif userInput == "octo" or userInput == "Octo":
        clear()
        LatinRef.octo()
        input("Press enter to exit.")
    elif userInput == "novem" or userInput == "Novem":
        clear()
        LatinRef.novem()
        input("Press enter to exit.")
    elif userInput == "decem" or userInput == "Decem":
        clear()
        LatinRef.decem()
        input("Press enter to exit.")
    elif userInput == "ad" or userInput == "Ad":
        clear()
        LatinRef.ad()
        input("Press enter to exit.")
    elif userInput == "ecce" or userInput == "Ecce":
        clear()
        LatinRef.ecce()
        input("Press enter to exit.")
    elif userInput == "magnus" or userInput == "Magnus":
        clear()
        LatinRef.magnus()
        input("Press enter to exit.")
    elif userInput == "parvus" or userInput == "Parvus":
        clear()
        LatinRef.parvus()
        input("Press enter to exit.")
    elif userInput == "ambulo" or userInput == "Ambulo":
        clear()
        LatinRef.ambulo()
        input("Press enter to exit.")
    elif userInput == "iratus" or userInput == "Iratus":
        clear()
        LatinRef.iratus()
        input("Press enter to exit.")
    elif userInput == "quis" or userInput == "Quis":
        clear()
        LatinRef.quis()
        input("Press enter to exit.")
    elif userInput == "quid" or userInput == "Quid":
        clear()
        LatinRef.quid()
        input("Press enter to exit.")
    elif userInput == "cur" or userInput == "Cur":
        clear()
        LatinRef.cur()
        input("Press enter to exit.")
    elif userInput == "ubi" or userInput == "Ubi":
        clear()
        LatinRef.ubi()
        input("Press enter to exit.")
    elif userInput == "sum" or userInput == "Ubi":
        clear()
        LatinRef.sum()
        input("Press enter to exit.")
    elif userInput == "eheu" or userInput == "Eheu":
        clear()
        LatinRef.eheu()
        input("Press enter to exit.")
    elif userInput == "pecunia" or userInput == "Pecunia":
        clear()
        LatinRef.pecunia()
        input("Press enter to exit.")
    elif userInput == "ego" or userInput == "Ego":
        clear()
        LatinRef.ego()
        input("Press enter to exit.")
    elif userInput == "tu" or userInput == "Tu":
        clear()
        LatinRef.tu()
        input("Press enter to exit.")
    elif userInput == "habeo" or userInput == "Habeo":
        clear()
        LatinRef.habeo()
        input("Press enter to exit.")
    elif userInput == "respondeo" or userInput == "Respondeo":
        clear()
        LatinRef.respondeo()
        input("Press enter to exit.")
    elif userInput == "venio" or userInput == "Venio":
        clear()
        LatinRef.venio()
        input("Press enter to exit.")
    elif userInput == "rideo" or userInput == "Rideo":
        clear()
        LatinRef.rideo()
        input("Press enter to exit.")
    elif userInput == "quod" or userInput == "Quod":
        clear()
        LatinRef.quod()
        input("Press enter to exit.")
    elif userInput == "ex" or userInput == "Ex":
        clear()
        LatinRef.ex()
        input("Press enter to exit.")
    elif userInput == "voco" or userInput == "Voco":
        clear()
        LatinRef.voco()
        input("Press enter to exit.")
    elif userInput == "clamo" or userInput == "Clamo":
        clear()
        LatinRef.clamo()
        input("Press enter to exit.")
    elif userInput == "specto" or userInput == "Specto":
        clear()
        LatinRef.specto()
        input("Press enter to exit.")
    elif userInput == "taberna" or userInput == "Taberna":
        clear()
        LatinRef.taberna()
        input("Press enter to exit.")
    elif userInput == "laboro" or userInput == "Laboro":
        clear()
        LatinRef.laboro()
        input("Press enter to exit.")
    elif userInput == "femina" or userInput == "Femina":
        clear()
        LatinRef.femina()
        input("Press enter to exit.")
    elif userInput == "vir" or userInput == "Vir":
        clear()
        LatinRef.vir()
        input("Press enter to exit.")
    elif userInput == "puer" or userInput == "Puer":
        clear()
        LatinRef.puer()
        input("Press enter to exit.")
    elif userInput == "puella" or userInput == "Puella":
        clear()
        LatinRef.puella()
        input("Press enter to exit.")
    elif userInput == "multus" or userInput == "Multus":
        clear()
        LatinRef.multus()
        input("Press enter to exit.")
    elif userInput == "urbs" or userInput == "Urbs":
        clear()
        LatinRef.multus()
        input("Press enter to exit.")
    elif userInput == "agricola" or userInput == "Agricola":
        clear()
        LatinRef.agricola()
        input("Press enter to exit.")
    elif userInput == "curro" or userInput == "Curro":
        clear()
        LatinRef.curro()
        input("Press enter to exit.")
    elif userInput == "hodie" or userInput == "Hodie":
        clear()
        LatinRef.hodie()
        input("Press enter to exit.")
    elif userInput == "iuvenis" or userInput == "Iuvenis":
        clear()
        LatinRef.iuvenis()
        input("Press enter to exit.")
    elif userInput == "meus" or userInput == "Meus":
        clear()
        LatinRef.meus()
        input("Press enter to exit.")
    elif userInput == "Senex" or userInput == "Senex":
        clear()
        LatinRef.senex()
    elif userInput == "sto" or userInput == "Sto":
        clear()
        LatinRef.sto()
        input("Press enter to exit.")
    elif userInput == "optimus" or userInput == "Optimus":
        clear()
        LatinRef.optimus()
        input("Press enter to exit.")
    elif userInput == "volo" or userInput == "Volo":
        clear()
        LatinRef.volo()
        input("Press enter to exit.")
    elif userInput == "fortis" or userInput == "Fortis":
        clear()
        LatinRef.fortis()
        input("Press enter to exit.")
    elif userInput == "emo":
        clear()
        LatinRef.emo()
        input("Press enter to exit.")
    elif userInput == "pulso":
        clear()
        LatinRef.pulso()
        input("Press enter to exit.")
    elif userInput == "bonus":
        clear()
        LatinRef.bonus()
        input("Press enter to exit.")
    elif userInput == "malus":
        clear()
        LatinRef.malus()
        input("Press enter to exit.")
    elif userInput == "festino":
        clear()
        LatinRef.festino()
        input("Press enter to exit.")
    elif userInput == "per":
        clear()
        LatinRef.per()
        input("Press enter to exit.")
    elif userInput == "pugno":
        clear()
        LatinRef.pugno()
        input("Press enter to exit.")
    elif userInput == "scribo":
        clear()
        LatinRef.scribo()
        input("Press enter to exit.")
    elif userInput == "tuus":
        clear()
        LatinRef.tuus()
        input("Press enter to exit.")
    elif userInput == "paro":
        clear()
        LatinRef.paro()
        input("Press enter to exit.")
    elif userInput == "cum":
        clear()
        LatinRef.cum()
        input("Press enter to exit.")
    elif userInput == "facio":
        clear()
        LatinRef.facio()
        input("Press enter to exit.")
    elif userInput == "heri":
        clear()
        LatinRef.heri()
        input("Press enter to exit.")
    elif userInput == "ingens":
        clear()
        LatinRef.ingens()
        input("Press enter to exit.")
    elif userInput == "nihil":
        clear()
        LatinRef.nihil()
        input("Press enter to exit.")
    elif userInput == "omnis":
        clear()
        LatinRef.omnis()
        input("Press enter to exit.")
    elif userInput == "vendo":
        clear()
        LatinRef.vendo()
        input("Press enter to exit.")
    elif userInput == "navis":
        clear()
        LatinRef.navis()
        input("Press enter to exit.")
    elif userInput == "prope":
        clear()
        LatinRef.prope()
        input("Press enter to exit.")
    elif userInput == "rogo":
        clear()
        LatinRef.rogo()
        input("Press enter to exit.")
    elif userInput == "terreo":
        clear()
        LatinRef.terreo()
        input("Press enter to exit.")
    elif userInput == "inquit":
        clear()
        LatinRef.inquit()
        input("Press enter to exit.")
    elif userInput == "tamen":
        clear()
        LatinRef.tamen()
        input("Press enter to exit.")
    elif userInput == "eum":
        clear()
        LatinRef.eum()
        input("Press enter to exit.")
    elif userInput == "eam":
        clear()
        LatinRef.eam()
        input("Press enter to exit.")
    elif userInput == "duco":
        clear()
        LatinRef.duco()
        input("Press enter to exit.")
    elif userInput == "saepe":
        clear()
        LatinRef.saepe()
        input("Press enter to exit.")
    elif userInput == "interficio":
        clear()
        LatinRef.interficio()
        input("Press enter to exit.")
    elif userInput == "habito":
        clear()
        LatinRef.habito()
        input("Press enter to exit.")
    elif userInput == "silva":
        clear()
        LatinRef.silva()
        input("Press enter to exit.")
    elif userInput == "statim":
        clear()
        LatinRef.statim()
        input("Press enter to exit.")
    elif userInput == "totus":
        clear()
        LatinRef.totus()
        input("Press enter to exit.")
    elif userInput == "pessimus":
        clear()
        LatinRef.pessimus()
        input("Press enter to exit.")
    elif userInput == "cupio":
        clear()
        LatinRef.cupio()
        input("Press enter to exit.")
    elif userInput == "celeriter":
        clear()
        LatinRef.celeriter()
        input("Press enter to exit.")
    elif userInput == "do":
        clear()
        LatinRef.do()
        input("Press enter to exit.")
    elif userInput == "iterum":
        clear()
        LatinRef.iterum()
        input("Press enter to exit.")
    elif userInput == "pulcher":
        clear()
        LatinRef.pulcher()
        input("Press enter to exit.")
    elif userInput == "dies":
        clear()
        LatinRef.dies()
        input("Press enter to exit.")
    elif userInput == "fero":
        clear()
        LatinRef.fero()
        input("Press enter to exit.")
    elif userInput == "homo":
        clear()
        LatinRef.homo()
        input("Press enter to exit.")
    elif userInput == "maneo":
        clear()
        LatinRef.maneo()
        input("Press enter to exit.")
    elif userInput == "medius":
        clear()
        LatinRef.medius()
        input("Press enter to exit.")
    elif userInput == "mox":
        clear()
        LatinRef.mox()
        input("Press enter to exit.")
    elif userInput == "ostendo":
        clear()
        LatinRef.ostendo()
        input("Press enter to exit.")
    elif userInput == "trado":
        clear()
        LatinRef.trado()
        input("Press enter to exit.")
    elif userInput == "nomen":
        clear()
        LatinRef.nomen()
        input("Press enter to exit.")
    elif userInput == "accipio":
        clear()
        LatinRef.accipio()
        input("Press enter to exit.")
    elif userInput == "frater":
        clear()
        LatinRef.frater()
        input("Press enter to exit.")
    elif userInput == "soror":
        clear()
        LatinRef.soror()
        input("Press enter to exit.")
    elif userInput == "invenio":
        clear()
        LatinRef.invenio()
        input("Press enter to exit.")
    elif userInput == "pax":
        clear()
        LatinRef.pax()
        input("Press enter to exit.")
    elif userInput == "bellum":
        clear()
        LatinRef.bellum()
        input("Press enter to exit.")
    elif userInput == "nos":
        clear()
        LatinRef.nos()
        input("Press enter to exit.")
    elif userInput == "quam":
        clear()
        LatinRef.quam()
        input("Press enter to exit.")
    elif userInput == "semper":
        clear()
        LatinRef.semper()
        input("Press enter to exit.")
    elif userInput == "taceo":
        clear()
        LatinRef.taceo()
        input("Press enter to exit.")
    elif userInput == "vos":
        clear()
        LatinRef.vos()
        input("Press enter to exit.")
    elif userInput == "stultus":
        clear()
        LatinRef.stultus()
        input("Press enter to exit.")
    elif userInput == "callidus":
        clear()
        LatinRef.callidus()
        input("Press enter to exit.")
    elif userInput == "uxor":
        clear()
        LatinRef.uxor()
        input("Press enter to exit.")
    elif userInput == "suus":
        clear()
        LatinRef.suus()
        input("Press enter to exit.")
    elif userInput == "solus":
        clear()
        LatinRef.solus()
        input("Press enter to exit.")
    elif userInput == "nuntio":
        clear()
        LatinRef.nuntio()
        input("Press enter to exit.")
    elif userInput == "magister":
        clear()
        LatinRef.magister()
        input("Press enter to exit.")
    elif userInput == "discipulus":
        clear()
        LatinRef.discipulus()
        input("Press enter to exit.")
    elif userInput == "doceo":
        clear()
        LatinRef.doceo()
        input("Press enter to exit.")
    elif userInput == "num":
        clear()
        LatinRef.num()
        input("Press enter to exit.")
    elif userInput == "subito":
        clear()
        LatinRef.subito()
        input("Press enter to exit.")
    elif userInput == "gratias":
        clear()
        LatinRef.gratias()
        input("Press enter to exit.")
    elif userInput == "quaeso":
        clear()
        LatinRef.quaeso()
        input("Press enter to exit.")
    elif userInput == "capio":
        clear()
        LatinRef.capio()
        input("Press enter to exit.")
    elif userInput == "nunc":
        clear()
        LatinRef.nunc()
        input("Press enter to exit.")
    elif userInput == "tum":
        clear()
        LatinRef.tum()
        input("Press enter to exit.")
    elif userInput == "mihi":
        clear()
        LatinRef.mihi()
        input("Press enter to exit.")
    elif userInput == "tibi":
        clear()
        LatinRef.tibi()
        input("Press enter to exit.")
    elif userInput == "credo":
        clear()
        LatinRef.credo()
        input("Press enter to exit.")
    elif userInput == "de":
        clear()
        LatinRef.de()
        input("Press enter to exit.")
    elif userInput == "noster":
        clear()
        LatinRef.noster()
        input("Press enter to exit.")
    elif userInput == "placet":
        clear()
        LatinRef.placet()
        input("Press enter to exit.")
    elif userInput == "civis":
        clear()
        LatinRef.civis()
        input("Press enter to exit.")
    elif userInput == "lego":
        clear()
        LatinRef.lego()
        input("Press enter to exit.")
    elif userInput == "iam":
        clear()
        LatinRef.iam()
        input("Press enter to exit.")
    elif userInput == "terra":
        clear()
        LatinRef.terra()
        input("Press enter to exit.")
    elif userInput == "custodio":
        clear()
        LatinRef.custodio()
        input("Press enter to exit.")
    elif userInput == "fortiter":
        clear()
        LatinRef.fortiter()
        input("Press enter to exit.")
    elif userInput == "fugio":
        clear()
        LatinRef.fugio()
        input("Press enter to exit.")
    elif userInput == "igitur":
        clear()
        LatinRef.igitur()
        input("Press enter to exit.")
    elif userInput == "tristis":
        clear()
        LatinRef.tristis()
        input("Press enter to exit.")
    elif userInput == "iubeo":
        clear()
        LatinRef.iubeo()
        input("Press enter to exit.")
    elif userInput == "deleo":
        clear()
        LatinRef.deleo()
        input("Press enter to exit.")
    elif userInput == "displodo":
        clear()
        LatinRef.displodo()
        input("Press enter to exit.")
    elif userInput == "aeger":
        clear()
        LatinRef.aeger()
        input("Press enter to exit.")
    elif userInput == "alter":
        clear()
        LatinRef.alter()
        input("Press enter to exit.")
    elif userInput == "fessus":
        clear()
        LatinRef.fessus()
        input("Press enter to exit.")
    elif userInput == "ignavus":
        clear()
        LatinRef.ignavus()
        input("Press enter to exit.")
    elif userInput == "nolo":
        clear()
        LatinRef.nolo()
        input("Press enter to exit.")
    elif userInput == "ne" or userInput == "-ne":
        clear()
        LatinRef.ne()
        input("Press enter to exit.")
    elif userInput == "traho":
        clear()
        LatinRef.traho()
        input("Press enter to exit.")
    elif userInput == "hic":
        clear()
        LatinRef.hic()
        input("Press enter to exit.")
    elif userInput == "ille":
        clear()
        LatinRef.ille()
        input("Press enter to exit.")
    elif userInput == "possum":
        clear()
        LatinRef.possum()
        input("Press enter to exit.")
    elif userInput == "que" or userInput == "-que":
        clear()
        LatinRef.que()
        input("Press enter to exit.")
    elif userInput == "ceteri":
        clear()
        LatinRef.ceteri()
        input("Press enter to exit.")
    elif userInput == "novus":
        clear()
        LatinRef.novus()
        input("Press enter to exit.")
    elif userInput == "se":
        clear()
        LatinRef.se()
        input("Press enter to exit.")
    elif userInput == "vita":
        clear()
        LatinRef.vita()
        input("Press enter to exit.")
    elif userInput == "attonitus":
        clear()
        LatinRef.attonitus()
        input("Press enter to exit.")
    elif userInput == "facilis":
        clear()
        LatinRef.facilis()
        input("Press enter to exit.")
    else:
        clear()
        print("Thats not a command.") ; sleep(1.5)
    clear()   
    return str.lower(input('\nType in your command or any Latin word to review or learn. Enter your responce: '))

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
                 , "sollicitus" , "mons" , "mirabilis" , "templum" , "mitto" , "sentio" , "tandem" , "iam" , "terra" , "custodio" , "fortiter" , "fugio" , "igitur" , "tristis" , "iubeo" , "deleo" , "displodo" , "aeger" , "alter" , "fessus" , "ignavus" , "nolo" , "-ne" , "traho" , "hic" , "ille" , "possum" , "-que" , "ceteri" , "novus" , "se" , "vita" , "attonitus" , "facilis"] 

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