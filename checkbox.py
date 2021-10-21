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
c = tk.Checkbutton(root, text="Check here", variable=value)
c.pack()

def show_value():
    myLabel = tk.Label(root, text=value.get())
    myLabel.pack()

myButton = tk.Button(root, text="Show selection", command=show_value)
myButton.pack()

root.mainloop()