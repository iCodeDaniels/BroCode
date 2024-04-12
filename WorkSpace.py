from tkinter import *
from tkinter import messagebox

def proceed():
    #messagebox.showinfo(title="Regulated Questions",message="This is a step to me becoming a great software developer")
    #messagebox.showwarning(title="Really risky on this",message="This is really a bad choice to make")
    messagebox.showerror(title="Error calling message",message="There's an error with the processed data")

window = Tk()

photo = PhotoImage(file='coder.png')
window.iconphoto(True,photo)

button = Button(window,text="Click me",command=proceed)
button.pack()

window.mainloop()