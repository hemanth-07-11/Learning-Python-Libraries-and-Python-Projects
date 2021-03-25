from tkinter import *
from tkinter.messagebox import Message
from math import pi, e, tau

class Calculator:

    def __init__(self):

        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry('')

        self.display = Entry(self.root,width = 60, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.button_0 = Button(self.root, text="0", padx=40, pady=20, font=5, bg="#ff7859", fg="black",command=lambda:self.add_to_expression("0")).grid(row=4, column=0)
        self.button_1 = Button(self.root, text="1", padx=40, pady=20, font=5,bg="#ff7859", fg="black", command=lambda:self.add_to_expression("1")).grid(row=3, column=0)
        self.button_2 = Button(self.root, text="2", padx=40, pady=20, font=5, bg="#ff7859", fg="black",command=lambda:self.add_to_expression("2")).grid(row=3, column=1)
        self.button_3 = Button(self.root, text="3", padx=40, pady=20, font=5,bg="#ff7859", fg="black", command=lambda:self.add_to_expression("3")).grid(row=3, column=2)
        self.button_4 = Button(self.root, text="4", padx=40, pady=20, font=5,bg="#ff7859", fg="black", command=lambda:self.add_to_expression("4")).grid(row=2, column=0)
        self.button_5 = Button(self.root, text="5", padx=40, pady=20, font=5,bg="#ff7859", fg="black", command=lambda:self.add_to_expression("5")).grid(row=2, column=1)
        self.button_6 = Button(self.root, text="6", padx=40, pady=20, font=5,bg="#ff7859", fg="black", command=lambda:self.add_to_expression("6")).grid(row=2, column=2)
        self.button_7 = Button(self.root, text="7", padx=40, pady=20, font=5, bg="#ff7859", fg="black",command=lambda:self.add_to_expression("7")).grid(row=1, column=0)
        self.button_8 = Button(self.root, text="8", padx=40, pady=20, font=5, bg="#ff7859", fg="black",command=lambda:self.add_to_expression("8")).grid(row=1, column=1)
        self.button_9 = Button(self.root, text="9", padx=40, pady=20, font=5, bg="#ff7859", fg="black",command=lambda:self.add_to_expression("9")).grid(row=1, column=2)

        self.button_add = Button(self.root, text="+", padx=40, pady=20, font=5, bg= "black", fg="yellow",command=lambda:self.add_to_expression("+")).grid(row=4, column=1)
        self.button_minus = Button(self.root, text="-", padx=40, pady=20, font=5,bg= "black", fg="yellow", command=lambda:self.add_to_expression('-')).grid(row=4, column=2)
        self.button_multiply = Button(self.root, text="×", padx=40, pady=20, font=5,bg= "black", fg="yellow", command=lambda:self.add_to_expression('×')).grid(row=5, column=0)
        self.button_divide = Button(self.root, text="÷", padx=40, pady=20, font=5,bg= "black", fg="yellow", command=lambda:self.add_to_expression('÷')).grid(row=5, column=1)
        self.button_exponent = Button(self.root, text="^", padx=40, pady=20, font=5,bg= "black", fg="yellow", command=lambda:self.add_to_expression('^')).grid(row=6, column=0)
        self.button_square = Button(self.root, text="x²", padx=40, pady=20, font=5,bg= "black", fg="yellow", command=lambda:self.add_to_expression('^(2)')).grid(row=6, column=2)
        self.button_obracket = Button(self.root, text="(", padx=40, pady=20, font=5,bg= "black", fg="yellow", command=lambda:self.add_to_expression('(')).grid(row=1, column=4)
        self.button_cbracket = Button(self.root, text=")", padx=40, pady=20, font=5,bg= "black", fg="yellow", command=lambda:self.add_to_expression(')')).grid(row=2, column=4)
        self.button_decimal = Button(self.root, text=".", padx=40, pady=20, font=5, bg= "black", fg="yellow",command=lambda:self.add_to_expression('.')).grid(row=3, column=4)
        self.button_pi = Button(self.root, text="pi", padx=40, pady=20, font=5,bg= "black", fg="yellow", command=lambda:self.add_to_expression('pi')).grid(row=4, column=4)
        self.button_e = Button(self.root, text="e", padx=40, pady=20, font=5, bg= "black", fg="yellow",command=lambda:self.add_to_expression('e')).grid(row=5, column=4)
        self.button_tau = Button(self.root, text="tau", padx=40, pady=20, font=5,bg= "black", fg="yellow", command=lambda:self.add_to_expression('tau')).grid(row=6, column=4)

        self.button_equal = Button(self.root, text="=", padx=40, pady=20, font=5,bg="#8ebfed",fg="black", command=self.display_result).grid(row=5, column=2)

        self.button_clear = Button(self.root, text="C", padx=38, pady=20, font=5, command=self.clear_display).grid(row=6, column=1)

        self.root.mainloop()


    def add_to_expression(self, element:str):

        self.string = str()
        self.string += element
        self.expression = self.string.replace('÷', '/')
        self.expression = self.string.replace('×', '*')
        self.expression = self.string.replace('^', '**')
        self.expression = self.string.replace('sin(', 'math.sin(')
        self.expression = self.string.replace('cos(', 'math.cos(')
        self.expression = self.string.replace('tan(', 'math.tan(')
        self.display.insert(END, self.string)
        return self.string


    def display_result(self):
      
        try:

            self.result_str = str(self.display.get())
            self.result_str = self.result_str.replace('÷', '/')
            self.result_str = self.result_str.replace('×', '*')
            self.result_str = self.result_str.replace('^', '**')
            self.result = eval(self.result_str)
            self.clear_display()
            self.display.insert(0, str(self.result))
            
        except:
            Message(self.root, message="Check the expression").show()
            self.clear_display()


    def clear_display(self):
        self.display.delete(0, END)    


if __name__ == "__main__":
    calculator = Calculator()
    print(f"{calculator.result_str}\n{calculator.result}")
    
    
