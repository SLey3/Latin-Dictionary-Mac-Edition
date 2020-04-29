# INITILIZATION 
class Initial:
    def __init__(self, definition, others = None, present = None, imperfect = None, perfect = None , otherInfo = None):
        self.definition = definition
        self.other_meanings = others
        self.present = present
        self.imperfect = imperfect
        self.perfect = perfect
        self.additionalInfo = otherInfo

    def __str__(self):
        return  str(self.__class__) + '\n' + '\n'.join((str(item) + ' = ' + str(self.__dict__[item]) for item in sorted(self.__dict__)))
    
# DEFINITIONS
def salve():
    dictator = Initial("hello\n" ,otherInfo="salvete = hello (plural)\n")
    print(dictator)
    
def vale():
    dictator = Initial("good-bye\n" ,otherInfo="valete = good-bye (plural)")
    print(dictator)

def et():
    dictator = Initial("and\n")
    print(dictator)

def est():
    dictator = Initial("is\n" ,present= "I = sum , you (singular) = es , he/she = est , we = sumus , you (plural) = estis , they = sunt\n" ,imperfect="I = eram, you(singular) = eras, he/she = erat, we = eramus, you(plural) = eratis, they = erant\n")
    print(dictator)

def In():
    dictator = Initial("in\n" ,"on\n")
    print(dictator)

def sunt():
    dictator = Initial("are\n" ,"there are / they are\n" ,"I = sum, you(singular) = es, he/she = est, we = sumus, you(plural) = estis, they = sunt\n" ,"I = eram, you(singular) = eras, he/she = erat, we = eramus, you(plural) = eratis, they = erant\n")
    print(dictator)
    
def non():
    dictator = Initial("not\n" ,"no\n")
    print(dictator)
    
def insula():
    dictator = Initial("island\n")
    print(dictator)
    
def sed():
    dictator = Initial("but\n")
    print(dictator)
    
def oppidum():
    dictator = Initial("town\n")
    print(dictator)

def quoque():
    dictator = Initial("also\n" , "too\n")
    print(dictator)

def canis():
    dictator = Initial("dog\n" ,"Nominative = canis(singular) / canes(plural) , Dative = cani(singular) / canibus(plural) , Accusative = canem(singular) / canes(plural)\n")
    print(dictator)

def coquus():
    dictator = Initial("cook\n" ,"Nominative = coquus(singular) / coqui(plural) , Dative = coquo(singular) / coquis(plural) , Accusative = coquum(singular) / coquos(plural)\n")
    print(dictator)

def filia():
    dictator = Initial("daughter\n" ,"Nominative = filia(singular) / filiae(plural) , Dative = filiae(singular) / filiis(plural) , Accusative = filiam(singular) / filias(plural)\n")
    print(dictator)

def filius():
    dictator = Initial("son\n" ,"Nominative = filius(singular) / filii(plural) , Dative = filio(singular) / filiis(plural) , Accusative = filium(singular) / filios(plural)\n")
    print(dictator)
    
def hortus():
    dictator = Initial("garden\n" ,"Nominative = hortus(singular) / horti(plural) , Dative = horto(singular) / hortis(plural) , Accusative = hortum(singular) / hortos(plural)\n")
    print(dictator)
    
def mater():
    dictator = Initial("mother\n" ,"Nominative = mater(singular) / matres(plural) , Dative = matri(singular) / matribus(plural) , Accusative = matrem(singular) / matres(plural)\n")
    print(dictator)

def pater():
    dictator = Initial("father\n" ,"Nominative = pater(singular) / patres(plural) , Dative = patri(singular) / patribus(plural) , Accusative = patrem(singular) / patres(plural)\n")
    print(dictator)

def servus():
    dictator = Initial("servant\n" ,"{slave} Nominative = servus(singular) / servi(plural) , Dative = servo(singular) / servis(plural) , Accusative = servum(singular) / servos(plural)\n" )
    print(dictator)

def via():
    dictator = Initial("road\n" ,"{street / way} Nominative = via(singular) / viae(plural) , Dative = viae(singular) / viis(plural) , Accusative = viam(singular) / vias(plural)\n")
    print(dictator)

def amicus():
    dictator = Initial("friend\n" ,"Nominative = amicus(singular) / amici(plural) , Dative = amico(singular) / amicis(plural) , Accusative = amicum(singular) / amicos(plural)\n")
    print(dictator)

def ancilla():
    dictator = Initial("female slave\n" ,"{Female servant}Nominative = ancilla(singular) / ancillae , Dative = ancillae(singular) / ancillis(plural) , Accusative = anicillam(singular) / ancillas(plural)\n")
    print(dictator)

def cena():
    dictator = Initial("dinner\n" ,"Nominative = cena(singular) / cenae(plural) , Dative = cenae(singular) / cenis(plural) , Accusative = cenam(singular) / cenas(plural)\n")
    print(dictator)

def cibus():
    dictator = Initial("food\n" ,"Nominative = cibus(singular) / cibi(plural) , Dative = cibo(singular) / cibis(plural) , Accusative = cibum(singular) / cibos(plural)\n")
    print(dictator)

def intro():
    dictator = Initial("enters\n",present="I = intro , you(singular) = intras , he/she = intrat , we = intramus , you(plural) = intratis , they = intrant\n" ,imperfect="I = intrabam , you(singular) = intrabas , he/she = intrabat , we = intrabamus , you(plural) = intrabatis , they = intrabant\n" ,perfect= "I = intravi , you(singular) = intravisti , he/she = intravit , we = intravimus , you(plural) = intravistis , they = intraverunt\n")
    print(dictator)

def saluto():
    dictator = Initial("greet\n" , present="I = saluto , you(singular) = salutas , he/she = salutat , we = salutamus , you(plural) = salutamus , you(plural) = salutatis , they = salutant\n" ,imperfect="I = salutabam , you(singular) = salutabas , he/she = salutabat , we = salutabamus , you(plural) = salutabatis , they = salutabant\n" ,perfect="I = salutavi , you(singular) = salutavisti , he/she = salutavit , we = salutavimus , you(plural) = salutavistis , they = salutaverunt\n")
    print(dictator)

