print("Hallo Welt")
import numpy as np
from tkinter  import*
top = Tk()
# Code to add widgets will go here...
canvas = Canvas(top,width = 1000, height = 1000, bg="#FFFFFF")
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

top.mainloop()

