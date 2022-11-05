print("Hallo Welt")
import numpy as np
from tkinter  import*
import threading
top = Tk()
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

        

    def coordinatesystem(self, xmax, xmin, ymax, ymin):
        self.lock.acquire()
        xh=self.width/2
        yh=self.height/2
        canvas.create_line(xh , 0, xh, self.height, fill="black", width=2)
        canvas.create_line(0 , yh, self.width, yh, fill="black", width=2)
        canvas.create_line(xh, 0, xh-10,self.scale, fill="black", width=2)
        canvas.create_line( xh, 0, xh+10, self.scale, fill="black", width=2)
        canvas.create_line(self.width , yh, self.width-10, yh+10, fill="black", width=2)
        
        canvas.create_line(self.width , yh, self.width+self.scale, yh-10, fill="black", width=2)

        bx=self.scale*2
        by=self.scale*2
        while bx<self.width or by<self.height:
            canvas.create_line(xh+bx, yh+10, xh+bx, yh-10, fill="black", width=2)
            canvas.create_line(xh-bx, yh+10, xh-bx, yh-10, fill="black", width=2)
            canvas.create_line(xh+10, yh+by, xh-10, yh+by, fill="black", width=2)
            canvas.create_line(xh+10, yh-by, xh-10, yh-by, fill="black", width=2)
            bx = bx+self.scale*2
            by = by+self.scale*2

        x = 0
        n = 0
        while x<self.width:
            canvas.create_text(xh+x,yh+15,text=str(0+n))
            canvas.create_text(xh-x,yh+15,text=str(0-n))
            canvas.create_text(xh-20,yh+x,text=str(0-n))
            canvas.create_text(xh-20,yh-x,text=str(0+n))
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
            canvas.create_line(coor1, coor2, fill=colour, width=2)
        self.lock.release()
        self.update()

canvas = Canvas(top,width = 1200, height = 1000, bg="#FFFFFF")
canvas.pack()

def Karo(canvas):
    x = 0
    y = 0
    xh = 500
    yh = 500
    while x<xh or y<yh:
        canvas.create_line(xh+x , 0, xh+x, 1000, fill="#aba9aa", width=1)
        canvas.create_line(xh-x , 0, xh-x, 1000, fill="#aba9aa", width=1)
        canvas.create_line(0 , yh+y, 1000, yh+y, fill="#aba9aa", width=1)
        canvas.create_line(0 , yh-y, 1000, yh-y, fill="#aba9aa", width=1)
        x = x + 20
        y = y + 20

def Koordinatensystem(canvas):
    xh=500
    yh=500
    canvas.create_line(xh , 0, xh, 1000, fill="black", width=2)
    canvas.create_line(0 , yh, 1000, yh, fill="black", width=2)
    canvas.create_line(xh, 0, 490, 20, fill="black", width=2)
    canvas.create_line( xh, 0, 510, 20, fill="black", width=2)
    canvas.create_line(1000 , yh, 980, 510, fill="black", width=2)
    canvas.create_line(1000 , yh, 980, 490, fill="black", width=2)

    bx=40
    by=40
    while bx<1000 or by<1000:
        canvas.create_line(xh+bx, yh+10, xh+bx, yh-10, fill="black", width=2)
        canvas.create_line(xh-bx, yh+10, xh-bx, yh-10, fill="black", width=2)
        canvas.create_line(xh+10, yh+by, xh-10, yh+by, fill="black", width=2)
        canvas.create_line(xh+10, yh-by, xh-10, yh-by, fill="black", width=2)
        bx = bx+40
        by = by+40

    x = 0
    n = 0
    while x<1000:
        canvas.create_text(xh+x,yh+15,text=str(0+n))
        canvas.create_text(xh-x,yh+15,text=str(0-n))
        canvas.create_text(xh-20,yh+x,text=str(0-n))
        canvas.create_text(xh-20,yh-x,text=str(0+n))
        x = x+40
        n = n+2
        

def Graphzeichnen(canvas):
    xh=500
    yh=500
    def f(x):
        return x


    sample = np.arange(-1000,1000,0.5)
    for i in range(1,len(sample)):
        coor1 = xh+sample[i-1]*20, yh-f(sample[i-1])*20
        coor2 = xh+sample[i]*20, yh-f(sample[i])*20
        canvas.create_line(coor1, coor2, fill="black", width=2)


def Kreis(canvas):
    xh=500
    yh=500
    canvas.create_oval ( xh+50, yh+50, xh-50, yh-50, width=2)

Karo(canvas)
Koordinatensystem(canvas)
Graphzeichnen(canvas)
Kreis(canvas)

zb=Zeichenbrett(canvas)
zb.reset()
zb.karo()
zb.coordinatesystem(10, -10, 7, -6)
zb.drawFunction(lambda x: x*x+x*x*x, -5, 5, 0.1, "blue")
top.mainloop()

