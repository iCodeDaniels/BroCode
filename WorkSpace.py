from tkinter import *

def display():
    if(x.get()==TRUE):
        print("You're valid and good to go")
    else:
        print("Passkey Invalid")

window = Tk()

photo = PhotoImage(file="coder.png")
x = BooleanVar()

checkbox = Checkbutton(window,
                       text="Proceed on the access",
                       variable=x,
                       onvalue=TRUE,
                       offvalue=FALSE,
                       command=display,
                       image=photo,
                       compound=LEFT)
checkbox.pack()

window.mainloop()