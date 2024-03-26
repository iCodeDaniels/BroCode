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

    #if messagebox.askretrycancel(title="Ask ok cancel",message="Do you want to retry?"):
        #print("REQUEST GRANTED")
    #else:
        #print("PASS REJECTED")

    #if messagebox.askyesno(title="Poiseii Demand",message="Are you fit for the test?"):
        #print("Please proceed")
    #else:
        #print("You're not eligible")

    #message = messagebox.askquestion(title="Asking Questions",message="Did you enjoy your stay here in Dubai?")
    #if message == "yes":
        #print("That's great. we love to see you soon")
    #else:
        #print("Give us your feedbacks and ratings please")

    message = messagebox.askyesnocancel(title="Yes no cancel",message="Do you like to code?",icon="error")
    if message == True:
        print("What's your favorite language")
    elif message == False:
        print("Try picking up HTML for a start")
    else:
        print("You skipped the question")

window = Tk()

button = Button(window,text='Click me',command=click)
button.pack()

window.mainloop()