from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
#Definiere variebeln
BreiteCanvas=900
HoeheCanvas=590
BreiteFenster=1000
HoeheFenster=600
#Funktion Knopf/Eingabe
def Knopfdruck():
    Formel2 = eingabe.get()
    FunktionFrame(OptionFrame, Funktion(Formel2, farbe="Blue"))

class Funktion:
    def __init__(self, term, farbe="black"):
        self.farbe = farbe
        self.term=term
    def eval (self, x):
        return eval(self.term, locals={"x":x})

class FunktionFrame:
    def __init__(self, parent, Funktion, farbe="Green"):
        self.parent = parent
        self.Funktion = Funktion
        self.FunktionKasten= Frame(parent, bg=farbe,width=parent.winfo_width(), height=90, relief=SOLID, borderwidth=3)
        self.FunktionKasten.pack()
        self.FunktionKasten.pack_propagate(0)
        self.DeleteButton = Button(self.FunktionKasten, text="X", command=self.delete)
        self.DeleteButton.pack(anchor=NE)
        self.Formel = Label(self.FunktionKasten, text=self.Funktion.term, foreground=self.Funktion.farbe)
        self.Formel.pack(anchor=NW)
        self.EditButton = Button(self.FunktionKasten, text="Bearbeite", command=self.AendereFunktion)
        self.EditButton.pack(side=RIGHT)

       
    def delete(self):
        if messagebox.askokcancel("Löschen", "Wirklich Löschen?"):
            self.FunktionKasten.pack_forget()
            self.FunktionKasten.destroy()
    def AendereFunktion(self):
        self.AendereFenster= Tk() 
        self.Eingabe2 = Entry(self.AendereFenster)
        self.Eingabe2.pack()
        self.ButtonOk = Button(self.AendereFenster, text="Ok", command=self.destroy)
        self.ButtonOk.pack()
        self.AendereFenster.mainloop()
    def destroy(self):
        self.Aenderung=self.Eingabe2.get()
        str(self.Aenderung)
        self.Formel.config(text=self.Aenderung)
        self.AendereFenster.destroy()
#Initialisiere fenster/canvas/Knopf
Fenster = Tk()
Fenster.title("Mathebuchvisualisierer")
Fenster.config(width=HoeheFenster, height=BreiteFenster)

#Frames
OptionFrame = Frame(Fenster, width=200, bg="Blue", height=HoeheFenster)
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