def porto():
    dictator = Initial("carry\n" ,present="I = porto , you(singular) = portas , he/she = portat , we = portamus , you(plural) = portatis , they = portant\n" ,imperfect="I = portabam , you(singular) = portabas , he/she = portabat , we = portabamus , you(plural) = portabatis , they = portabant\n" , perfect="I = portavi , you(singular) = portavisti , he/she = portavit , we = portavimus , you(plural) = portavistis , they = portaverunt\n")
    print(dictator)

def video():
    dictator = Initial("see\n" ,present="I = video , you(singular) = vides , he/she = videt , we = videmus , you(plural) , vident\n" ,imperfect="I = videbam , you(singular) = videbas , he/she = videbat , we = videbamus , you(plural) = videbatis , they = videbant\n" ,perfect="I = vidi , you(singular) = vidisti , he/she = vidit , we = vidimus , you(plural) = vidistis , they = viderunt\n")
    print(dictator)

def dominus():
    dictator = Initial("master\n" ,"{lord} Nominative = dominus(singular) / domini(plural) , Dative = domino(singular) / dominis(plural) , Accusative = dominum(singular) / dominos(plural)\n")
    print(dictator)

def laetus():
    dictator = Initial("happy\n")
    print(dictator)

def mercator():
    dictator = Initial("merchant\n" ,"Nominative = mercator(singular) / mercatores(plural) , Dative = mercatori(singular) / mercatoribus(plural) , Accusative = mercatorem(singular) / mercatores(plural)\n")
    print(dictator)
    
def audio():
    dictator = Initial("hear\n" ,present="I = audio , you(singular) = audis , he/she = audit , we = audimus , you(plural) = auditis , they = audiunt\n" ,imperfect="I = audiebam , you(singular) = audiebas , he/she = audiebat , we = audiebamus , you(plural) = audiebatis , they = audiebant\n" ,perfect="I = audivi , you(singular) = audvisiti , he/she = audivit , we = audivimus , you(plural) = audivistis , they = audiverunt\n")
    print(dictator)

def dico():
    dictator = Initial("say\n" ,present="I = dico , you(singular) = dicis , he/she = dicit , we = dicimus , you(plural) = dicitis , they = dicunt\n" ,imperfect="I = dicebam , you(singular) = dicebas , he/she = dicebat , we = dicebamus , you(plural) = dicebatis , they = dicebant\n" ,perfect="I = dixi , you(singular) = dixisti , he/she = dixit , we = diximus , you(plural) = dixistis , they = dixerunt\n")
    print(dictator)

def unus():
    dictator = Initial("one\n")
    print(dictator)

def duo():
    dictator = Initial("two\n")
    print(dictator)

def tres():
    dictator = Initial("three\n")
    print(dictator)

def quattuor():
    dictator = Initial("four\n")
    print(dictator)

def quinque():
    dictator = Initial("five\n")
    print(dictator)

def sex():
    dictator = Initial("six\n")
    print(dictator)

def septem():
    dictator = Initial("seven\n")
    print(dictator)

def octo():
    dictator = Initial("eight\n")
    print(dictator)

def novem():
    dictator = Initial("nine\n")
    print(dictator)

def decem():
    dictator = Initial("ten\n")
    print(dictator)
    
def ad():
    dictator = Initial("to\n" ,"towards / at\n")
    print(dictator)

def ecce():
    dictator = Initial("look\n" ,"behold\n")
    print(dictator)
    
def magnus():
    dictator = Initial("big\n" ,"large / great\n")
    print(dictator)

def parvus():
    dictator = Initial("small\n" ,"little\n")
    print(dictator)

def ambulo():
    dictator = Initial("walk\n" ,present="I = ambulo , you(singular) = ambulas , he/she = ambulat , we = ambulamus , you(plural) = ambulatis , ambulant\n" ,imperfect="I = ambulabam , you(singular) = ambulabas , he/she = ambulabat , we = ambulabamus , you(plural) = ambulabatis , they = ambulabant\n" ,perfect="I = ambulavi , you(singular) = ambulavisti , he/she = ambulavit , we = ambulavimus , you(plural) = ambulavistis , they = ambulaverunt\n")
    print(dictator)

def iratus():
    dictator = Initial("angry\n")
    print(dictator)

def quis():
    dictator = Initial("who\n")
    print(dictator)

def quid():
    dictator = Initial("what\n")
    print(dictator)
    
def cur():
    dictator = Initial("why\n")
    print(dictator)

def ubi():
    dictator = Initial("where\n" ,"when\n")
    print(dictator)

def sum():
    dictator =  Initial("I am\n" ,present="I = sum , you(singular) = es , he/she = est , we = sumus , you(plural) = estis , they = sunt\n" ,imperfect="I = eram , you(singular) = eras , he/she = erat , we = eramus , you(plural) = eratis , they = erant\n")
    print(dictator)

def eheu():
    dictator = Initial("oh no\n" ,"oh dear / alas\n")
    print(dictator)

def pecunia():
    dictator = Initial("money\n" ,"Nominative = pecunia(singular) / pecuniae(plural) , dative = pecuniae(singular) / pecuniis(plural) , accusative = pecuniam(singular) , pecunias(plural)\n")
    print(dictator)

def ego():
    dictator = Initial("I\n")
    print(dictator)

def tu():
    dictator = Initial("you\n")
    print(dictator)

def habeo():
    dictator = Initial("have\n" ,"has\n" ,"I = habeo , you(singular) = habes , he/she = habet , we = habemus , you(plural) = habetis , they = habent\n" ,"I = habebam , you(singular) = habebas , he/she = habebat , we = habebamus , you(plural) = habebatis , they = habebant\n" ,"I = habui , you(singular) = habuisti , he/she = habuit , we = habuimus , you(plural) = habuistis , they = habuerunt\n")
    print(dictator)

