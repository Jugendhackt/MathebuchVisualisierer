from tkinter import *

#Definiere variebeln
BreiteCanvas=900
HoeheCanvas=590
BreiteFenster=1000
HoeheFenster=600
#Funktion Knopf/Eingabe
def Knopfdruck():
    Grafik.create_rectangle(20, 20 ,BreiteCanvas-20, HoeheCanvas-40)

class Funktion:
    def __init__(self, term, farbe="black"):
        self.farbe = farbe
        self.term=term
    def eval (self, x):
        return eval(self.term, locals={"x":x})
         
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
Fenster.update()

Grafik = Canvas(CanvasFrame, width=CanvasFrame.winfo_width(), height=CanvasFrame.winfo_height())

Knopf = Button(EingabeFrame, text="Zeichne!", command=Knopfdruck)
eingabe = Entry(EingabeFrame, font=("Arial",16))
eingabe.pack(side=LEFT, fill=X, expand=True)
Knopf.pack(side=RIGHT, fill=Y)
Grafik.pack(fill=BOTH, expand=True)

#Aktualisiere fenster
Fenster.mainloop()
