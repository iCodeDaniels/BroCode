from tkinter import *

window = Tk()

canvas = Canvas(window,width=400,height=400,bg="midnight blue")
canvas.create_line(0,0,400,400,fill="yellow",width=5)
canvas.create_line(0,400,400,0,fill="yellow",width=5)
canvas.create_rectangle(50,50,350,300,fill="sky blue")
canvas.pack()

window.mainloop()


window = Tk()

canvas = Canvas(window,width=400,height=400,bg="indigo")
canvas.create_line(0,0,400,400,fill="midnight blue",width=5)
canvas.create_line(0,400,400,0,fill="midnight blue",width=5)
canvas.create_rectangle(20,20,150,150,fill="violet")
canvas.pack()

window.mainloop()