#FUNCTIONS
def help():
    commands = ["list of Button functions", "help = Display of commands", "Word list = Shows all latin words that are defined.", "Enter = Enters the entry and searches for the word inputed in the search bar.", "Clear entry = Clears the search bar.", "Clear log = Clears the actions log."]
    return map(str, commands)
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
    return map(str, wordList) 