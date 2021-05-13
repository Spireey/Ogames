# RESTE A FAIRE: AFFICHAGE COULE (cf CheckCoule), AFFICHAGE VICTOIRE (cf CheckWin)

from turtle import *
from random import *

title("Bataille Navale")
setup(1500,750)
ht()
speed('fastest')
width(5)
up()
partieEncours = True
pvA, pvB, pvPO, pvCR, pvCO1, pvCO2, pvTO = 17, 17, 5, 4, 3, 3, 2

for j in range(2):
    for i in range(11):
        setheading(0)
        goto(-600+j*700,-250+i*50)
        down()
        forward(500)
        up()
        setheading(90)
        goto(-600+i*50+j*700,-250)
        down()
        forward(500)
        up()
goto(-350,310)
down()
write("Votre grille",False,"center",("arial",20,"normal"))
up()
goto(350,310)
down()
write("Grille adverse",False,"center",("arial",20,"normal"))
up()
dico = ["a","b","c","d","e","f","g","h","i","j"]
chiffres = ["0","1","2","3","4","5","6","7","8","9"]

for j in range(2):
    for i in range(10):
        goto(-600+j*700+i*50+25,265)
        down()
        write(chiffres[i],False,"center",("arial",15,"normal"))
        up()
        goto(-625+j*700,215-i*50)
        down()
        write(dico[i],False,"center",("arial",15,"normal"))
        up()

def liste_pos():
    liste=[]
    for i in range(10):
        for j in range(10):
            liste += [(i,j)]
    return liste

def position_random(liste):
    n=randint(0,len(liste)-1)
    return liste.pop(n)

def cercle(grille, y, x):
    if grille == 'a':
        goto(-575+x*50, 225-y*50)
        dot(30, 'black')
    else:
        goto(125+x*50, 225-y*50)
        dot(30, 'black')

def croix(grille, y, x):
    color('red')
    if grille == 'a':
        for i in range(4):
            goto(-575+x*50, 225-y*50)
            setheading(45+i*90)
            down()
            forward(25)
            up()
    else:
        for i in range(4):
            goto(125+x*50, 225-y*50)
            setheading(45+i*90)
            down()
            forward(25)
            up()
    color('black')

def checkWin():
    global partieEncours
    if pvA == 0 or pvB == 0:
        partieEncours = False
        if pvA == 0:
            clearscreen()
            hideturtle()
            goto(0,0)
            write('Gagnant: B', False, 'center')
        else:
            clearscreen()
            hideturtle()
            goto(0,0)
            write('Gagnant: A', False, 'center')

def Coule():
    print('Coulé')

def checkCoule():
    global pvPO, pvCR, pvCO1, pvCO2, pvTO
    if pvPO == 0:
        Coule()
        pvPO = -1
    if pvCR == 0:
        Coule()
        pvCR = -1
    if pvCO1 == 0:
        Coule()
        pvCO1 = -1
    if pvCO2 == 0:
        Coule()
        pvCO2 = -1
    if pvTO == 0:
        Coule()
        pvTO = -1
    
liste = liste_pos()

grilleA = [['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','','']]

grilleB = [['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','','']]

xPorteAvion,yPorteAvion = randint(0,2),randint(0,3)
xCroiseur, yCroiseur = randint(7,9),randint(0,3)
xContre1, yContre1 = randint(0,2),randint(4,7)
xContre2, yContre2 = randint(3,7),randint(7,9)
xTorpilleur, yTorpilleur = randint(3,6),randint(4,5)

xPorteAvionE,yPorteAvionE = randint(0,2),randint(2,5)
xCroiseurE, yCroiseurE = randint(3,6),randint(6,9)
xContre1E, yContre1E = 3,randint(2,5)
xContre2E, yContre2E = randint(6,9),randint(0,2)
xTorpilleurE, yTorpilleurE = randint(0,4),randint(0,1)

for i in range(5):
    grilleA[yPorteAvion][xPorteAvion+i]="x"
    grilleB[yPorteAvionE+i][xPorteAvionE]="po"
for i in range(4):
    grilleA[yCroiseur+i][xCroiseur]="x"
    grilleB[yCroiseurE][xCroiseurE+i]="cr"
for i in range(3):
    grilleA[yContre1+i][xContre1]="x"
    grilleA[yContre2][xContre2+i]="x"
    grilleB[yContre1E][xContre1E+i]="co1"
    grilleB[yContre2E+i][xContre2E]="co2"
for i in range(2):
    grilleA[yTorpilleur+i][xTorpilleur]="x"
    grilleB[yTorpilleurE][xTorpilleurE+i]="to"

for y in range(10):
    for x in range(10):
        if grilleA[y][x] == "x":
            cercle('a',y,x)

while partieEncours:
    bomb = textinput("Bombardement","Veuillez saisir la case à bombarder!")
    bomb = [i for i in bomb]
    bomb = [dico.index(bomb[0]), int(bomb[1])]
    if grilleB[bomb[0]][bomb[1]] != '':
        cercle('b',bomb[0],bomb[1])
        pvB -= 1
        if grilleB[bomb[0]][bomb[1]] == 'po':
            pvPO -= 1
        elif grilleB[bomb[0]][bomb[1]] == 'cr':
            pvCR -= 1
        elif grilleB[bomb[0]][bomb[1]] == 'co1':
            pvCO1 -= 1
        elif grilleB[bomb[0]][bomb[1]] == 'co2':
            pvCO2 -= 1
        else: pvTO -= 1
        checkCoule()
        checkWin()
    if partieEncours == False:
        break
    croix('b',bomb[0],bomb[1])
    
    bomb = position_random(liste)
    if grilleA[bomb[0]][bomb[1]] == 'x':
        cercle('a', bomb[0], bomb[1])
        pvA -= 1
        checkWin()
    if partieEncours == False:
        break
    croix('a', bomb[0], bomb[1])
    print(pvB)

done()