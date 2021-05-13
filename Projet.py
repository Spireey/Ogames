from tkinter import *
from turtle import*
import subprocess
import time
import webbrowser



def P4():
    exec(open("Puissance4.py").read())
    
def MDT():
    exec(open("MDT.py").read())


def destroy():
    fenetre.destroy()

def BT():
    exec(open("Bataille Navale.py").read())
    


def crédits():
    fcrédits = Tk()
    fcrédits.title("Crédits")
    fcrédits.geometry("800x100")
    fcrédits.config(background ='#666666')
    label_title = Label(fcrédits, text="Designer d'interface : OISON Clément", font=("Courrier", 30), bg='#666666',fg='white')
    label_title.pack()
    label_title2 = Label(fcrédits, text="Développeurs : OISON Clément & Valentin", font=("Courrier", 30), bg='#666666',fg='white')
    label_title2.pack()


fenetre = Tk()


fenetre.title("Ogames")
#732
fenetre.geometry("1024x735")
fenetre.config(background='#666666')
bg = PhotoImage(file="vraie.gif")
Labelimg = Label(fenetre, image=bg)
Labelimg.place(x=0, y=0)
label_title = Label(Labelimg, text="Bienvenue sur Ogames", font=("Eras", 40), bg='#666666',fg='white')
label_title.place(x=235,y=0)


imgp4 = PhotoImage(file ="p4.png")

BPuissance4 = Button(fenetre, image = imgp4, font=("Courrier", 20), bg='#666666',fg='white', command = P4)
BPuissance4.place(x=459,y=200)

img = PhotoImage(file ="a.png")

BBatailleNavale = Button(fenetre, image=img,  font=("Courrier", 20), bg='#666666',fg='white', command = BT)
BBatailleNavale.place(x=459,y=370)


imgmdt = PhotoImage(file ="mdt.png")

BMDT = Button(fenetre, image = imgmdt,  font=("Courrier", 20), bg='#666666',fg='white', command = MDT)
BMDT.place(x=459,y=540)


BCrédits = Button(fenetre, text="Crédits",  font=("Courrier", 20), bg='#666666',fg='white', command = crédits)
BCrédits.place(x="10",y="670")

Bdestroy = Button(fenetre, text="Fermer", font=("Courrier", 20), bg='#666666', fg='white', command = destroy)
Bdestroy.place(x="905",y="670")


fenetre.mainloop()



