import tkinter as tk
import os
from tkinter.constants import W

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
# root.geometry("400x400")

# r = tk.IntVar()
# r.set(2) # default value, Option 2 is selected at start

# command is run at each time an option is selected, 
# even if the option is already selected
# tk.Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# tk.Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

TOPPINGS = [
    ('Pepperoni', "Pepperoni"),
    ('Cheese', "Cheese"),
    ('Mushroom', "Mushroom"),
    ('Onion', "Onion")
]

pizza = tk.StringVar()
pizza.set("Pepperoni")

for topping_name, topping in TOPPINGS:
    tk.Radiobutton(root, text=topping_name, variable=pizza, value=topping, command=lambda: clicked(pizza.get())).pack(anchor=W)

label_1 = tk.Label(root, text=pizza.get())
label_1.pack()

def clicked(value):
    label_1 = tk.Label(root, text=value)
    label_1.pack()

my_button = tk.Button(root, text="Click me", command=lambda: clicked(pizza.get()))
my_button.pack()

root.mainloop()