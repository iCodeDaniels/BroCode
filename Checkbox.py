from tkinter import *

def display():
    if(x.get()==1):
        print("You agree")
    else:
        print("I disagree")

window = Tk()

x = IntVar()

checkbox_button = Checkbutton(window,text="I agree on this",
                              variable=x,
                              onvalue=1,
                              offvalue=0,
                              command=display)
checkbox_button.pack()

window.mainloop()