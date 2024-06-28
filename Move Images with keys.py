from tkinter import *

def upwards(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)

window = Tk()
window.geometry("500x500")

window.bind("<w>",upwards)

photo = PhotoImage(file='coder.png')
window.iconphoto(True,photo)

photo = PhotoImage(file='coder.png')
label = Label(window,image=photo,bg="red")
label.place(x=0,y=0)

window.mainloop()