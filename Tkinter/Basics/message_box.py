from tkinter import *
import tkinter.messagebox as tkMessageBox  #for python 3.x version import tkinter.messagebox


root = Tk()
tkMessageBox.showinfo('Window Title',"Message Box Sample")       

answer = tkMessageBox.askquestion('Cric Test',"Do u know about Virat Kohli")

if answer == 'yes':
    print("Nice")

root.mainloop()