def respondeo():
    dictator = Initial("reply\n" ,"answer / respond\n" ,"I = respondeo , you(singular) = respondes , he/she = respondet, we = respondemus , you(plural) = respondetis , they = respondent\n" ,"I = respondebam , you(singular) = respondebas , he/she = respondebat , we = respondebamus , you(plural) = respondebatis , they = respondebant\n" ,"I = respondi , you(singular) = respondisti , he/she = respondit , we = respondimus , you(plural) = respondistis , they = responderunt\n")
    print(dictator)

def venio():
    dictator = Initial("come\n" ,present="I = venio , you(singular) = venis , he/she = venit , we = venimus , you(plural) = venitis , they = veniunt\n" ,imperfect="I = veniebam , you(singular) = veniebas , he/she = veniebat , we = veniebamus , you(Plural) = vaniebatis , they = veniebant\n")
    print(dictator)
def rideo():
    dictator = Initial("laugh\n" ,"smile" ,"I = rideo , you(singular) = rides , he/she = ridet , we = ridemus , you(plural) = ridetis , they = rident\n" ,"I = ridebam , you(singular) = ridebas , he/she = ridebat , we = ridebamus , you(plural) = ridebatis , they = ridebant\n" ,"I = risi , you(singular) = risisti , he/she = risit , we = risimus , you(plural) = risistis , they = riserunt\n")
    print(dictator)
    
def quod():
    dictator = Initial("because\n")
    print(dictator)
    
def ex():
    dictator = Initial("out of\n" ,"out from / from\n")
    print(dictator)
    
def voco():
    dictator = Initial("call\n" ,"summon\n" ,"I = voco , you(singular) = vocas , he/she = vocat , we = vocamus , you(plural) = vocatis , they = vocant\n" ,"I = vocabam , you(singular) = vocabas , he/she = vocabat , we = vocabamus you(plural) = vocabatis , they = vocabant\n" ,"I = vocavi , you(singular) = vocavisti , he/she = vocavit , we = vocavimus , you(plural) = vocavistis , they = vocaverunt\n")
    print(dictator)

def clamo():
    dictator = Initial("shout\n" ,"yell / noise (written as ''clamor'')\n" ,"I = clamo , you(singular) = clamas , he/she = clamat , we = clamamus , you(plurs) = clamatis , they = clamant\n" ,"I = clamabam , you(singular) = clamabas , he/she = clamabat , we = clamabamus , you(plural) = clamabatis, they = clamabant\n" ,"I = clamavi , you(singular) = clamavisti , he/she = clamavit , we = clamavimus , you(plural) = clamvistis , they = clamaverunt\n")
    print(dictator)

def specto():
    dictator = Initial("look\n" ,"watch\n" ,"I = specto , you(singular) = spectas , he/she = spectat , we = spectamus , you(singular) = spectatis , they = spectant\n" ,"I = spectabam , you(singular) = spectabas , he/she = spectabat , we = spectabamus , you(plural) = spectabatis , they = spectabant\n" ,"I = spectavi , you(singular) = spectavisti , he/she = spectavit , we = spectavimus , you(plural) = spectavistis , they = spectaverunt\n")
    print(dictator)

def taberna():
    dictator = Initial("shop\n" ,"{store / inn} Nominative = taberna(singular) / tabernae(plural) , Dative = tabernae(singular) / tabernis(plural) , Accusative = tabernam(singular) / tabernas(plural)\n")
    print(dictator)

def laboro():
    dictator = Initial("work\n",present="I = laboro , you(singular) = laboras , he/she = laborat , we = laboramus , you(plural) = laboratis , they = laborant\n" ,imperfect="I = laborabam , you(singular) = laborabas , he/she = laborabat , we = laborabamus , you(plural) = laborabatis , they = laborabant\n" ,perfect="I = laboravi , you(singular) = laboravisti , he/she = laboravit , we = laboravimus , you(plural) = laboravistis , they = laboraverunt\n")
    print(dictator)

def femina():
    dictator = Initial("woman\n" ,"Nominative = femina(singular) / feminae(plural) , Dative = feminae(singular) / feminis(plural) , Accusative = Feminam(singular) / feminas(plural)\n")
    print(dictator)

def vir():
    dictator = Initial("man\n" ,"Nominative = vir(singular) / viri(plural) , Dative = viro(singular) / viris(plural) , Accusative = virum(singular) / viros(plural)\n")
    print(dictator)  

def puer():
    dictator = Initial("boy\n" ,"Nominative = puer(singular) / puri(plural) , Dative = puero(singular) / pueris(plural) , Accusative = puerum(singular) / pueros(plural)\n")
    print(dictator) 

def puella():
    dictator = Initial("girl\n" ,"Nominative = puella(singular) / puellae(plural) , Dative = puellae(singular) / puellis(plural) , Accusative = puellam(singular) / puellas(plural)\n")
    print(dictator)
    
def multus():
    dictator = Initial("many\n" ,"much\n")
    print(dictator)
    
def urbs():
    dictator = Initial("city\n" ,"Nominative = urbs(singular) / urbes(plural) , Dative = urbi(singular) / urbibus(plural) , Accusative = urbem(singular) / urbes(plural)\n")
    print(dictator)
   
def agricola():
    dictator = Initial("farmer\n" ,"Nominative = agricola(singular) / agricolae(plural) , Dative = agricolae(singular) / agricolis(plural) , Accusative = agricolam(singular) / agricolas(plural)\n")
    print(dictator)

def curro():
    dictator = Initial("run\n" ,present="I = curro , you(singular) = curris , he/she = currit , we = currimus , you(plural) = curritis , they = currunt\n" ,imperfect="I = currebam , you(singular) = currebas , he/she = currebat , we = currebamus , you(singualar) = currebatis, they = currebant\n" ,perfect="I = cucurri , you(singular) = cucurristi , he/she = cucurrit , we = cucurrimus , you(singular) = cucurristis , they = cucurrerunt\n")
    print(dictator)
    
