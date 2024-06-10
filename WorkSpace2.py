from tkinter import *

food = ["Shawarma","Kebab","Pasta","Cereals","Mayo Pastries"]
def order():
    if(x.get()==0):
        print("You ordered",food[0])
    elif(x.get()==1):
        print("You ordered",food[1])
    elif (x.get() == 2):
        print("You ordered", food[2])
    elif (x.get() == 3):
        print("You ordered", food[3])
    elif (x.get() == 4):
        print("You ordered", food[4])


window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,text=food[index],
                              variable=x,
                              bg="violet",
                              value=index,
                              command=order)
    radiobutton.pack(anchor=W)

window.mainloop()