from tkinter import *

def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()
text = Text(window,bg="light yellow",fg="purple",font=("Ink free",20,"italic"),height=8,width=20)
text.pack()

submit_button = Button(window,text="Submit",command=submit)
submit_button.pack()

window.mainloop()