def hodie():
    dictator = Initial("today\n")
    print(dictator)
    
def iuvenis():
    dictator = Initial("youth\n" ,"{young man} Nominative = iuvenis(singular) / iuvenes(plural) , Dative = iuveni(singular) / iuvenibus(plural) , Accusative = iuvenem(singular) / iuvenes(plural)\n")
    print(dictator)
    
def meus():
    dictator = Initial("my\n" ,"mine\n")
    print(dictator)
    
def senex():
    dictator = Initial("old man\n" ,"Nominative = senx(singular) / senes(plural), Dative = seni(plural) / senibus(plural) , Accusative = senem(singular) / senes(plural)\n")
    print(dictator)
    
def sto():
    dictator = Initial("stand\n" ,present="I = sto , you(singular) = stas , he/she = stat , we = stamus , you(plural) = statis , they = stant\n" ,imperfect="I = stabam , you(singular) = stabas , he/she = stabat , we = stabamus , you(plural) = stabatis , they = stabant\n" ,perfect="I = seti , you(singular) = stetisti , he/she = stetit , we = stetimus , you(plural) = stetistis , they = steterunt\n")
    print(dictator)
    
def optimus():
    dictator = Initial("best\n" ,"excellent / very good\n")
    print(dictator)
    
def volo():
    dictator = Initial("want\n" ,present="I = volo , you(singular) = vis , he/she = vult , we = volumus , you(plural) = vultis , they = volunt\n" ,imperfect="I = volebam, you(singular) = volebas , he/she = volebat , we = volebamus , you(plural) = volebatis , they = volebant\n" ,perfect="I = volui , you(singular) = voluisti , he/she = voluit , we = voluimus , you(singular) = voluistis , they = voluerunt\n")
    print(dictator)
    
def fortis():
    dictator = Initial("strong\n" ,"brave\n")
    print(dictator)
    
def emo():
    dictator = Initial("buy\n" ,present="I = emo , you(sinuglar) = emis , he/she = we = emimus , you(plural) = emitis , they = emunt\n" ,imperfect="I = emebam , you(singualar) = emebas , he/she = emebat , we = emebamus , you(plural) = emebatis , they = emebant\n" ,perfect="I = emi , you(singular) = emisti , he/she = emit , we = emimus , you(plural) = emistis , they = emeverunt\n")
    print(dictator)
    
def pulso():
    dictator = Initial("hit\n" ,"punch / strike / knocks at\n" ,"I = pulso , you(singular) = pulsas , he/she = pulsat , we = pulsamus , you(plural) = pulsatis , they = pulsant\n" ,"I = pulsabam , you(singular) = pulsabas , he/she = pulsabat , we = pulsabamus , you(singular) = pulsabatis , they = pulsabant\n" ,"I = pulsavi , you(singular) = pulsavisti , he/she = pulsavit , we = pulsavimus , you(plural) = pulsavistis , they = pulsaverunt\n")
    print(dictator)
    
def bonus():
    dictator = Initial("good\n")
    print(dictator)
    
def malus():
    dictator = Initial("bad\n" ,"evil\n")
    print(dictator)
    
def festino():
    dictator = Initial("hurry\n" ,present="I = festino , you(singular) = festinas , he/she = festinat , we = festinamus , you(plural) = festinatis , they = festinant\n" ,imperfect="I = festinabam , you(singular) = festinabas , he/she = festinabat , we = festinabamus , you(plural) = festinabatis , they = festinabant\n" ,perfect="I = festinavi , you(singular) = festinavisti , he/she = festinavit , we = festinavimus , you(plural) =  festinavistis , they = festinaverunt\n")
    print(dictator)

def per():
    dictator = Initial("through\n")
    print(dictator)

def pugno():
    dictator = Initial("fight\n" ,present="I = pugno , you(singular) = pugnas , he/she = pugnat , we = pugnamus , you(plural) = pugnatis , they = pugnant\n" ,imperfect="I = pugnabam , you(singular) = pugnabas , he/she = pugnabat , we = pugnabamus , you(plural) = pugnabatis , they = pugnabant\n" ,perfect="I = pugnavi , you(singular) = pugnavisti , he/she = pugnavit , we = pugnavimus , you(plural) = pugnavistis , they = pugnaverunt\n")
    print(dictator)

def scribo():
    dictator = Initial("write\n" ,present="I = scribo , you(singular) = scribis , he/she = scribit , we = scribimus , you(plural) = scribitis , they = scribunt\n" ,imperfect="I = scribebam , you(singular) = scirbebas , he/she = scribebat , we = scribebamus , you(singular) = scribebatis , they = scribebant\n" ,perfect="I = scripsi , you(singular) = scripsisti , he/she = scripsit , we = scripsimus , you(plural) = scripsistis , they = scripserunt\n")
    print(dictator)

def tuus():
    dictator = Initial("your\n")
    print(dictator)

def paro():
    dictator = Initial("prepare\n" ,present="I = paro , you(singular) = paras , he/she = parat , we = paramus , you(plural) = paratis , they = parant\n" ,imperfect="I = parabam , you(singular) = parabas , he/she = parabat , we = parabamus , you(plural) = parabatis , they = parabant\n" ,perfect="I = paravi , you(singular) = paravisti , he/she = paravit , we = paravimus , you(plural) = paravistis , they = paraverunt\n")
    print(dictator)
    
def cum():
    dictator = Initial("with\n")
    print(dictator)
    
def facio():
    dictator = Initial("make\n" ,"Does / do\n" ,"I = facio , you(singular) = facis , he/she = facit , we = facimus , you(plural) = facitis , they = faciunt\n" ,"I = faciebam , you(singular) = faciebas , he/she = faciebat , we = faciebamus , you(singular) = faciebatis , they = faciebant\n" ,"I = feci , you(singular) = fecisti , he/she = fecit , we = fecimus , you(plural) = fecistis , they = fecerunt\n")
    print(dictator)
    
