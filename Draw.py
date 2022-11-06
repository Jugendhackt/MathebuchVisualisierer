print("Hallo Welt")
import numpy as np
import threading
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
        
        self.lock = threading.Lock()

        self.update()




    def update(self):
        self.lock.acquire()
        self.img = ImageTk.PhotoImage(self.content)
        self.canvas.itemconfig(self.container,image=self.img)
        self.canvas.update()
        self.canvas.update_idletasks()
        self.lock.release()

    
    def reset(self):
        self.lock.acquire()
        self.content=Image.new('RGB', (self.width,self.height))
        self.draw = ImageDraw.Draw(self.content)
        self.draw.rectangle([0,0,self.width,self.height],fill="white")
        self.lock.release()
        self.update()
        
    
    def karo(self):
        self.lock.acquire()
        x = 0
        y = 0
        xh = self.width/2
        yh = self.height/2
        while x<xh or y<yh:
            self.draw.line([xh+x , 0, xh+x, self.height], fill="#aba9aa", width=1)
            self.draw.line([xh-x , 0, xh-x, self.height], fill="#aba9aa", width=1)
            self.draw.line([0 , yh+y, self.width, yh+y], fill="#aba9aa", width=1)
            self.draw.line([0 , yh-y, self.width, yh-y], fill="#aba9aa", width=1)
            x = x + self.scale
            y = y + self.scale
        self.lock.release()
        self.update()

        

    def coordinatesystem(self):
        self.lock.acquire()
        xh=self.width/2
        yh=self.height/2

        self.draw.line([xh , 0, xh, self.height], fill="black", width=2)
        self.draw.line([0 , yh, self.width, yh], fill="black", width=2)
        self.draw.line([xh, 0, xh-10,self.scale], fill="black", width=2)
        self.draw.line([ xh, 0, xh+10, self.scale], fill="black", width=2)
        self.draw.line([self.width , yh, self.width-10, yh+10], fill="black", width=2) 
        self.draw.line([self.width , yh, self.width-10, yh-10], fill="black", width=2)

        bx=self.scale*2
        by=self.scale*2
        while bx<self.width or by<self.height:
            self.draw.line([xh+bx, yh+10, xh+bx, yh-10], fill="black", width=2)
            self.draw.line([xh-bx, yh+10, xh-bx, yh-10], fill="black", width=2)
            self.draw.line([xh+10, yh+by, xh-10, yh+by], fill="black", width=2)
            self.draw.line([xh+10, yh-by, xh-10, yh-by], fill="black", width=2)
            bx = bx+self.scale*2
            by = by+self.scale*2

        x = 0
        n = 0
        while x<self.width:
            self.draw.text((xh+x,yh+15),str(0+n), fill="black")
            self.draw.text((xh-x,yh+15),str(0-n), fill="black")
            self.draw.text((xh-20,yh+x),str(0-n), fill="black")
            self.draw.text((xh-20,yh-x),str(0+n), fill="black")
            x = x+40
            n = n+2
        self.lock.release()
        
        self.update()

    

    def drawFunction(self, f, start, end, step, colour):
        self.lock.acquire()
        xh=self.width/2
        yh=self.height/2


        sample = np.arange(start,end+step,step)
        for i in range(1,len(sample)):
            coor1 = xh+sample[i-1]*self.scale, yh-f(sample[i-1])*self.scale
            coor2 = xh+sample[i]*self.scale, yh-f(sample[i])*self.scale
            self.draw.line([coor1, coor2], fill=colour, width=3)
        self.lock.release()
        self.update()



class Funktion:
    def __init__(self, term, farbe="black"):
        self.farbe = farbe
        self.term=term
    def eval (self, x):
        return eval(self.term)


