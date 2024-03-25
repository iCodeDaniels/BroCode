from tkinter import *

def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You ordered:")

    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  font=("Times New Roman",25,"bold"),
                  relief=RAISED,
                  fg="Midnight blue",
                  bg="yellow",
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Hamburger")
listbox.insert(3,"Milky Doughnut")
listbox.insert(4,"Stir fry pasta")
listbox.insert(5,"Rice and lettuce")
listbox.insert(6,"Garlic bread")

listbox.config(height=listbox.size())

entrybox = Entry(window,
                 font=("Times New Roman",20,"bold"),
                 fg="midnight blue",
                 bg="yellow")
entrybox.pack()

add_button = Button(window,text="add",command=add)
add_button.pack()

submit_button = Button(window,text="Submit",command=submit)
submit_button.pack()

delete_button = Button(window,text="delete",command=delete)
delete_button.pack()

window.mainloop()