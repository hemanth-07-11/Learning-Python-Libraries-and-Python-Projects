import tkinter as tk
import webbrowser

root = tk.Tk()
root.geometry("430x130")
root.title("Search Bar")

query = tk.StringVar()

def open(text):
    if text == "google":
        url = "https://google.co.in/search?q="
        webbrowser.open_new_tab(url+query.get())
        
    if text == "bing":
        url="https://www.bing.com/search?q="
        webbrowser.open_new_tab(url+query.get())

    if text == "youtube":
        url="https://www.youtube.com/results?search_query="
        webbrowser.open_new_tab(url+query.get())

    if text== "amazon":
        url="https://www.amazon.com/s?k="
        webbrowser.open_new_tab(url+query.get())


google = tk.Button(root, text="Google", command=lambda:open("google"), width = 10)
google.place(x = 20, y = 80)

bing = tk.Button(root, text="Bing", command=lambda : open("bing"), width = 10)
bing.place(x = 120, y = 80)

youtube = tk.Button(root, text="Youtube", command=lambda : open("youtube"), width = 10)
youtube.place(x = 220, y = 80)

amazon = tk.Button(root, text="Amazon", command=lambda : open("amazon"), width = 10)
amazon.place(x = 320, y = 80)

label1 = tk.Label(root, text="Search")
label1.place(x = 20, y = 20)

entry = tk.Entry(root, width = 34, textvariable = query, font = (20))
entry.place(x = 20, y = 40)

root.mainloop()
