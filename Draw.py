print("Hallo Welt")

from tkinter  import*
top = Tk()
# Code to add widgets will go here...
canvas = Canvas(top,width = 500, height = 1000, bg="#FFFFFF")
canvas.pack()
x = 0
y = 0
xh = 250
yh = 500
while x<xh or y<yh:
    canvas.create_line(xh+x , 0, xh+x, 1000, fill="#aba9aa", width=1.5)
    canvas.create_line(xh-x , 0, xh-x, 1000, fill="#aba9aa", width=1.5)
    canvas.create_line(0 , yh+y, 1000, yh+y, fill="#aba9aa", width=1.5)
    canvas.create_line(0 , yh-y, 1000, yh-y, fill="#aba9aa", width=1.5)
    x = x + 20
    y = y + 20
    


top.mainloop()