def heri():
    dictator = Initial("yesterday\n")
    print(dictator)
    
def ingens():
    dictator = Initial("huge\n")
    print(dictator)
    
def nihil():
    dictator = Initial("nothing\n")
    print(dictator)
    
def omnis():
    dictator = Initial("all\n" ,"every")
    print(dictator)
    
def vendo():
    dictator = Initial("sell\n" ,present="I = vendo , you(singular) = vendis , he/she = vendit , we = vendimus , you(plural) = venditis , they = vendunt\n" ,imperfect="I = vendebam , you(singular) = vendebas , he/she = vendebat , we = vendebamus , you(plural) = vendebatis , they = vendebant\n" ,perfect="I = vendidi , you(singular) = vendidisti , he/she = vendidit , we = vendidimus , you(plural) = vendidistis , they = vendiderunt\n")
    print(dictator)
    
def navis():
    dictator = Initial("ship\n" ,"Nominative = navis(singular) / naves(plural) , Dative = navi(singular) / navibus(plural) , Accusative = navem(singular) / naves(plural)")
    print(dictator)
    
def prope():
    dictator = Initial("near\n")
    print(dictator)
    
def rogo():
    dictator = Initial("ask\n" ,perfect="I = rogavi, you(singular) = rogavisti , he/she = rogavit , we = rogavimus , you(plural) = roagavistis , they = rogaverunt\n")
    print(dictator)
    
def terreo():
    dictator = Initial("scare\n" ,"terrify / frightens\n" ,"I = terreo , you(singular) = terres , he/she = terret , we = terremus , you(plural) = terretis , they = terrent\n" ,"I = terrebam , you(singular) = terrebas , he/she = terrebat , we = terrebamus , you(plural) = terrebatis , they = terrebant\n" ,"I = terrui , you(singular) = terruisti , he/she = terruisti , he/she = terruit , we = terruimus , you(plural) = terruistis , they = terruerunt\n")
    print(dictator)
    
def inquit():
    dictator = Initial("says\n" ,"said\n" ,"I = N/A , you(singular) = inquis , he/she = inquit , we = inquimus , you(plural) = N/A , they = inquiunt\n")
    print(dictator)
    
def tamen():
    dictator = Initial("however\n")
    print(dictator)
    
def eum():
    dictator = Initial("him\n")
    print(dictator)
    
def eam():
    dictator = Initial("her\n")
    print(dictator)
    
def duco():
    dictator = Initial("lead\n" ,"takes\n" ,"I = duco , you(singular) = ducis , he/she = ducit , we = ducimus , you(plural) = ducitis , they = ducunt\n" ,"I = ducebam , you(singular) = ducebas , he/she = ducebat , we = ducebamus , you(plural) = ducebatis , they = ducebant\n" ,"I = duxi , you(singular) = duxisti , he/she = duxit , we = duximus , you(plural) = duxistis , they = duxerunt\n")
    print(dictator)
    
def saepe():
    dictator = Initial("often\n")
    print(dictator)
    
def interficio():
    dictator = Initial("kill\n" ,"killed\n" ,"I = interfecio , you(singular) = interfecisti , he/she = interfecit , we = interfecimus , you(plural) = interfecistis , they = interfecerunt\n")
    print(dictator)
    
def habito():
    dictator = Initial("lives\n" ,present="I = habito , you(singular) = habitas , he/she = habitat , we = habitamus , you(plural) = habitatis , they = habitant\n" ,imperfect="I = habitabam , you(singular) = habitaba , he/she = habitabat , we = habitabamus , you(plural) = habitabatis , they = habitabant\n" ,perfect="I = habitavi , you(singular) = habitavisti , he/she = habitavit , we = habitavimus , you(plural) = habitavistis , they = habitaverunt\n")
    print(dictator)
    
def silva():
    dictator = Initial("forest\n" ,"{woods} Nominative = silva(singular) / silvae(plural) , Dative = silvae(singular) / silvis(plural) , Accusative = silvam(singular) / silvas(plural)\n")
    print(dictator)
    
def statim():
    dictator = Initial("at once\n" ,"immediately\n")
    print(dictator)
    
def totus():
    dictator = Initial("whole\n" ,"entire\n")
    print(dictator)
    
def pessimus():
    dictator = Initial("worst\n" ,"very bad\n")
    print(dictator)
    
def cupio():
    dictator = Initial("desire\n" ,"want\n" ,"I = cupio , you(singular) = cupis , he/she = cupit , we = cupimus , you(plural) = cupitis , they = cupiunt\n" ,"I = cupiebam , you(singular) = cupiebas , he/she = cupiebat , we = cupiebamus , you(plural) = cupiebatis , they = cupiebant\n" ,"I = cupivi , you(singular) = cupivisti , he/she = cupivit , we = cupivimus , you(plural) = cupivistis , they = cupiverunt\n")
    print(dictator)
    
def celeriter():
    dictator = Initial("quickly\n")
    print(dictator)
    
def do():
    dictator = Initial("give\n" ,present="I = do , you(singular) = das , he/she = dat , we = damus , you(plural) = datis , they = dant\n" ,imperfect="I = dabam , you(singular) = dabas")
    print(dictator)
def iterum():
    dictator = Initial("again\n")
    print(dictator)
    
def pulcher():
    dictator = Initial("beautiful\n" ,"handsome\n")
    print(dictator)
    
def dies():
    dictator = Initial("day\n" ,"Nominative = dies(singular) / dies(plural) , Dative = dii(singular) / diibus(plural) , Accusative = diem(singular) / dies(plural)\n")
    print(dictator)

def fero():
    dictator = Initial("bring\n" ,"carry\n" ,"I = fero , you(singular) = fers , he/she = fert , we = ferimus , you(plural) = fertis, they = ferunt\n" ,"I = ferebam , you(singular) = ferebas , he/she = ferebat , we = ferebamus , you(plural) = ferebatis , they = ferebant\n" ,"I = tuli , you(singular) = tulisti , he/she = tulit , we = tulimus , you(plural) = tulistis , they = tulerunt\n")
    print(dictator)
    
