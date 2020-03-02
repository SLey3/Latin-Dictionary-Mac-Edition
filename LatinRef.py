# INITILIZATION
class Initial:
    def __init__(self, arg1, arg2, arg3, arg4, arg5):
        self.definition = arg1
        self.other_meanings = arg2
        self.present = arg3
        self.imperfect = arg4
        self.perfect = arg5

    def __str__(self):
        return  str(self.__class__) + '\n' + '\n'.join((str(item) + ' = ' + str(self.__dict__[item]) for item in sorted(self.__dict__)))
    

# DEFINITIONS
def salve():
    dictator = Initial("hello\n" ,"salvete = hello (plural)\n" , None , None, None)
    print(dictator)
    
def vale():
    dictator = Initial("good-bye\n" ,"valete = good-bye (plural)\n" , None , None , None)
    print(dictator)

def et():
    dictator = Initial("and\n" , None , None , None , None)
    print(dictator)

def est():
    dictator = Initial("is\n" , None ,"I = sum , you (singular) = es , he/she = est , we = sumus , you (plural) = estis , they = sunt\n" ,"I = eram, you(singular) = eras, he/she = erat, we = eramus, you(plural) = eratis, they = erant\n" , None)
    print(dictator)

def In():
    dictator = Initial("in\n" ,"on\n" , None , None , None)
    print(dictator)

def sunt():
    dictator = Initial("are\n" ,"there are / they are\n" ,"I = sum, you(singular) = es, he/she = est, we = sumus, you(plural) = estis, they = sunt\n" ,"I = eram, you(singular) = eras, he/she = erat, we = eramus, you(plural) = eratis, they = erant\n", None)
    print(dictator)
    
def non():
    dictator = Initial("not\n" ,"non = no\n" , None , None , None)
    print(dictator)
    
def insula():
    dictator = Initial("island\n" , None , None , None , None)
    print(dictator)
    
def sed():
    dictator = Initial("but\n" , None , None , None , None)
    print(dictator)
    
def oppidum():
    dictator = Initial("town\n" , None , None , None , None)
    print(dictator)

def quoque():
    dictator = Initial("also\n" , "too\n" , None , None , None)
    print(dictator)

def canis():
    dictator = Initial("dog\n" ,"Nominative = canis(singular) / canes(plural) , Dative = cani(singular) / canibus(plural) , Accusative = canem(singular) / canes(plural)\n" , None , None , None)
    print(dictator)

def coquus():
    dictator = Initial("cook\n" ,"Nominative = coquues(singular) / coqui(plural) , Dative = coquo(singular) / coquis(plural) , Accusative = coquum(singular) / coquos(plural)\n" , None , None , None)
    print(dictator)

def filia():
    dictator = Initial("daughter\n" ,"Nominative = filia(singular) / filiae(plural) , Dative = filiae(singular) / filiis(plural) , Accusative = filiam(singular) / filias(plural)\n" , None , None , None)
    print(dictator)

def filius():
    dictator = Initial("son\n" ,"Nominative = filius(singular) / filii(plural) , Dative = filio(singular) / filiis(plural) , Accusative = filium(singular) / filios(plural)\n" , None , None , None)
    print(dictator)
    
def hortus():
    dictator = Initial("garden\n" ,"Nominative = hortus(singular) / horti(plural) , Dative = horto(singular) / hortis(plural) , Accusative = hortum(singular) / hortos(plural)\n" , None , None , None)
    print(dictator)
    
def mater():
    dictator = Initial("mother\n" ,"Nominative = mater(singular) / matres(plural) , Dative = matri(singular) / matribus(plural) , Accusative = matrem(singular) / matres(plural)\n" , None , None , None)
    print(dictator)

def pater():
    dictator = Initial("father\n" ,"Nominative = pater(singular) / patres(plural) , Dative = patri(singular) / patribus(plural) , Accusative = patrem(singular) / patres(plural)\n" , None , None , None)
    print(dictator)

def servus():
    dictator = Initial("servant\n" ,"{servus = slave} Nominative = servus(singular) / servi(plural) , Dative = servo(singular) / servis(plural) , Accusative = servum(singular) / servos(plural)\n" , None , None , None)
    print(dictator)

def via():
    dictator = Initial("road\n" ,"{street / way} Nominative = via(singular) / viae(plural) , Dative = viae(singular) / viis(plural) , Accusative = viam(singular) / vias(plural)\n" , None , None , None)
    print(dictator)

