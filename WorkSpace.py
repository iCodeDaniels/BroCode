from tkinter import *

def dragevent(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def dragmotion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

window = Tk()

label = Label(window,width=10,height=5,bg="purple",fg="yellow",text="Heyo Brother!")
label.place(x=0,y=0)

label2 = Label(window,width=10,height=5,bg="yellow",fg="purple",text="Heyo Brother!")
label2.place(x=100,y=100)

label.bind("<Button-1>",dragevent)
label.bind("<B1-Motion>",dragmotion)

label2.bind("<Button-1>",dragevent)
label2.bind("<B1-Motion>",dragmotion)

window.mainloop()