def homo():
    dictator = Initial("human\n" ,"{person/man} Nominative = homo(singular) / homines(plural) , Dative = homini(singular) / hominibus(plural) , Accusative = hominem(singular) / homines(plural)\n")
    print(dictator)
    
def maneo():
    dictator = Initial("remain\n" ,"stay\n" ,"I = maneo , you(singular) = manes , he/she = manet , we = manemus , you(plural) = manetis , they = manent\n" ,"I = manebam , you(singular) = manebas , he/she = manebat , we = manebamus , you(singular) = manebatis , they = manebant\n" ,"I = mansi , you(singular) = mansisti , he/she = mansit , we = mansimus , you(plural) = mansistis , they = manserunt\n")
    print(dictator)
    
def medius():
    dictator = Initial("middle\n")
    print(dictator)
    
def mox():
    dictator = Initial("soon\n")
    print(dictator)
    
def ostendo():
    dictator = Initial("show\n" ,present="I = ostendo , you(singular) = ostendis , he/she = ostendit , we = ostendimus , you(plural) = ostenditis , they = ostendunt\n" ,imperfect="I = ostendebam , you(singular) = ostendebas , he/she = ostendebat , we = ostendebamus , you(plural) = ostendebatis . they = ostendebant\n" ,perfect="I = ostendi , you(singular) = ostendisti , he/she = ostendit , we = ostendimus , you(plural) = ostendistis , they = ostenderunt\n")
    print(dictator)
    
def trado():
    dictator = Initial("hand over\n" ,present="I = trado , you(singular) = tradis , he/she = tradit , we = tradimus , you(plural) = traditis , they = tradunt\n" ,imperfect="I = tradebam , you(singular) = tradebas , he/she = tradebat , we = tradebamus , you(plural) = tradebatis , they = tradebant\n" ,perfect="I = tradidi , you(singular) = tradidisti , he/she = tradidit , we = tradidimus , you(plural) = tradidistis , they = tradiderunt\n")
    print(dictator)
    
def nomen():
    dictator = Initial("name\n")
    print(dictator)
    
def accipio():
    dictator = Initial("recieve\n" ,"accept\n" ,"I = accipio , you(singular) = accipis , he/she = accipit , we = accipimus , you(plural) = accipitis , they = accipiunt\n" ,"I = accipiebam , you(singular) = acciebas , he/she = accipiebat , we = accipiebamus , you(plural) = accipiebatis , they = accipiebant\n" ,"I = accepi , you(singular) = accepisti , he/she = accepit , we = accepimus , you(plural) = accepistis , they = acceperunt\n")
    print(dictator)
    
def frater():
    dictator = Initial("brother\n" ,"Nominative = frater(singular) / fratres(plural) , Dative = fratri(singular) / fratribus(plural) , Accusative = fratrem(singular) / fratres\n")
    print(dictator)
    
def soror():
    dictator = Initial("sister\n" ,"Nominative = soror(singular) / sorores(plural) , Dative = sorori(singular) / sororibus(plural) , Accusative = sororem(singular) / sorores(plural)\n")
    print(dictator)
    
def invenio():
    dictator = Initial("find\n" ,present="I = invenio\n" ,perfect="I = inveni , you(singular) = invenisti , he/she = invenit , we = invenimus , you(plural) = invenistis , they = invenerunt\n")
    print(dictator)
    
def pax():
    dictator = Initial("peace\n" ,"Nominative = pax(singular) / paces(plural) , Dative = paci(singular) / pacibus(plural) , Accusative = pacem(singular) / paces(plural)\n")
    print(dictator)
    
def bellum():
    dictator = Initial("war\n")
    print(dictator)
    
def nos():
    dictator = Initial("we(plural)\n" ,"us\n")
    print(dictator)
    
def quam():
    dictator = Initial("than\n" ,"how\n")
    print(dictator)
    
def semper():
    dictator = Initial("always\n")
    print(dictator)
    
def taceo():
    dictator = Initial("silent\n" ,"quiet\n" ,"I = taceo , you(singular) = taces , he/she = tacet , we = tacemus , you(plural) = tacetis , they = tacent\n" ,"I = tacebam , you(singular) = tacebas , he/she = tacebat , we = tacebamsus , you(plural) = tacebatis , they = tacebant\n" ,"I = tacui , you(singular) = tacuisti , he/she = tacuit , we = tacuimus , you(plural) = tacuistis , they - tacuerunt\n" ,"Tace = Shut up\n")
    print(dictator)
    
def vos():
    dictator = Initial("you(plural)\n")
    print(dictator)
    
def stultus():
    dictator = Initial("foolish\n" ,"stupid\n")
    print(dictator)
    
def callidus():
    dictator = Initial("clever\n" ,"cunning\n")
    print(dictator)
    
def uxor():
    dictator = Initial("wife\n" ,"Nominative = uxor(singular) / uxores(plural) , Dative = uxori(singular) / uxoribus(plural) , Accusative = uxorem(singular) / uxores(plural)\n")
    print(dictator)
    
def suus():
    dictator = Initial("his\n" ,"hers/its/their\n")
    print(dictator)
    
def solus():
    dictator = Initial("alone\n" ,"only/lonely\n")
    print(dictator)
    
def nuntio():
    dictator = Initial("announce\n" ,present="I = nuntio , you(singular) = nuntias , he/she = nuntiat , we = nuntiamus , you(plural) = nuntiatis , they = nuntiant\n" ,imperfect="I = nuntiabam , you(singular) = nuntiabas , he/she = nuntiabat , we = nuntiabamus , you(plural) = nuntiabatis , they = nuntiabant\n" ,perfect="I = nuntiavi , you(singular) = nuntiavisti , he/she = nuntiavit , we = nuntiavimus , you(plural) = nuntiavistis , they = nuntiaverunt\n")
    print(dictator)
    
