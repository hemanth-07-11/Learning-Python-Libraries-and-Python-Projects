
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Menu and Submenu")
root.geometry("500x500")

def func1():
    print(" Menu creation using Tkinter, Functions haven't been added yet")

def help():
    print("Help function !!!!")
    tmsg.showinfo("Help", "What help do u require")

def rate():
    print("Rate Us!")
    val = tmsg.askquestion("How was you experience", "Was your experience Good / Bad ?")
    if val == "yes":
        msg = "Great. Rate us on so and so platform!"

    else:
        msg = "Tell us what went wrong. we will call you soon."
    tmsg.showinfo("Experience", msg)


mainmenu = Menu(root)


m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New File", command=func1)
m1.add_command(label="Save", command=func1)
m1.add_separator()
m1.add_command(label="Save As", command=func1)
m1.add_command(label="Print", command=func1)
m1.add_command(label="Edit", command=func1)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)


m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Undo", command=func1)
m2.add_command(label="Redo", command=func1)
m2.add_separator()
m2.add_command(label="Cut", command=func1)
m2.add_command(label="Copy", command=func1)
m2.add_command(label="Paste", command=func1)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)


m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)

mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)
root.mainloop()
