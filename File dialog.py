from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfile()
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()

filebutton = Button(window,text="Open file",command=openfile)
filebutton.pack()

window.mainloop()