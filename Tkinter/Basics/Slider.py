
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Slider - Tkinter")
root.geometry("500x500")

def getdollor():
    print(f"We have added {myslider2.get()} score to your energy pack")
    tmsg.showinfo("Energy Score added",f"We have added {myslider2.get()} score to your energy pack")


Label(root, text="How much energy score have you paid for ??").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=5)
myslider2.set(30) 
myslider2.pack()

Button(root, text="Get energy!", command=getdollor).pack()

root.mainloop()