def magister():
    dictator = Initial("teacher\n" ,"master\n")
    print(dictator)
    
def discipulus():
    dictator = Initial("student\n")
    print(dictator)
    
def doceo():
    dictator = Initial("teach\n" ,present="I = doceo , you(singular) = doces , he/she = docet , we = docemus , you(plural) = docetis , they = docent\n" ,imperfect="I = docebam , you(singular) = docebas , he/she = docebat , we = docebamus , you(plural) = docebatis , they = docebant\n" ,perfect="I = docui , you(singular) = docuisti , he/she = docuit , we = docuimus , you(plural) = docuistis , they = docuerunt\n")
    print(dictator)
    
def num():
    dictator = Initial("surely not\n")
    print(dictator)
    
def subito():
    dictator = Initial("suddenly\n")
    print(dictator)
    
def gratias():
    dictator = Initial("thank\n" ,"Nominative = gratiae(plural) , Dative = gratiis(plural) , Accusative = Gratias(plural)\n")
    print(dictator)
    
def quaeso():
    dictator = Initial("please\n")
    print(dictator)
    
def capio():
    dictator = Initial("take\n" ,"capture\n" ,"I = capio , you(singular) = capis , he/she = capit , we = capimus , you(plural) = capitis , they = capiunt\n" ,"I = capiebam , you(singular) = capiebas , he/she = capiebat , we = capiebamus , you(plural) = capiebatis , they = capiebant\n" ,"I = cepi , you(singular) = cepisti , he/she = cepit , we = cepimus , you(plural) = cepistis , they = ceperunt\n")
    print(dictator)

def nunc():
    dictator = Initial("now\n")
    print(dictator)
    
def tum():
    dictator = Initial("then\n")
    print(dictator)
    
def mihi():
    dictator = Initial("to me\n" ,"for me\n")
    print(dictator)
    
def tibi():
    dictator = Initial("to you\n" ,otherInfo="vobis(plural) = for you\n")
    print(dictator)
    
def credo():
    dictator = Initial("believe\n" ,"trusts/faith\n" ,"I = credo , you(singular) = credis , he/she = credit , we = credimus , you(plural) = creditis , they = credunt\n" ,"I = credebam , you(singular) = credebas , he/she = credebat , we = credebamus , you(plural) = credebatis , they = credebant\n" ,"I = credidi , you(singular) = credidisti , he/she = credidit , we = credidimus , you(plural) = credidimus , they = crediderunt\n")
    print(dictator)
    
def de():
    dictator = Initial("from\n" ,"about\n")
    print(dictator)
    
def noster():
    dictator = Initial("our\n")
    print(dictator)
    
def placet():
    dictator = Initial("pleases\n" ,"likes/suit\n" ,"I = placeo , you(singular) = places , he/she = placet , we = placemus , you(plural) = placetis , they = placent\n" ,"I = placebam , you(singular) = placebas , he/she = placebat , we = placebamus , you(plural) = placebatis , they = placebant\n" ,"I = placui , you(singular) = placuisti , he/she = placuit , we = placuimus , you(plural) = placuistis , they = placuerunt\n")
    print(dictator)
    
def civis():
    dictator = Initial("citizen\n" ,"Nominative = civis(singular) / cives(plural) , Dative = civi(singular) / civibus(plural) , Accusative = civem(singular) / cives(plural)\n")
    print(dictator)
    
def lego():
    dictator = Initial("read\n" ,present="I = lego , you(singular) = legis , he/she = legit , we = legimus , you(plural) = legitis , they = legunt\n" ,imperfect="I = legebam , you(singular) = legebas , he/she = legebat , we = legebamus , you(plural) = legebatis , they = legebant\n" ,perfect="I = legi , you(singular) = legisti , he/she = legit , we = legimus , you(plural) = legistis , they = legerunt\n")
    print(dictator)
    
def iam():
    dictator = Initial("now\n" ,"already\n")
    print(dictator)
    
def terra():
    dictator = Initial("land\n" ,"{earth/ground} Nominative = terra(singular) / terrae(plural) , Dative = terrae(singular) / terris(plural) , Accusative = terram(singular) / terras(plural)\n")
    print(dictator)
    
def custodio():
    dictator = Initial("guard\n" ,present="I = custodio , you(singular) = custodis , he/she = custodit , we = custodimus , you(plural) = custoditis , they = custodiunt\n" ,imperfect="I = custodiebam , you(singular) = custodiebas , he/she = custodiebat , we = custodiebamus , you(plural) = custodiebatis , they = custodiebant\n" ,perfect="I = custodivi , you(singular) = custodivisti , he/she = custodivit , we = custodivimus , you(plural) = custodivistis , they = custodiverunt\n" ,otherInfo="custodio is like multiple guards while custos = one guard\n")
    print(dictator)
    
def fortiter():
    dictator = Initial("bravely\n" ,"strongly\n")
    print(dictator)
    
def fugio():
    dictator = Initial("flee\n" ,"run away\n" ,"I = fugio , you(singular) = fugis , he/she = fugit , we = fugimus , you(plural) = fugitis, they = fugiunt\n" ,"I = fugiebam , you(singular) = fugiebas , he/she = fugiebat , we = fugiebamus , you(plural) = fugiebatis , they = fugiebant\n" ,"I = fugi , you(singular) = fugisti , he/she = fugit , we = fugimus , you(plural) = fugistis , they = fugerunt\n")
    print(dictator)
    
def igitur():
    dictator = Initial("therefore\n" ,"And so...\n")
    print(dictator)
    
def tristis():
    dictator = Initial("sad\n")
    print(dictator)
    
def iubeo():
    dictator = Initial("order\n" ,present="I = iubeo , you(singular) = iubes , he/she = iubet , we = iubemus , you(plural) = iubetis , they = iubent\n" ,imperfect="I = iubebam , you(singular) = iubebas , he/she = iubebat , we = iubebamus , you(plural) = iubebatis , they = iubebant\n" ,perfect="I = iussi , you(singular) = iussisti , he/she = iussit , we = iussimus , you(plural) = iussistis , they = iusserunt\n")
    print(dictator)
    
