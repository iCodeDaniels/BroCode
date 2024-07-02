from tkinter import *

def produce(event):
    label.config(text=event.keysym)
    print(x=event)

window = Tk()

window.bind("<Key>",produce)
label = Label(window,font=("Algerian",150))
label.pack()

window.mainloop()