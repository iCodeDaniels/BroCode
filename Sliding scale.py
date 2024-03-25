from tkinter import *

def submit():
    print("The temperature is",sliding_scale.get(),"degrees C")
window = Tk()

sliding_scale = Scale(window,
                      from_=100,to=0,
                      font=("Comic Sans",15,"bold"),
                      length=400,
                      orient=VERTICAL,
                      tickinterval=10,
#                      showvalue=0,
                      troughcolor="black",
                      bg="purple",
                      fg="yellow")
sliding_scale.set(50)
sliding_scale.pack()

button = Button(window,text="submit",command=submit)
button.pack()

window.mainloop()