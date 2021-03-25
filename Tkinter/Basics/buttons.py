from tkinter import *

class hems:

    def __init__(self, master):  
        self.printmessage = []   

        frame = Frame(master)
        frame.pack()


        self.printButton = Button(frame, text="Print- Message", command=self.printmessage)
        self.printButton.pack(side=LEFT)


        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)


root = Tk()
a = hems(root)
root.mainloop()
