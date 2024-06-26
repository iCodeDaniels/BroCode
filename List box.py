from tkinter import *
def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You order for:")

    for index in food:
        print(index)
    print("has been confirmed")
def add():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height=listbox.size())
def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

window = Tk()

window.config(bg="purple")

listbox = Listbox(window,bg="purple",fg="yellow",font=("Algerian",15,"bold"),selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Hamburger")
listbox.insert(3,"Milky Doughnut")
listbox.insert(4,"Stir fry pasta")
listbox.insert(5,"Rice and lettuce")
listbox.insert(6,"Garlic bread")

listbox.config(height=listbox.size())

entry = Entry(window,font=("Comic Sans",10))
entry.pack()

submit_button = Button(window,text="submit",command=submit)
submit_button.place(x=60,y=165)

add_button = Button(window,text="add",command=add)
add_button.place(x=130,y=165)

delete_button = Button(window,text="delete",command=delete)
delete_button.place(x=185,y=165)

window.mainloop()