def amicus():
    dictator = Initial("friend\n" ,"Nominative = amicus(singular) / amici(plural) , Dative = amico(singular) / amicis(plural) , Accusative = amicum(singular) / amicos(plural)\n" , None , None , None)
    print(dictator)

def ancilla():
    dictator = Initial("female slave\n" ,"Nominative = ancilla(singular) / ancillae , Dative = ancillae(singular) / ancillis(plural) , Accusative = anicillam(singular) / ancillas(plural)\n" , None , None , None)
    print(dictator)

def cena():
    dictator = Initial("dinner\n" ,"Nominative = cena(singular) / cenae(plural) , Dative = cenae(singular) / cenis(plural) , Accusative = cenam(singular) / cenas(plural)\n" , None , None , None)
    print(dictator)

def cibus():
    dictator = Initial("food\n" ,"Nominative = cibus(singular) / cibi(plural) , Dative = cibo(singular) / cibis(plural) , Accusative = cibum(singular) / cibos(plural)\n" , None , None , None)
    print(dictator)

def intro():
    dictator = Initial("enters\n" , None ,"I = intro , you(singular) = intras , he/she = intrat , we = intramus , you(plural) = intratis , they = intrant\n" ,"I = intrabam , you(singular) = intrabas , he/she = intrabat , we = intrabamus , you(plural) = intrabatis , they = intrabant\n" , "I = intravi , you(singular) = intravisti , he/she = intravit , we = intravimus , you(plural) = intravistis , they = intraverunt\n")
    print(dictator)

def saluto():
    dictator = Initial("greet\n" , None ,"I = saluto , you(singular) = salutas , he/she = salutat , we = salutamus , you(plural) = salutamus , you(plural) = salutatis , they = salutant\n" ,"I = salutabam , you(singular) = salutabas , he/she = salutabat , we = salutabamus , you(plural) = salutabatis , they = salutabant\n" ,"I = salutavi , you(singular) = salutavisti , he/she = salutavit , we = salutavimus , you(plural) = salutavistis , they = salutaverunt\n")
    print(dictator)

def porto():
    dictator = Initial("carry\n" , None ,"I = porto , you(singular) = portas , he/she = portat , we = portamus , you(plural) = portatis , they = portant\n" ,"I = portabam , you(singular) = portabas , he/she = portabat , we = portabamus , you(plural) = portabatis , they = portabant\n" , "I = portavi , you(singular) = portavisti , he/she = portavit , we = portavimus , you(plural) = portavistis , they = portaverunt\n")
    print(dictator)

def video():
    dictator = Initial("see\n" , None ,"I = video , you(singular) = vides , he/she = videt , we = videmus , you(plural) , vident\n" ,"I = videbam , you(singular) = videbas , he/she = videbat , we = videbamus , you(plural) = videbatis , they = videbant\n" ,"I = vidi , you(singular) = vidisti , he/she = vidit , we = vidimus , you(plural) = vidistis , they = viderunt\n")
    print(dictator)

def dominus():
    dictator = Initial("master\n" ,"{dominus = lord} Nominative = dominus(singular) / domini(plural) , Dative = domino(singular) / dominis(plural) , Accusative = dominum(singular) / dominos(plural)\n" , None , None , None)
    print(dictator)

def laetus():
    dictator = Initial("happy\n" , None , None , None , None)
    print(dictator)

def mercator():
    dictator = Initial("merchant\n" ,"Nominative = mercator(singular) / mercatores(plural) , Dative = mercatori(singular) / mercatoribus(plural) , Accusative = mercatorem(singular) / mercatores(plural)\n" , None , None , None)
    print(dictator)
    
def audio():
    dictator = Initial("hear\n" , None , "I = audio , you(singular) = audis , he/she = audit , we = audimus , you(plural) = auditis , they = audiunt\n" ,"I = audiebam , you(singular) = audiebas , he/she = audiebat , we = audiebamus , you(plural) = audiebatis , they = audiebant\n" ,"I = audivi , you(singular) = audvisiti , he/she = audivit , we = audivimus , you(plural) = audivistis , they = audiverunt\n")
    print(dictator)

