from tkinter import *
from tkinter.ttk import *
import time

def download():
    print()

window = Tk()

bar = Progressbar(window,orient=HORIZONTAL,length=350
                  )
bar.pack()

button = Button(window,text="Download",command=download)
button.pack()

window.mainloop()