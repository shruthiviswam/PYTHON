from tkinter import *

root = Tk()


def display():
    print("Hello")


menubar = Menu(root)
menubar.add_command(label="New", command=display())
menubar.add_command(label="Quit", command=root.quit)
root.config(menu=menubar)
root.mainloop()