def dico():
    dictator = Initial("say\n" , None ,"I = dico , you(singular) = dicis , he/she = dicit , we = dicimus , you(plural) = dicitis , they = dicunt\n" , "I = dicebam , you(singular) = dicebas , he/she = dicebat , we = dicebamus , you(plural) = dicebatis , they = dicebant\n" ,"I = dixi , you(singular) = dixisti , he/she = dixit , we = diximus , you(plural) = dixistis , they = dixerunt\n")
    print(dictator)

def unus():
    dictator = Initial("one\n" , None , None , None , None)
    print(dictator)

def duo():
    dictator = Initial("two\n" , None , None , None , None)
    print(dictator)

def tres():
    dictator = Initial("three\n" , None , None , None , None)
    print(dictator)

def quattuor():
    dictator = Initial("four\n" , None , None , None , None)
    print(dictator)

def quinque():
    dictator = Initial("five\n" , None , None , None , None)
    print(dictator)

def sex():
    dictator = Initial("six\n" , None , None , None , None)
    print(dictator)

def septem():
    dictator = Initial("seven\n" , None , None , None , None)
    print(dictator)

def octo():
    dictator = Initial("eight\n" , None , None , None , None)
    print(dictator)

def novem():
    dictator = Initial("nine\n" , None , None , None , None)
    print(dictator)

def decem():
    dictator = Initial("ten\n" , None , None , None , None)
    print(dictator)
    
def ad():
    dictator = Initial("to\n" ,"towards / at\n" , None , None , None)
    print(dictator)

def ecce():
    dictator = Initial("look\n" ,"behold\n" , None , None , None , None)
    print(dictator)
    
def magnus():
    dictator = Initial("big\n" ,"large / great\n" , None , None , None)
    print(dictator)

def parvus():
    dictator = Initial("small\n" ,"little\n" , None , None , None)
    print(dictator)

def ambulo():
    dictator = Initial("walk\n" , None , "I = ambulo , you(singular) = ambulas , he/she = ambulat , we = ambulamus , you(plural) = ambulatis , ambulant\n" ,"I = ambulabam , you(singular) = ambulabas , he/she = ambulabat , we = ambulabamus , you(plural) = ambulabatis , they = ambulabant\n" ,"I = ambulavi , you(singular) = ambulavisti , he/she = ambulavit , we = ambulavimus , you(plural) = ambulavistis , they = ambulaverunt\n")
    print(dictator)

def iratus():
    dictator = Initial("angry\n" , None , None , None , None)
    print(dictator)

def quis():
    dictator = Initial("who\n" , None , None , None , None)
    print(dictator)

def quid():
    dictator = Initial("what\n" , None , None , None , None)
    print(dictator)
    
def cur():
    dictator = Initial("why\n" , None , None , None , None)
    print(dictator)

def ubi():
    dictator = Initial("where\n" ,"when\n" , None , None , None)
    print(dictator)

def sum():
    dictator =  Initial("I am\n" , None ,"I = sum , you(singular) = es , he/she = est , we = sumus , you(plural) = estis , they = sunt\n" ,"I = eram , you(singular) = eras , he/she = erat , we = eramus , you(plural) = eratis , they = erant\n" , None)
    print(dictator)

def eheu():
    dictator = Initial("oh no\n" ,"oh dear / alas\n" , None , None , None)
    print(dictator)

def pecunia():
    dictator = Initial("money\n" ,"Nominative = pecunia(singular) / pecuniae(plural) , dative = pecuniae(singular) / pecuniis(plural) , accusative = pecuniam(singular) , pecunias(plural)\n" , None , None , None)
    print(dictator)

def ego():
    dictator = Initial("I\n" , None , None , None , None)
    print(dictator)

def tu():
    dictator = Initial("you\n" , None , None , None , None)
    print(dictator)

def habeo():
    dictator = Initial("have\n" ,"has\n" ,"I = habeo , you(singular) = habes , he/she = habet , we = habemus , you(plural) = habetis , they = habent\n" ,"I = habebam , you(singular) = habebas , he/she = habebat , we = habebamus , you(plural) = habebatis , they = habebant\n" ,"I = habui , you(singular) = habuisti , he/she = habuit , we = habuimus , you(plural) = habuistis , they = habuerunt\n")
    print(dictator)

def respondeo():
    dictator = Initial("reply\n" ,"answer / respond\n" ,"I = respondeo , you(singular) = respondes , he/she = respondet, we = respondemus , you(plural) = respondetis , they = respondent\n" ,"I = respondebam , you(singular) = respondebas , he/she = respondebat , we = respondebamus , you(plural) = respondebatis , they = respondebant\n" ,"I = respondi , you(singular) = respondisti , he/she = respondit , we = respondimus , you(plural) = respondistis , they = responderunt\n")
    print(dictator)

