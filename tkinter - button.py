from tkinter import *


def display():
    label1.config(text="Button clicked!")


window = Tk()
window.title("GUI Button")

label1 = Label(window, text="Hello")
but = Button(window, text="Click Here", command=display)
but.pack()
label1.pack()
window.geometry("300x300")
window.mainloop()
