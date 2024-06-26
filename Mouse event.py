from tkinter import *

def processor(event):
    print("The mouse cordinates:",str(event.x),str(event.y))

window = Tk()

window.bind("<Button-1>",processor)
window.bind("<Button-3>",processor)
window.bind("<Leave>",processor)
window.bind("<Motion>",processor)

window.mainloop()