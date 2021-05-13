

from turtle import *
import time





title("Puissance 4")
setup(900,800)
ht()
speed('fastest')
width(5)
up()
onTurn = 'red'

goto(-323,-370)
write('A',font=("Arial", 50))

goto(-223,-370)
write('Z',font=("Arial", 50))

goto(-123,-370)
write('E',font=("Arial", 50))

goto(-23,-370)
write('R',font=("Arial", 50))

goto(77,-370)
write('T',font=("Arial", 50))

goto(177,-370)
write('Y',font=("Arial", 50))

goto(277,-370)
write('U',font=("Arial", 50))



for y in range(6):
    for x in range(7):
        goto(-302.5 + 100*x,-290 + 100*y)
        down()
        circle(42.5)
        up()

grille = [['','','','','',''],
          ['','','','','',''],
          ['','','','','',''],
          ['','','','','',''],
          ['','','','','',''],
          ['','','','','',''],
          ['','','','','','']]

etatColonne = [0,0,0,0,0,0,0]

def Jeton0():
    global onTurn
    global etatColonne
    global grille
    global changeTurnCheck
    if etatColonne[0] < 6:
        goto(-302.5,-247.5 + 100*etatColonne[0])
        dot(80,onTurn)
        grille[0].insert(etatColonne[0],onTurn)
        etatColonne[0] += 1
        changeTurnCheck()

def Jeton1():
    global onTurn
    global etatColonne
    global grille
    global changeTurnCheck
    if etatColonne[1] < 6:
        goto(-202.5,-247.5 + 100*etatColonne[1])
        dot(80,onTurn)
        grille[1].insert(etatColonne[1],onTurn)
        etatColonne[1] += 1
        changeTurnCheck()

def Jeton2():
    global onTurn
    global etatColonne
    global grille
    global changeTurnCheck
    if etatColonne[2] < 6:
        goto(-102.5,-247.5 + 100*etatColonne[2])
        dot(80,onTurn)
        grille[2].insert(etatColonne[2],onTurn)
        etatColonne[2] += 1
        changeTurnCheck()

def Jeton3():
    global onTurn
    global etatColonne
    global grille
    global changeTurnCheck
    if etatColonne[3] < 6:
        goto(-2.5,-247.5 + 100*etatColonne[3])
        dot(80,onTurn)
        grille[3].insert(etatColonne[3],onTurn)
        etatColonne[3] += 1
        changeTurnCheck()

def Jeton4():
    global onTurn
    global etatColonne
    global grille
    global changeTurnCheck
    if etatColonne[4] < 6:
        goto(97.5,-247.5 + 100*etatColonne[4])
        dot(80,onTurn)
        grille[4].insert(etatColonne[4],onTurn)
        etatColonne[4] += 1
        changeTurnCheck()

def Jeton5():
    global onTurn
    global etatColonne
    global grille
    global changeTurnCheck
    if etatColonne[5] < 6:
        goto(197.5,-247.5 + 100*etatColonne[5])
        dot(80,onTurn)
        grille[5].insert(etatColonne[5],onTurn)
        etatColonne[5] += 1
        changeTurnCheck()

def Jeton6():
    global onTurn
    global etatColonne
    global grille
    global changeTurnCheck
    if etatColonne[6] < 6:
        goto(297.5,-247.5 + 100*etatColonne[6])
        dot(80,onTurn)
        grille[6].insert(etatColonne[6],onTurn)
        etatColonne[6] += 1
        changeTurnCheck()

        
 # ECRAN DE FIN____________________________________________________
def win(winner):
    clear()
    if winner == 'red':
        for loop in range(5):
            goto(0,0)
            write(' Les rouges gagnent!',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('Les rouges gagnent! ',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('es rouges gagnent! L',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('s rouges gagnent! Le',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write(' rouges gagnent! Les',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('rouges gagnent! Les ',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('ouges gagnent! Les r',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('uges gagnent! Les ro',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('ges gagnent! Les rou',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('es gagnent! Les roug',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('s gagnent! Les rouge',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write(' gagnent! Les rouges',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('gagnent! Les rouges ',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('agnent! Les rouges g',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('gnent! Les rouges ga',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('nent! Les rouges gag',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('ent! Les rouges gagn',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('nt! Les rouges gagne',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('t! Les rouges gagnen',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('! Les rouges gagnent',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write(' Les rouges gagnent!',align="center",font=("Arial", 50))
            
                     
            
    else:
        for loop in range(5):
            goto(0,0)
            write(' Les jaunes gagnent!',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('Les jaunes gagnent! ',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('es jaunes gagnent! L',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('s jaunes gagnent! Le',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write(' jaunes gagnent! Les',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('jaunes gagnent! Les ',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('aunes gagnent! Les j',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('unes gagnent! Les ja',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('nes gagnent! Les jau',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('es gagnent! Les jaun',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('s gagnent! Les jaune',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write(' gagnent! Les jaunes',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('gagnent! Les jaunes ',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('agnent! Les jaunes g',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('gnent! Les jaunes ga',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('nent! Les jaunes gag',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('ent! Les jaunes gagn',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('nt! Les jaunes gagne',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('t! Les jaunes gagnen',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write('! Les jaunes gagnent',align="center",font=("Arial", 50))
            time.sleep(0.05)
            clear()
            write(' Les jaunes gagnent!',align="center",font=("Arial", 50))
 #_________________________________________________________________

            
def changeTurnCheck():
    global win
    for i in range(7):
        for j in range(3):
            if (grille[i][j] == grille[i][j+1] and grille[i][j+1] == grille[i][j+2] and grille[i][j+2] == grille[i][j+3]) and (grille[i][j] == 'red' or grille[i][j] == 'yellow'):
                win(grille[i][j])
    for i in range(6):
        for j in range(4):
            if (grille[j][i] == grille[j+1][i] and grille[j+1][i] == grille[j+2][i] and grille[j+2][i] == grille[j+3][i]) and (grille[j][i] == 'red' or grille[j][i] == 'yellow'):
                win(grille[j][i])
    for i in range(4):
        for j in range(3):
            if (grille[i][j] == grille[i+1][j+1] and grille[i+1][j+1] == grille[i+2][j+2] and grille[i+2][j+2] == grille[i+3][j+3]) and (grille[i][j] == 'red' or grille[i][j] == 'yellow'):
                win(grille[i][j])
    for i in range(4):
        for j in range(3):
            if (grille[i+3][j] == grille[i+2][j+1] and grille[i+2][j+1] == grille[i+1][j+2] and grille[i+1][j+2] == grille[i][j+3]) and (grille[i+3][j] == 'red' or grille[i+3][j] == 'yellow'):
                win(grille[i+3][j])
    if sum(etatColonne) == 42:
        clear()
    global onTurn
    if onTurn == 'red':
        onTurn = 'yellow'
    else: onTurn = 'red'

listen()
onkeypress(Jeton0, 'a')
onkeypress(Jeton1, 'z')
onkeypress(Jeton2, 'e')
onkeypress(Jeton3, 'r')
onkeypress(Jeton4, 't')
onkeypress(Jeton5, 'y')
onkeypress(Jeton6, 'u')
done()
