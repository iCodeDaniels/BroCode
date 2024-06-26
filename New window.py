from tkinter import *

def create():
    

    new_window = Tk()

    old_window.destroy()

old_window = Tk()

button = Button(old_window,text="Creating new Windows",command=create)
button.pack()
old_window.mainloop()