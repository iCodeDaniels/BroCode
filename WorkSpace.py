from tkinter import *

def submit():
    if(x.get()==0):
        print("You ordered Pizza")

food = ["Pizza","Hamburger","Shawarma","Kebab","Pasta"]

window = Tk()

foodimage1 = PhotoImage(file="food1.png")
foodimage2 = PhotoImage(file="food2.png")
foodimage3 = PhotoImage(file="food3.png")
foodimage4 = PhotoImage(file="food2.png")
foodimage5 = PhotoImage(file="food1.png")
foodImage = [foodimage1,foodimage2,foodimage3,foodimage4,foodimage5]

x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],
                               variable=x,
                               value=index,
                               image=foodImage[index],
                               compound="left",
                               command=submit)
    radio_button.pack(anchor=W)

window.mainloop()