def deleo():
    dictator = Initial("grieve\n" ,"be hurt\n")
    print(dictator)
    
def displodo():
    dictator = Initial("explode\n")
    print(dictator)   
    
def aeger():
    dictator = Initial("sick\n" ,"{ill} Nominative = aeger(singular) / aegri(plural) , Dative = aegro(singular) /aegris(plural) , Accusative = aegrum(singular) / aegris(plural)\n")
    print(dictator)
    
def alter():
    dictator = Initial("other\n" ,"{of two} Nominative = alter(singular) / alteri(plural) , Dative = altero(singular) / alteris(plural) , Accusative = alterum(singular) / alteros(plural)\n")
    print(dictator)

def fessus():
    dictator = Initial("tired\n" ,"Nominative = fessus(singular) / fessi(plural) , Dative = fesso(singular) / fessis(plural) , Accusative = fessum(singular) / fessos(plural)\n")
    print(dictator)
    
def ignavus():
    dictator = Initial("cowardly\n" ,"{lazy} Nominative = ignavus(singular) / ignavi(plural) . Dative = ignavo(singular) / ignavis(plural) , Accusative = ignavos(singular) / ignavos(plural)\n")
    print(dictator)
    
def nolo():
    dictator = Initial("not want\n" ,"be unwilling / refuse\n" ,"I = nolo , you(singular) = non vis , he/she = non vult , we = nolumus , you(plural) = non vultis , they = nolunt\n" ,"I = nolebam , you(singular) = nolebas , he/she = nolebat , we = nolebamus , you(plural) = nolebatis , they = nolebant\n" ,"I = nolui , you(singular) = noluisti , he/she = noluit , we = noluimus , you(plural) = noluistis , they = noluerunt\n")
    print(dictator)
    
def traho():
    dictator = Initial("drag\n" ,"pull\n" ,"I = traho , you(singular) = trahis , he/she = trahit , we = trahimus , you(plural) = trahitis , they = trahunt\n" ,"I = trahebam , you(singular) = trahebas , he/she = trahebat , we = trahebamus , you(plural) = trahebatis , they = trahebant\n" ,"I = traxi , you(singular) = traxisti , he/she = traxit , we = traximus , you(plural) = traxistis , they = traxerunt\n")
    print(dictator)
    
def hic():
    dictator = Initial("this\n" ,"Nominative = hic(singular) / hi(plural) , Dative = huic(singular) / his(plural) , Accusative = hunc(singular) / hos(plural)\n")
    print(dictator)
    
def ille():
    dictator = Initial("that\n" ,"{he} Nominative = ille(singular) / illi(plural) , Dative = illi(singular) / illis(plural) , Accusative = illum(singular) / illos(plural)\n")
    print(dictator)
    
def possum():
    dictator = Initial("be able\n" ,"can\n" ,"I = possum , you(singular) = potes , he/she = potest , we = possumus , you(plural) = potestis , they = possunt\n" ,"I = poteram , you(singular) = poteras , he/she = poterat , we = poteramus , you(plural) = poteratis , they = poterant\n" ,"I = potui , you(singular) = potuisti , he/she = potuit , we = potuimus , you(plural) = potuistis , they = potuerunt\n")
    print(dictator)
    
def que():
    dictator = Initial("and\n" ,otherInfo="Placed after a word. (e.g materque pater)\n")
    print(dictator)

def ne():
    dictator = Initial(None ,otherInfo="Signals a question. (e.g. Estne)\n")
    print(dictator)
    
def ceteri():
    dictator = Initial("others\n" ,"{the rest} Nominative = ceteri(plural) , Dative = ceteris(plural) , Accusative = ceteros(plural)\n")
    print(dictator)

def novus():
    dictator = Initial("new\n" ,"Nominative = novus(singular) / novi(plural) , Dative = novo(singular) / novis(plural) , Accusative = novum(singular) / novos(plural)\n")
    print(dictator)
    
def se():
    dictator = Initial("himself\n" ,"{herself, itself, themselves} Nominative = None , Dative = sibi(singular and plural) , Accusative = sui(singular and plural)\n")
    print(dictator)
    
def vita():
    dictator = Initial("life\n" ,"Nominative = vita(singular) / vitae(plural) , Dative = vitae(singular) / vitis(plural) , Accusative = vitam(singular) / vitas\n")
    print(dictator)
    
def attonitus():
    dictator = Initial("astonished\n" ,"Nominative = attonitus(singular) / attonti(plural) , Dative = attonito(singular) / attonitis(plural) , Accusative = attonitum(singular) / attonitos(plural)\n")
    print(dictator)
    
def facilis():
    dictator = Initial("easy\n" ,"Nominative = facilis(singular) / faciles(plural) , Dative = facili(singular) / facilibus(plural) , Accusative = facilem(singular) / faciles(plural)\n")
    print(dictator)
    
def apud():
    dictator = Initial("among\n" ,"At someone's house\n")
    print(dictator)
    
def decorus():
    dictator = Initial("proper" ,"{appropriate / right} Nominative = decorus(singular) / decori(plural) , Dative = decoro(singular) / decoris(plural) , Accusative = decorum(singular) / decoros(plural)\n")
def ipse():
    dictator = Initial("-self\n" ,otherInfo="Used after him / her and other words that follows similary to those two words. (e.g himself, herself, and itself)\n")
    print(dictator)
    
def iste():
    dictator = Initial("That\n" ,otherInfo="In a negative sence\n")
    print(dictator)
    
def necesse():
    dictator = Initial("necessary\n")
    print(dictator)
    
def quamquam():
    dictator = Initial("although\n")
    print(dictator)
    
def deus():
    dictator = Initial("god\n" ,otherInfo="dea = goddess\n")
    print(dictator)