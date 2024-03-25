from tkinter import *

food = ["Pizza","Hamburger","Shawarma","Kebab","Pasta"]

def order():
    if(x.get()==0):
        print("You ordered Pizza")
    elif(x.get()==1):
        print("You ordered a Hamburger")
    elif(x.get()==2):
        print("You ordered Shawarma")
    elif (x.get() == 3):
        print("You ordered a Kebab")
    elif (x.get() == 4):
        print("You ordered Pasta")
    else:
        print("There's an invalid input")

window = Tk()

foodimage1 = PhotoImage(file="food1.png")
foodimage2 = PhotoImage(file="food2.png")
foodimage3 = PhotoImage(file="food3.png")
foodimage4 = PhotoImage(file="food2.png")
foodimage5 = PhotoImage(file="food1.png")
foodImage = [foodimage1,foodimage2,foodimage3,foodimage4,foodimage5]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              image=foodImage[index],
                              compound="left",
                              command=order,
                              bg="violet")
    radiobutton.pack(anchor=W)
window.mainloop()