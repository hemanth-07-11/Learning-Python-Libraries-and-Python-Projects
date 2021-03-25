
from tkinter import *

root = Tk()
topFrame = Frame(root) 
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame,text="button1",fg="red")
button2 = Button(topFrame,text="button2",bg="black",fg="yellow")
button3 = Button(bottomFrame,text="button3",fg="blue")
button4 = Button(bottomFrame,text="button4",fg="black")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=RIGHT)
button4.pack(side=LEFT)
root.mainloop()
