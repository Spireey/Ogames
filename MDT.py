from tkinter import*
import webbrowser
webbrowser.open("https://youtu.be/khjXfnxMEig")
f = Tk()
f.title("Maître du temps")
f.geometry("900x800")
f.config(background='#666666')

b = Button(f, text = "Démarrer", font=("Courrier", 20), bg='#666666',fg='white',)
b.place(x = 319, y = 400, anchor=('n'))

a = Button(f, text = "Arrêter", font=("Courrier", 20), bg='#666666',fg='white',)
a.place(x = 596, y = 400, anchor=('n'))

fr = Frame(f, bg = 'white', height = 55, width = 400)
fr.place(x = 450, y = 400, anchor=('s'))
f.destroy()





