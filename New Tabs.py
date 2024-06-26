from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1,text="Jewelries Section")
notebook.add(tab2,text="Sunglasses Section")
notebook.pack(expand=True,fill="both")

Label(tab1,text="Luxury meets confident lifestyle",width=50,height=25).pack()
Label(tab2,text="Flawless skin needs to be protected",width=50,height=25).pack()

window.mainloop()