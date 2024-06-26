from tkinter import *

def process(event):
    #print("You did a thing",event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>",process)

label = Label(window,font=("Times New Roman",50))
label.pack()

window.mainloop()