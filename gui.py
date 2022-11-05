from tkinter import *

#Definiere variebeln
BreiteCanvas=900
HoeheCanvas=590
BreiteFenster=1000
HoeheFenster=600
#Funktion Knopf
def Knopfdruck():
    Grafik.create_rectangle(20, 20 ,BreiteCanvas-20, HoeheCanvas-20)
#Initialisiere fenster/canvas/Knopf
Fenster = Tk()
Fenster.title("Mathebuchvisualisierer")
Fenster.config(width=HoeheFenster, height=BreiteFenster) 
Grafik = Canvas(Fenster, width=BreiteCanvas, height=HoeheCanvas)
Knopf = Button(Fenster, text="Zeichne!", command=Knopfdruck)
Knopf.place(y=HoeheFenster-40, x=BreiteFenster-220, width=120, height=30)
Grafik.pack()
Fenster.mainloop()
