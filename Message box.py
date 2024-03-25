from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title="This is an info message box",message="You are welcome aboard here")
    #messagebox.showwarning(title="Death Trap", message="You are welcome aboard here")
    #messagebox.showerror(title="ERROR", message="Something went wrong")

    #if messagebox.askokcancel(title="Ask ok cancel",message="Do you want to proceed?"):
        #print("REQUEST GRANTED")
    #else:
        #print("REJECTED")

    if messagebox.askretrycancel(title="Ask ok cancel",message="Do you want to retry?"):
        print("REQUEST GRANTED")
    else:
        print("REJECTED")

window = Tk()

button = Button(window,text='Click me',command=click)
button.pack()

window.mainloop()