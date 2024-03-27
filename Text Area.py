from tkinter import *
def submit():
    input = text_area.get(1.0, END)
    print(input)

window = Tk()

text_area = Text(window,
                 bg="light yellow",fg="midnight blue",
                 font=("Times New Roman",25),
                 height=10,
                 width=25,
                 bd=6,
                 relief=SUNKEN)
text_area.pack()

text_button = Button(window,text="Submit",command=submit,font=("Times New Roman",10,"bold italic"))
text_button.pack()

window.mainloop()