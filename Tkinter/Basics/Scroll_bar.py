from tkinter import *

root = Tk()
root.title("SCROLL BAR")
root.geometry("500x500")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand = scrollbar.set)
for i in range(400):
    listbox.insert(END, f"ITEM {i}")
listbox.pack(fill="both")
scrollbar.config(command=listbox.yview)

root.mainloop()
