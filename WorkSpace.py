from tkinter import *
from tkinter import colorchooser

window = Tk()

window.geometry("300x350")
window.config(bg="cyan")

color_button = Button(window,text="Choose your color")
color_button.pack()

window.mainloop()