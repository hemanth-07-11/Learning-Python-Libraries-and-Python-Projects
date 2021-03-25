from tkinter import *

root = Tk()

label = Label(root,text="Name")
label2 = Label(root,text="Password")
entry_1 =Entry(root)  
entry_2 = Entry(root)

label.grid(row=0)
label2.grid(row=1)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)      


root.mainloop()
