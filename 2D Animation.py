from tkinter import *
import time

WIDTH = 450
HEIGHT = 450

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

photo_image = PhotoImage(file='food2.png')
myimage = canvas.create_image(0,0,image=photo_image,anchor=NW)

while True:
    coordinates = canvas.coords((myimage))
    print(coordinates)
    window.update()
    time.sleep(0.01)

window.mainloop()