from tkinter import *
def hems():
    print("HEMS")

root = Tk()
toolbar = Frame(root,bg="blue")
button_1 = Button(toolbar,text="Insert Img",command=hems)
button_1.pack(side=LEFT,padx=2,pady=2)
printbut = Button(toolbar,text="print HEMS",command=hems)
printbut.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)


root.mainloop()
