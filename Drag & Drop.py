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

label = Label(window,font=("Algerian",15,"italic"),
              fg="Purple",bg="Yellow",
              text="Heyo! Brody",
              width=13,height=5)
label.place(x=0,y=0)

label2 = Label(window,font=("Algerian",15,"italic"),
              fg="Yellow",bg="Purple",
              text="Gotcha",
              width=13,height=5)
label2.place(x=150,y=150)

label.bind("<Button-1>",dragevent)
label.bind("<B1-Motion>",dragmotion)

label2.bind("<Button-1>",dragevent)
label2.bind("<B1-Motion>",dragmotion)

window.mainloop()