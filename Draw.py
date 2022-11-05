print("Hallo Welt")
import numpy as np
from tkinter  import*

# Code to add widgets will go here...
from PIL import Image, ImageTk, ImageDraw

class Zeichenbrett:
    def __init__(self,canvas):
        canvas.update()
        self.content=Image.new('RGB', (canvas.winfo_width(),canvas.winfo_height()))
        self.draw = ImageDraw.Draw(self.content)
        
        self.width = canvas.winfo_width()
        self.height = canvas.winfo_height()
        self.canvas = canvas
        self.scale = 20
        
        self.img = ImageTk.PhotoImage(self.content)
        self.container = canvas.create_image(0, 0, image=self.img, anchor=NW)



    def update(self):
        self.img = ImageTk.PhotoImage(self.content)
        self.canvas.itemconfig(self.container,image=self.img)
    
    def reset(self):
        pass
    
    def karo(self):
        pass

    def coordinatesystem(self):
        pass

    

    def drawFunction(self, f, start, end, step, colour):
        pass


class Funktion:
    def __init__(self, term, farbe="black"):
        self.farbe = farbe
        self.term=term
    def eval (self, x):
        return eval(self.term, locals={"x":x})


