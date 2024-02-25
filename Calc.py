import tkinter as tk
from tkinter import messagebox
import math


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x400")
        self.minsize(400, 400) #размер

        self.result_var = tk.StringVar()
        self.first_number = 0
        self.second_number = 0
        self.operator = None
        self.check = False
        self.repeat = False

        self.create_widgets() # Создание GUI

        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

        self.entry.bind("<Key>", lambda _: "break")

    def create_widgets(self):
        self.entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, state="readonly")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=("Arial", 18), width=5, height=2,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        square_button = tk.Button(self, text="x²", font=("Arial", 18), width=5, height=2, command=self.square)
        square_button.grid(row=0, column=4, sticky="nsew")

        sqrt_button = tk.Button(self, text="√", font=("Arial", 18), width=5, height=2, command=self.square_root)
        sqrt_button.grid(row=1, column=4, sticky="nsew")

        cleanup_button = tk.Button(self, text="C", font=("Arial", 18), width=5, height=2, command=self.cleanup)
        cleanup_button.grid(row=5, column=0, columnspan=2, sticky="nsew")

    def on_button_click(self, text): # При нажатии кнопки
        if text == "=": # Равно
            if self.operator and self.first_number is not None and self.result_var.get() and self.repeat is False:
                self.second_number = float(self.result_var.get())
                result = self.calculate(self.first_number, self.second_number, self.operator)
                self.result_var.set(result)
                self.first_number = result
                self.operator = self.operator
                self.check = True
                self.repeat = True
            elif self.first_number is not None and self.result_var.get():
                result = self.calculate(self.first_number, self.second_number, self.operator)
                self.result_var.set(result)
                self.first_number = result
                self.operator = self.operator
                self.check = True

        elif text == "+" or text == "-" or text == "*" or text == "/": # Плюс, минус, умнож и дел
            self.operator = text
            self.first_number = float(self.result_var.get())
            self.result_var.set("")
            self.check = False
            self.repeat = False
        elif text == "." and not self.check: # Запятая/точка
            current_text = self.result_var.get()
            if "." not in current_text:
                new_text = current_text + "."
                self.result_var.set(new_text)
        elif text == "C": # Очистка
            self.result_var.set("")
            self.first_number = None
            self.operator = None
            self.check = False
            self.repeat = False
        else:
            if self.check:
                self.result_var.set("")
                self.check = False
            current_text = self.result_var.get()
            new_text = current_text + text
            self.result_var.set(new_text)

    def calculate(self, num1, num2, operator): # Операции плюс, минус, умнож и дел
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 / num2

    def square(self): # Квадрат
        current_text = self.result_var.get()
        if current_text:
            num = float(current_text)
            result = num * num
            self.result_var.set(result)
            self.first_number = result

    def square_root(self): # Корень
        current_text = self.result_var.get()
        if current_text:
            num = float(current_text)
            if num >= 0:
                result = math.sqrt(num)
                self.result_var.set(result)
                self.first_number = result
            else:
                messagebox.showerror("Ошибка", "Нельзя найти корень из негативного числа")

    def cleanup(self): # Очистка
        self.result_var.set("")
        self.first_number = None
        self.operator = None
        self.check = False


if __name__ == "__main__": # Начало прграммы
    app = Calculator()
    app.mainloop()