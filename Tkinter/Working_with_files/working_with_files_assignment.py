from tkinter import *
import datetime
import os.path

class Application(Frame):
 
    def __init__(self, master=None):
        self.cur_file = "current.txt"
        self.col_file = "assignment.txt"
        self.date = datetime.datetime.now().strftime("%d.%m.%Y")
        self.list_date = ""
        
        Frame.__init__(self, master)
 
        Label(master, text="Assignment: ").grid(row=0, column=0)
        self.entry = Entry(master)
        self.entry.grid(row=0, column=1)
        Button(master, text="Add", command=self.add).grid(row=0, column=2)

        self.text = Text(master, width=40, state='disabled')
        self.text.grid(row=3, columnspan=3)
        
        self.scrollbar = Scrollbar(master)
        self.scrollbar.grid(row=3, column=2, sticky=E+N+S)
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        self.ldate = Label(master, text="Date of list: " + self.list_date)
        self.ldate.grid(row=4, columnspan=3)
        self.cdate = Label(master, text="Current date: " + self.date)
        self.cdate.grid(row=5, columnspan=3)

        Button(master, text="Commit day", command=self.commit).grid(row=6, column=1)

        self.load()
        

    def load(self):
        """Load currently active list"""
                                                            # Clear text to avoid double entries from reloading
        self.text.config(state='normal')
        self.text.delete('1.0', END)
        self.text.config(state='disabled')
        
        if  not os.path.exists(self.cur_file):
                                                            # If current list does not exist, create it with current date.
            f_out = open(self.cur_file, 'w')
            f_out.write(self.date + "\n")
            f_out.close()
            self.list_date = self.date
        else:
                                                             # Otherwise, load in existing list
            f_in = open(self.cur_file, 'r', encoding='utf-8')
            self.list_date = f_in.readline().strip('\n')
            for line in f_in:
                if not line == "\n":
                    self.text.config(state='normal')
                    self.text.insert(END, line)
                    self.text.config(state='disabled')
            f_in.close()
            

        self.ldate.config(text="Date of list: " + self.list_date)

    def add(self):
        """Add item to list and write it to the file."""
        if not self.entry.get().strip() == "":
            with open(self.cur_file, 'a', encoding='utf-8') as fh:
                fh.write(self.entry.get() + '\n')
            self.load()
            self.entry.delete(0, END)

    def commit(self):

        temp = []
        with open(self.cur_file, 'r', encoding='utf-8') as fh:
            temp = fh.readlines()

        with open(self.col_file, 'a', encoding='utf-8') as fh:
            fh.write('\n')
            for line in temp:
                fh.write(line)


        next_day = datetime.datetime.now() + datetime.timedelta(days=1)

        if not self.list_date == self.date:
            next_day = datetime.datetime.now()
        
        with open(self.cur_file, 'w', encoding='utf-8') as fh:
            fh.write(next_day.strftime("%d.%m.%Y"))
            fh.write('\n')
        self.load()


if __name__ == "__main__":
    root = Tk()
    root.title("Assignment List")
    app = Application(master=root)
    app.mainloop()
