from tkinter import *

#Definiere variebeln
BreiteCanvas=900
HoeheCanvas=590
BreiteFenster=1000
HoeheFenster=600
#Funktion Knopf/Eingabe
def Knopfdruck():
    Grafik.create_rectangle(20, 20 ,BreiteCanvas-20, HoeheCanvas-40)


#Initialisiere fenster/canvas/Knopf
Fenster = Tk()
Fenster.title("Mathebuchvisualisierer")
Fenster.config(width=HoeheFenster, height=BreiteFenster)

#Frames
OptionFrame = Frame(Fenster, width=100, bg="Blue", height=HoeheFenster)
OptionFrame.pack(side=LEFT, fill=Y, expand=False)
CanvasFrame = Frame(Fenster, width=BreiteFenster-100, bg="Red", height=HoeheFenster-40)
CanvasFrame.pack(anchor=NE, fill=BOTH, expand=True)
EingabeFrame = Frame(Fenster, width=BreiteFenster-100, height=40, bg="green")
EingabeFrame.pack(side=BOTTOM, fill=X, expand=False)


#Knopf und eingabe
Grafik = Canvas(Fenster, width=BreiteCanvas, height=HoeheCanvas)
Knopf = Button(Fenster, text="Zeichne!", command=Knopfdruck)
eingabe = Entry(Fenster, width=60, font=("Arial",16))
eingabe.place(x=25, y=560)
Knopf.pack()
Grafik.pack()

#Aktualisiere fenster
Fenster.mainloop()
