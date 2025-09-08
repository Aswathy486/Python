from tkinter import *
from time import strftime

root = Tk()
root.title("Clock")

def update():
    lbl.config(text=f"{strftime('%H:%M:%S')}\n{strftime('%Y-%m-%d')}")
    lbl.after(1000, update)

lbl = Label(root, font=('Arial', 40))
lbl.pack()

update()
root.mainloop()
