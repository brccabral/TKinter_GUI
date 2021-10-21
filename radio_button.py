import tkinter as tk
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
# root.geometry("400x400")

r = tk.IntVar()
r.set(2) # default value, Option 2 is selected at start

# command is run at each time an option is selected, 
# even if the option is already selected
tk.Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
tk.Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

label_1 = tk.Label(root, text=r.get())
label_1.pack()

def clicked(value):
    label_1 = tk.Label(root, text=value)
    label_1.pack()

my_button = tk.Button(root, text="Click me", command=lambda: clicked(r.get()))
my_button.pack()

root.mainloop()