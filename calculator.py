import tkinter as tk
from tkinter.constants import END

root = tk.Tk()
root.title("Simple Calculator")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))

e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def btn_value(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))

previous = 0
operation = ""
last_number = "" # saves last number to keep pressing equal with same number
def btn_operation(c_func):
    global previous, operation, last_number
    if e.get() != "":
        previous = e.get()
    operation = c_func
    last_number = ""
    e.delete(0, END)

def btn_equal():
    global last_number
    current = e.get()
    if current == "":
        return
    if last_number == "":
        last_number = previous
    e.delete(0, END)
    result = ""
    if operation == "+":
        result = float(last_number) + float(current)
    if operation == "*":
        result = float(last_number) * float(current)
    if operation == "-":
        if last_number == previous:
            result = float(last_number) - float(current)
        else:
            result = float(current) - float(last_number)
    if operation == "/":
        if last_number == previous:
            result = float(last_number) / float(current)
        else:
            result = float(current) / float(last_number)
    if last_number == previous:
        last_number = current
    e.insert(0, str(result))

def btn_clear():
    global previous, operation
    e.delete(0, END)
    previous = 0
    operation = ""

button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: btn_value(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: btn_value(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: btn_value(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: btn_value(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: btn_value(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: btn_value(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: btn_value(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: btn_value(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: btn_value(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: btn_value(0))
button_add = tk.Button(root, text="+", padx=36, pady=20, command=lambda: btn_operation("+"))
button_sub = tk.Button(root, text="-", padx=39, pady=20, command=lambda: btn_operation("-"))
button_mult = tk.Button(root, text="*", padx=39, pady=20, command=lambda: btn_operation("*"))
button_div = tk.Button(root, text="/", padx=40, pady=20, command=lambda: btn_operation("/"))
button_equal = tk.Button(root, text="=", padx=39, pady=20, command=btn_equal)
button_clear = tk.Button(root, text="C", padx=39, pady=20, command=btn_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_mult.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)


root.mainloop()