def venio():
    dictator = Initial("come\n" , None ,"I = venio , you(singular) = venis , he/she = venit , we = venimus , you(plural) = venitis , they = veniunt\n" ,"I = veniebam , you(singular) = veniebas , he/she = veniebat , we = veniebamus , you(singular) = vaniebatis , they = veniebant\n")
    
def rideo():
    dictator = Initial("laugh\n" ,"smile" ,"I = rideo , you(singular) = rides , he/she = ridet , we = ridemus , you(plural) = ridetis , they = rident\n" ,"I = ridebam , you(singular) = ridebas , he/she = ridebat , we = ridebamus , you(plural) = ridebatis , they = ridebant\n" ,"I = risi , you(singular) = risisti , he/she = risit , we = risimus , you(plural) = risistis , they = riserunt\n")
    print(dictator)
    
def quod():
    dictator = Initial("because\n" , None , None , None , None)
    print(dictator)
    
def ex():
    dictator = Initial("out of\n" ,"{ex = e} out from / from\n" , None , None , None)
    print(dictator)
    
def voco():
    dictator = Initial("call\n" ,"summon\n" ,"I = voco , you(singular) = vocas , he/she = vocat , we = vocamus , you(plural) = vocatis , they = vocant\n" ,"I = vocabam , you(singular) = vocabas , he/she = vocabat , we = vocabamus you(plural) = vocabatis , they = vocabant\n" ,"I = vocavi , you(singular) = vocavisti , he/she = vocavit , we = vocavimus , you(plural) = vocavistis , they = vocaverunt\n")
    print(dictator)
  
def clamo():
      dictator = Initial("shout\n" ,"{yell / uproar} Nominative = clamor(singular) / clamores(plural) , Dative = clamori(singular) / clamoribus(plural) , Accusative = clamorem(singular) / clamores(plural)\n" , None , None , None)
      print(dictator)
      
def specto():
    dictator = Initial("look at\n" ,"looks at / watches\n" ,"I = specto , you(singular) = spectas , he/she = spectat , we = spectamus , you(plural) = spectatis , they = spectant\n" ,"I = spectabam , you(singular) = spectabas , he/she = spectabat , we = spectabamus , you(plural) = spectabatis , they = spectabant\n" ,"I = spectavi , you(singular) = spectavisti , he/she = spectavit , we = spectavimus , you(plural) = spectavistis , they = spectaverunt\n")
    print(dictator)
    
def taberna():
    dictator = Initial("shop\n" ,"{store / inn} Nominative = taberna(plural) / tabernae(plural) , Dative = tabernae(singular) / tabernis(plural) , Accusative = tabernam(singular) / tabernas(dative)\n" , None , None , None)
    print(dictator)
    
def laboro():
    dictator = Initial("work\n" , None ,"I = laboro , you(singular) = laboras , he/she = laborat , we = laboramus , you(plural) = laboratis , they = laborant\n" ,"I = laborabam , you(singular) = laborabas , he/she = laborabat , we = laborabamus , you(plural) = laborabatis , they = laborabant\n" ,"I = laboravi , you(singular) = laboravisti , he/she = laboravit , we = laboravimus , you(plural) = laboravistis , they = laboraverunt\n")
    print(dictator)

def femina():
    dictator = Initial("woman\n" ,"Nominative = femina(singular) / feminae(plural) , Dative = feminae(singular) / feminis(plural) , Accusative = Feminam(singular) / feminas(plural)\n" , None , None , None)
    print(dictator)

def vir():
    dictator = Initial("man\n" ,"Accusative = vir(singular) / viri(plural) , Dative = viro(singular) / viris(plural) , Accusative = virum(singular) / viros(plural)\n" , None , None , None)
    print(dictator)  

def puer():
    dictator = Initial("boy\n" ,"Accusative = puer(singular) / puri(plural) , Dative = puero(singular) / pueris(plural) , Accusative = puerum(singular) / pueros(plural)\n" , None , None , None)
    print(dictator) 

def puella():
    dictator = Initial("girl\n" ,"Nominative = puella(singular) / puellae(plural) , Dative = puellae(singular) / puells(plural) , Accusative = puellam(singular) / puellas(plural)\n" , None , None , None)
    print(dictator)
    
