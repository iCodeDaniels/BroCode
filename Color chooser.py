from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    print(color)
    colorhex = color[1]
    print(colorhex)
window = Tk()
window.geometry("350x300")
button = Button(window,text="Click me",command=click)
button.pack()

window.mainloop()