from tkinter import *

def order():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("Your order for:")

    for index in food:
        print(index)
    print("is ready. Enjoy yourself")

def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

window = Tk()

frame = Frame(window,bd=5,relief=SUNKEN)
frame.pack(side=TOP)

window.config(background="midnight blue")

listbox = Listbox(frame,font=("Baskerville",25,"bold italic"),
                  selectmode=MULTIPLE,
                  background="midnight blue",
                  foreground="cyan")
listbox.pack()

listbox.insert(1,"Macaroni")
listbox.insert(2,"Pepperoni Pizza")
listbox.insert(3,"Shawarma")
listbox.insert(4,"Rice & Chicken")
listbox.insert(5,"Mayo Pasta")
listbox.insert(6,"Chic-Fil-A")
listbox.insert(7,"HotDog")
listbox.insert(8,"Sandwich")
listbox.insert(9,"Sushi")

listbox.config(height=listbox.size())

menu_bar = Menu(frame)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar,tearoff=0,
                  background="midnight blue",
                  foreground="cyan")
menu_bar.add_cascade(label="Mode of Payment",menu=file_menu)

file_menu.add_command(label="Order mode",font=("Baskerville",10,"bold italic"),command=order)
file_menu.add_command(label="Add Item",font=("Baskerville",10,"bold italic"),command=add)
file_menu.add_command(label="Delete Item",font=("Baskerville",10,"bold italic"),command=delete)
file_menu.add_separator()
file_menu.add_command(label="Close",font=("Baskerville",10,"bold italic"),command=quit)

entrybox = Entry(frame,font=("Baskerville",15,"bold italic"),
                 width=32,
                 background="midnight blue",
                 foreground="cyan",)
entrybox.pack()

window.mainloop()