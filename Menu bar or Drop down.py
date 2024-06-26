from tkinter import *

def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You order for:")

    for index in food:
        print(index)
    print("is ready. Enjoy your")

window = Tk()

frame = Frame(window)
frame.pack()

listbox = Listbox(frame,font=("Bakerville Old Face",30,"bold italic"),selectmode=MULTIPLE)
listbox.pack(side=TOP)

listbox.insert(1,"Hamburger")
listbox.insert(2,"Pizza")
listbox.insert(3,"Shawarma")
listbox.insert(4,"Mayo Pasta")
listbox.insert(5,"Chic-Fil-A")
listbox.insert(6,"Macaroni")

listbox.config(height=listbox.size())

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Order Mode",menu=file_menu)

file_menu.add_command(label="Place order",command=submit,font=("Consolas",15,"italic"))
file_menu.add_command(label="Add Item",font=("Consolas",15,"italic"))
file_menu.add_command(label="Delete Item",font=("Consolas",15,"italic"))
file_menu.add_command(label="Entry box",font=("Consolas",15,"italic"))
file_menu.add_separator()
file_menu.add_command(label="Close",command=quit,font=("Consolas",15,"italic"))

customer_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Customer's corner",menu=customer_menu)

customer_menu.add_command(label="FAQs",command=submit,font=("Consolas",15,"italic"))
customer_menu.add_command(label="Feedback",font=("Consolas",15,"italic"))
customer_menu.add_command(label="Ratings",font=("Consolas",15,"italic"))
customer_menu.add_separator()
customer_menu.add_command(label="Close",font=("Consolas",15,"italic"),command=quit)

entrybox = Entry(frame,width=40)
entrybox.pack(side=LEFT)

window.mainloop()