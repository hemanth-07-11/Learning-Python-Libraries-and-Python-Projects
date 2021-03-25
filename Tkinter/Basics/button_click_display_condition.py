from tkinter import * 
window = Tk()        

score = 1

def addToScore():
  message = txt.get()
  if message == "Hi" :
    lbl['text'] = "Hi"
  elif message == "Hello":
    lbl['text'] = "Hello"
  else:
    lbl['text'] = "Ok Bye"

lbl = Label(window, text=score, font=("Arial Bold", 25))
lbl.grid(column=0, row=0)

btn = Button(window, text="Click", command=addToScore)
btn.grid(column = 0 , row = 1)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)

window.mainloop()    


