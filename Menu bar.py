from tkinter import *

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(window,)
menubar.add_cascade(label="Click to proceed",menu=fileMenu)

window.mainloop()