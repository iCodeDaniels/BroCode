from tkinter import *

def submit():
    print("Projected button")

def enter():
    input = entrybox.get()
    print("Welcome",input)

window = Tk()
window.title("Reassurance that everything is going to be better")
window.geometry("400x350")
window.config(background="Black")

icon = PhotoImage(file='coder.png')
window.iconphoto(True,icon)

label = Label(window,text="Please Proceed",
              font=("Times New Roman",32,"bold italic"),
              background="yellow",foreground="purple",
              relief=SUNKEN)
label.pack()

button = Button(window,text="Please Proceed",command=submit,
              font=("Times New Roman",20,"bold italic"),
              background="yellow",foreground="purple",
              relief=SUNKEN,activebackground="yellow",activeforeground="purple")
button.place(x=100,y=140)

entrybox = Entry(window,font=("Times New Roman",20,"bold italic"),
              background="yellow",foreground="purple",
              relief=SUNKEN,show="*")
entrybox.place(x=150,y=250)

entrybutton = Button(window,text="Submit",command=enter,
                     font=("Times New Roman",12,"bold italic"),
                     background="yellow",foreground="purple",
                     relief=SUNKEN,
                     activebackground="yellow",activeforeground="purple",)
entrybutton.place(x=450,y=250)

window.mainloop()