def multus():
    dictator = Initial("many\n" ,"much\n" , None , None , None)
    print(dictator)
    
def urbs():
    dictator = Initial("city\n" ,"Nominative = urbs(singular) / urbes(plural) , Dative = urbi(singular) / urbibus(plural) , Accusative = urbem(singular) / urbes(plural)\n" , None , None , None)
    print(dictator)
   
def agricola():
    dictator = Initial("farmer\n" ,"Nominative = agricola(singular) / agricolae(plural) , Dative = agricolae(singular) / agricolis(plural) , Accusative = agricolam(singular) / agricolas(plural)\n" , None , None , None)
    print(dictator)
    
def curro():
    dictator = Initial("run\n" , None ,"I = curro , you(singular) = curris , he/she = currit , we = currimus , you(plural) = curritis , they = currunt\n" ,"I = currebam , you(singular) = currebas , he/she = currebat , we = currebamus , you(singualar) = currebatis, they = currebant\n" ,"I = cucurri , you(singular) = cucurristi , he/she = cucurrit , we = cucurrimus , you(singular) = cucurristis , they = cucurrerunt\n")
    print(dictator)
    
def hodie():
    dictator = Initial("today\n" , None , None , None , None)
    print(dictator)
    
def iuvenis():
    dictator = Initial("youth\n" ,"{young man} Nominative = iuvenis(singular) / iuvenes(plural) , Dative = iuveni(singular) / iuvenibus(plural) , Accusative = iuvenem(singular) / iuvenes(plural)\n" , None , None , None)
    print(dictator)
    
def meus():
    dictator = Initial("my\n" ,"mine\n" , None , None , None)
    print(dictator)
    
def senex():
    dictator = Initial("old man\n" ,"Nominative = senx(singular) / senes(plural), Dative = seni(plural) / senibus(plural) , Accusative = senem(singular) / senes(plural)\n" , None , None , None)
    print(dictator)
    
def sto():
    dictator = Initial("stand\n" , None ,"I = sto , you(singular) = stas , he/she = stat , we = stamus , you(plural) = statis , they = stant\n" ,"I = stabam , you(singular) = stabas , he/she = stabat , we = stabamus , you(plural) = stabatis , they = stabant\n" ,"I = seti , you(singular) = stetisti , he/she = stetit , we = stetimus , you(plural) = stetistis , they = steterunt\n")
    print(dictator)
    
def optimus():
    dictator = Initial("best\n" ,"excellent, very good\n" , None , None , None)
    print(dictator)
    
def volo():
    dictator = Initial("want\n" , None ,"I = volo , you(singular) = vis , he/she = vult , we = volumus , you(plural) = vultis , they = volunt\n" ,"I = volebam, you(singular) = volebas , he/she = volebat , we = volebamus , you(plural) = volebatis , they = volebant\n" ,"I = volui , you(singular) = voluisti , he/she = voluit , we = voluimus , you(singular) = voluistis , they = voluerunt\n")
    print(dictator)
    
def fortis():
    dictator = Initial("strong\n" ,"brave\n" , None , None , None)
    print(dictator)
    
def emo():
    dictator = Initial("buy\n", None ,"I = emo , you(sinuglar) = emis , he/she = we = emimus , you(plural) = emitis , they = emunt\n" ,"I = emebam , you(singualar) = emebas , he/she = emebat , we = emebamus , you(plural) = emebatis , they = emebant\n" ,"I = emi , you(singular) = emisti , he/she = emit , we = emimus , you(plural) = emistis , they = emeverunt\n")
    print(dictator)
    
def pulso():
    dictator = Initial("hit\n" ,"punch / strike / knocks at\n" ,"I = pulso , you(singular) = pulsas , he/she = pulsat , we = pulsamus , you(plural) = pulsatis , they = pulsant\n" ,"I = pulsabam , you(singular) = pulsabas , he/she = pulsabat , we = pulsabamus , you(singular) = pulsabatis , they = pulsabant\n" ,"I = pulsavi , you(singular) = pulsavisti , he/she = pulsavit , we = pulsavimus , you(plural) = pulsavistis , they = pulsaverunt\n")
    print(dictator)
    
def bonus():
    dictator = Initial("good\n" , None , None , None , None)
    print(dictator)
    
