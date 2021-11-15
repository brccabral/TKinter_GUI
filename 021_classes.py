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

class Elder:
    def __init__(self, master):
        myFrame = tk.Frame(master)
        myFrame.pack()

        self.myButton = tk.Button(master, text="Click me!", command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("You clicked")

e = Elder(root)

root.mainloop()