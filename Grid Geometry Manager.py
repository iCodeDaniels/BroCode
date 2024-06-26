from tkinter import *

window = Tk()

firstnameLabel = Label(window,text="First Name: ").grid(row=0,column=0)
firstnameEntry = Entry(window).grid(row=0,column=1)

lastnameLabel = Label(window,text="Last Name: ").grid(row=1,column=0)
lastnameEntry = Entry(window).grid(row=1,column=1)

emailLabel = Label(window,text="E-mail: ").grid(row=2,column=0)
emailEntry = Entry(window).grid(row=2,column=1)

submitbutton = Button(window,text="submit",width=10).grid(row=3,column=0,columnspan=2)

window.mainloop()