def malus():
    dictator = Initial("bad\n" ,"evil\n" , None , None , None)
    print(dictator)
    
def festino():
    dictator = Initial("hurry\n" , None ,"I = festino , you(singular) = festinas , he/she = festinat , we = festinamus , you(plural) = festinatis , they = festinant\n" ,"I = festinabam , you(singular) = festinabas , he/she = festinabat , we = festinabamus , you(plural) = festinabatis , they = festinabant\n" ,"I = festinavi , you(singular) = festinavisti , he/she = festinavit , we = festinavimus , you(plural) =  festinavistis , they = festinaverunt\n")
    print(dictator)

def per():
    dictator = Initial("through\n" , None , None , None , None)
    print(dictator)

def pugno():
    dictator = Initial("fight\n" , None ,"I = pugno , you(singular) = pugnas , he/she = pugnat , we = pugnamus , you(plural) = pugnatis , they = pugnant\n" ,"I = pugnabam , you(singular) = pugnabas , he/she = pugnabat , we = pugnabamus , you(plural) = pugnabatis , they = pugnabant\n" ,"I = pugnavi , you(singular) = pugnavisti , he/she = pugnavit , we = pugnavimus , you(plural) = pugnavistis , they = pugnaverunt\n")
    print(dictator)

def scribo():
    dictator = Initial("write\n" , None ,"I = scribo , you(singular) = scribis , he/she = scribit , we = scribimus , you(plural) = scribitis , they = scribunt\n" ,"I = scribebam , you(singular) = scirbebas , he/she = scribebat , we = scribebamus , you(singular) = scribebatis , they = scribebant\n" ,"I = scripsi , you(singular) = scripsisti , he/she = scripsit , we = scripsimus , you(plural) = scripsistis , they = scripserunt\n")
    print(dictator)

def tuus():
    dictator = Initial("your\n" , None , None , None , None)
    print(dictator)

def paro():
    dictator = Initial("prepare\n" , None ,"I = paro , you(singular) = paras , he/she = parat , we = paramus , you(plural) = paratis , they = parant\n" ,"I = parabam , you(singular) = parabas , he/she = parabat , we = parabamus , you(plural) = parabatis , they = parabant\n" ,"I = paravi , you(singular) = paravisti , he/she = paravit , we = paravimus , you(plural) = paravistis , they = paraverunt\n")
    print(dictator)
    
def cum():
    dictator = Initial("with\n" , None , None , None , None)
    print(dictator)
    
def facio():
    dictator = Initial("make\n" ,"Does / do\n" ,"I = facio , you(singular) = facis , he/she = facit , we = facimus , you(plural) = facitis , they = faciunt\n" ,"I = faciebam , you(singular) = faciebas , he/she = faciebat , we = faciebamus , you(singular) = faciebatis , they = faciebant\n" ,"I = feci , you(singular) = fecisti , he/she = fecit , we = fecimus , you(plural) = fecistis , they = fecerunt\n")
    print(dictator)
    
def heri():
    dictator = Initial("yesterday\n" , None , None , None , None)
    print(dictator)
    
def ingens():
    dictator = Initial("huge\n" , None , None , None , None)
    print(dictator)
    
def nihil():
    dictator = Initial("nothing\n" , None , None , None , None)
    print(dictator)
    
def omnis():
    dictator = Initial("all\n" ,"every" , None , None , None)
    print(dictator)
    
def vendo():
    dictator = Initial("sell\n" , None ,"I = vendo , you(singular) = vendis , he/she = vendit , we = vendimus , you(plural) = venditis , they = vendunt\n" ,"I = vendebam , you(singular) = vendebas , he/she = vendebat , we = vendebamus , you(plural) = vendebatis , they = vendebant\n" ,"I = vendidi , you(singular) = vendidisti , he/she = vendidit , we = vendidimus , you(plural) = vendidistis , they = vendiderunt\n")
    print(dictator)
    
def navis():
    dictator = Initial("ship\n" ,"Nominative = navis(singular) / naves(plural) , Dative = navi(singular) / navibus(plural) , Accusative = navem(singular) / naves(plural)" , None , None , None)
    print(dictator)
    
def prope():
    dictator = Initial("near\n" , None , None , None, None)
    print(dictator)
    
def rogo():
    dictator = Initial("ask\n" , None ,"I = rogavi, you(singular) = rogavisti , he/she = rogavit , we = rogavimus , you(plural) = roagavistis , they = rogaverunt\n" , None , None , None)
    print(dictator)
    
