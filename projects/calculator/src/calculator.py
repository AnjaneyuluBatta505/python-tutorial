import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x500")
        
        self.expression = ""
        self.memory = ""
        self.input_text = tk.StringVar()
        
        self.create_ui()
        
    def create_ui(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack()
        
        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('arial', 18), width=25, bd=5, relief=tk.GROOVE)
        input_field.grid(row=0, column=0, columnspan=4)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack()
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('M+', 5, 1), ('M-', 5, 2), ('MR', 5, 3),
            ('^', 6, 0), ('√', 6, 1), ('%', 6, 2), ('log', 6, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(button_frame, text=text, font=('arial', 14), width=5, height=2, 
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
        
    def on_button_click(self, button_text):
        if button_text == '=':
            try:
                self.expression = str(eval(self.expression))
                self.input_text.set(self.expression)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.input_text.set("")
        elif button_text == 'C':
            self.expression = ""
            self.input_text.set("")
        elif button_text == 'M+':
            self.memory = self.expression
        elif button_text == 'M-':
            self.memory = ""
        elif button_text == 'MR':
            self.expression += self.memory
            self.input_text.set(self.expression)
        elif button_text == '√':
            try:
                self.expression = str(math.sqrt(float(self.expression)))
                self.input_text.set(self.expression)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input for Square Root")
        elif button_text == '^':
            self.expression += "**"
            self.input_text.set(self.expression)
        elif button_text == '%':
            self.expression += "%"
            self.input_text.set(self.expression)
        elif button_text == 'log':
            try:
                self.expression = str(math.log10(float(self.expression)))
                self.input_text.set(self.expression)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input for Logarithm")
        else:
            self.expression += button_text
            self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
