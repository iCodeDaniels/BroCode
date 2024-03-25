from tkinter import *

def click():
    print("You clicked the input button")

window = Tk()

tap = PhotoImage(file='button.png')
tap.config()
button = Button(window,text="Input",
                command=click,
                fg="blue",
                bg="black",
                activebackground="black",
                activeforeground="green",
                state=ACTIVE,
                image=tap,
                compound="bottom")
button.pack()
window.mainloop()