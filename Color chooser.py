from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    print(color)
    colorhex = color[1]
    print(colorhex)
    window.config(bg=colorhex)

window = Tk()
window.geometry("350x300")
window.config(bg="blue")
button = Button(window,text="Click me",command=click)
button.pack()

window.mainloop()