from tkinter import *

window = Tk()

frame = Frame(window,relief=SUNKEN,bd=5)
frame.pack()

Button(frame,text="S",width=5,relief=SUNKEN).pack(side=TOP)
Button(frame,text="W",width=5,relief=SUNKEN).pack(side=LEFT)
Button(frame,text="A",width=5,relief=SUNKEN).pack(side=LEFT)
Button(frame,text="D",width=5,relief=SUNKEN).pack(side=LEFT)

window.mainloop()