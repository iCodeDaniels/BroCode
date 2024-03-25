from tkinter import *

window = Tk()
window.geometry("420x425")
window.title("iCodeDaniel")

icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)

window.config(background="navy blue")

photo = PhotoImage(file='logo.png')
label = Label(window,
              text="Sawubona iCodeDaniel",
              font=('Arial',25,'bold'),
              foreground='sky blue',
              background='black',
              relief=RAISED,
              bd=6,
              padx=20,
              pady=10,
              image=photo,
              compound='bottom')
label.place(x=5,y=5)

button = Button(window,
                relief=RAISED,
                bd=6)
button.pack()

window.mainloop()