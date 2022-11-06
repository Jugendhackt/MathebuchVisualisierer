from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Draw import *
#Definiere variebeln

AktuelleFormeln = 0
MaximumFormeln=9
FarbenListe=["Black", "Blue", "Orange", "Green", "Red", "Purple", "Yellow", "Pink", "Brown"]
FunktionListe = [None, None, None,None,None,None,None,None, None]
BreiteCanvas=900
HoeheCanvas=590  
BreiteFenster=1000
HoeheFenster=600
#Funktion Knopf/Eingabe
def Knopfdruck():
    AktuelleFormeln =+0
    if  AktuelleFormeln <MaximumFormeln:
        Formel2 = eingabe.get()
        AktuellFarbe= FarbenListe[0]
        FarbenListe.insert(len(FarbenListe),FarbenListe.pop(0))
        F=Funktion(Formel2, farbe=AktuellFarbe)
        ZB.drawFunction(F.eval, colour=AktuellFarbe, start=float(eingabeStart.get()), step=float(eingabeStep.get()), end=float(eingabeStop.get()))
      
        Term=FunktionFrame(OptionFrame, F)
        for i in range(9): 
            if FunktionListe [i] is None:
                FunktionListe [i] = Term
                Term.index = i
                break
        
        AktuelleFormeln =+1
    else:
        messagebox.showerror(title="Fehler", message="Zu viele funktionen erstellt")


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
        self.index = 8
       
    def delete(self):
        AktuelleFormeln=+0
        if messagebox.askokcancel("Löschen", "Wirklich Löschen?"):
            self.FunktionKasten.pack_forget()
            self.FunktionKasten.destroy()
            AktuelleFormeln=AktuelleFormeln -1
            FunktionListe[self.index]=None
            ZB.reset()
            ZB.karo()
            ZB.coordinatesystem()
            for i in FunktionListe:
                if i is not None:
                    ZB.drawFunction(i.Funktion.eval, colour=i.Funktion.farbe, start=float(eingabeStart.get()), step=float(eingabeStep.get()), end=float(eingabeStop.get()))

            

    def AendereFunktion(self):
        self.AendereFenster= Tk() 
        self.Eingabe2 = Entry(self.AendereFenster)
        self.Eingabe2.pack()
        self.ButtonOk = Button(self.AendereFenster, text="Ok", command=self.destroy)
        self.ButtonOk.pack()
        self.AendereFenster.mainloop()

    def destroy(self):
        self.Funktion.term=self.Eingabe2.get()
        

        ZB.reset()
        ZB.karo()
        ZB.coordinatesystem()
        for i in FunktionListe:
                if i is not None:
                    ZB.drawFunction(i.Funktion.eval, colour=i.Funktion.farbe, start=float(eingabeStart.get()), step=float(eingabeStep.get()), end=float(eingabeStop.get()))

        self.Formel.config(text=self.Eingabe2.get())
        self.AendereFenster.destroy()

#Initialisiere fenster/canvas/Knopf
Fenster = Tk()
Fenster.title("Formelvisualisierer")
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
AktuelleFormeln=0
Knopf = Button(EingabeFrame, text="Zeichne!", command=Knopfdruck)
eingabe = Entry(EingabeFrame, font=("Arial",16))
eingabeStart = Entry(EingabeFrame, font=("Arial",16))
eingabeStop = Entry(EingabeFrame, font=("Arial",16))
eingabeStep = Entry(EingabeFrame, font=("Arial",16))
eingabe.insert(0, "Formel")
eingabeStart.insert(0, "Startwert")
eingabeStop.insert(0, "Endwert")
eingabeStep.insert(0, "Schrittweite")
eingabe.pack(side=LEFT, fill=X, expand=True)
eingabeStart.pack(side=LEFT,  expand=False)
eingabeStop.pack(side=LEFT,  expand=False)
eingabeStep.pack(side=LEFT,  expand=False)
Knopf.pack(side=RIGHT, fill=Y)
Grafik.pack(fill=BOTH, expand=True)
ZB=Zeichenbrett(Grafik)
ZB.reset()
ZB.karo()
ZB.coordinatesystem()

def resize(event):
    ZB.width = event.width
    ZB.height = event.height
    ZB.reset()
    ZB.karo()
    ZB.coordinatesystem()
    for i in FunktionListe:
                if i is not None:
                    ZB.drawFunction(i.Funktion.eval, colour=i.Funktion.farbe, start=float(eingabeStart.get()), step=float(eingabeStep.get()), end=float(eingabeStop.get()))

Grafik.bind('<Configure>', resize)




#Aktualisiere fenster
Fenster.mainloop()
