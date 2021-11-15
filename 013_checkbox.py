import tkinter as tk
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")

value = tk.IntVar()
str_value = tk.StringVar()
# default values are 0 and 1
# use onvalue and offvalue to set custom values
c = tk.Checkbutton(root, text="Check here", variable=str_value, onvalue="sim", offvalue="nao")
c.deselect()
c.pack()

def show_value():
    myLabel = tk.Label(root, text=str_value.get())
    myLabel.pack()

myButton = tk.Button(root, text="Show selection", command=show_value)
myButton.pack()

root.mainloop()