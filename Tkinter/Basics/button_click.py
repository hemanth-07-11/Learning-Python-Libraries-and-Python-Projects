from tkinter import *
root = Tk()
def printName():
    print("This is Hemanth")
button1 = Button(root,text="Who is this?",command=printName)                                                                    
button1.pack()
root.mainloop()
