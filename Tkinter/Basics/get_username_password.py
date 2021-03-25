from tkinter import *

root = Tk()
root.title("Work with grids")
root.geometry("400x400")

def getvalues():
    print(f"Usearname: {uservalue.get()}")
    print(f"Password: {passvalue.get()}")

user = Label(text="username")
user.grid()

password = Label(text="password")
password.grid()

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable= uservalue)
passentry = Entry(root, textvariable= passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(root, command=getvalues, text="Button").grid()
root.mainloop()
