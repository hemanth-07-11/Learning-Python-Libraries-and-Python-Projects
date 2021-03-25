from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Work with Radio Button")
root.geometry("500x500")

def order():
    tmsg.showinfo("Response Received", f"We have received your response as '{var.get()}'.")

var = StringVar()
var.set("Radio")
Label(root, text="Which semester are u currently in?",
      justify=LEFT, padx=4, font="lucida 20 bold").pack()

radio = Radiobutton(root, text="Semester 1", padx=4, variable=var, value="Semester 1").pack(anchor="w")
radio = Radiobutton(root, text="Semester 2", padx=4, variable=var, value="Semester 2").pack(anchor="w")
radio = Radiobutton(root, text="Semester 3", padx=4, variable=var, value="Semester 3").pack(anchor="w")
radio = Radiobutton(root, text="Semester 4", padx=4, variable=var, value="Semester 4").pack(anchor="w")

Button(root, text="Submit", command=order).pack()
root.mainloop()
