from tkinter import *

def submit():
    input = entry.get()
    print("Hello dear",input)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,font=("Times New Roman",35,"italic"),show="*")

entry.pack(side=LEFT)

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=LEFT)

delete_button = Button(window,text="delete",command=delete)
delete_button.pack(side=LEFT)

backspace_button = Button(window,text="backspace",command=backspace)
backspace_button.pack(side=LEFT)

window.mainloop()