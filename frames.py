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

# pad inside
frame = tk.LabelFrame(root, text="This is my frame", padx=50, pady=50)
# pad outside
frame.pack(padx=10, pady=10)

b = tk.Button(frame, text="Click me")
b.pack()

root.mainloop()