def terreo():
    dictator = Initial("scare\n" ,"terrify / frightens\n" ,"I = terreo , you(singular) = terres , he/she = terret , we = terremus , you(plural) = terretis , they = terrent\n" ,"I = terrebam , you(singular) = terrebas , he/she = terrebat , we = terrebamus , you(plural) = terrebatis , they = terrebant\n" ,"I = terrui , you(singular) = terruisti , he/she = terruisti , he/she = terruit , we = terruimus , you(plural) = terruistis , they = terruerunt\n")
    print(dictator)
    
def inquit():
    dictator = Initial("says\n" ,"said\n" ,"I = N/A , you(singular) = inquis , he/she = inquit , we = inquimus , you(plural) = N/A , they = inquiunt\n" , None , None)
    print(dictator)
    
def tamen():
    dictator = Initial("however\n" , None , None , None , None)
    print(dictator)
    
def eum():
    dictator = Initial("him\n" , None , None , None , None)
    print(dictator)
    
def eam():
    dictator = Initial("her\n" , None , None , None , None)
    print(dictator)
    
def duco():
    dictator = Initial("lead\n" ,"takes\n" ,"I = duco , you(singular) = ducis , he/she = ducit , we = ducimus , you(plural) = ducitis , they = ducunt\n" ,"I = ducebam , you(singular) = ducebas , he/she = ducebat , we = ducebamus , you(plural) = ducebatis , they = ducebant\n" ,"I = duxi , you(singular) = duxisti , he/she = duxit , we = duximus , you(plural) = duxistis , they = duxerunt\n")
    print(dictator)
    
def saepe():
    dictator = Initial("often\n" , None , None , None , None)
    print(dictator)
    
def interficio():
    dictator = Initial("kill\n" ,"killed\n" ,"I = interfecio , you(singular) = interfecisti , he/she = interfecit , we = interfecimus , you(plural) = interfecistis , they = interfecerunt\n" , None , None)
    print(dictator)
    
def habito():
    dictator = Initial("lives\n" , None ,"I = habito , you(singular) = habitas , he/she = habitat , we = habitamus , you(plural) = habitatis , they = habitant\n" ,"I = habitabam , you(singular) = habitaba , he/she = habitabat , we = habitabamus , you(plural) = habitabatis , they = habitabant\n" ,"I = habitavi , you(singular) = habitavisti , he/she = habitavit , we = habitavimus , you(plural) = habitavistis , they = habitaverunt\n")
    print(dictator)
    
def silva():
    dictator = Initial("forest\n" ,"{woods} Nominative = silva(singular) / silvae(plural) , Dative = silvae(singular) / silvis(plural) , Accusative = silvam(singular) / silvas(plural)\n" , None , None , None)
    print(dictator)
    
def statim():
    dictator = Initial("at once\n" ,"immediately\n" , None , None , None)
    print(dictator)
    
def totus():
    dictator = Initial("whole\n" ,"entire\n" , None , None , None)
    print(dictator)
    
def pessimus():
    dictator = Initial("worst\n" ,"very bad\n" , None , None , None)
    print(dictator)
    
def cupio():
    dictator = Initial("desire\n" ,"want\n" ,"I = cupio , you(singular) = cupis , he/she = cupit , we = cupimus , you(plural) = cupitis , they = cupiunt\n" ,"I = cupiebam , you(singular) = cupiebas , he/she = cupiebat , we = cupiebamus , you(plural) = cupiebatis , they = cupiebant\n" ,"I = cupivi , you(singular) = cupivisti , he/she = cupivit , we = cupivimus , you(plural) = cupivistis , they = cupiverunt\n")
    print(dictator)
    
def celeriter():
    dictator = Initial("quickly\n" , None , None , None , None)
    print(dictator)
    
def do():
    dictator = Initial("give\n" , None ,"I = do , you(singular) = das , he/she = dat , we = damus , you(plural) = datis , they = dant\n" ,"I = dabam , you(singular) = dabas")

def iterum():
    dictator = Initial("again\n" , None , None , None , None)
    print(dictator)
    
def pulcher():
    dictator = Initial("beautiful\n" ,"handsome\n" , None , None , None)
    print(dictator)
    
def dies():
    dictator = Initial("day\n" ,"Nominative = dies(singular)")
    
