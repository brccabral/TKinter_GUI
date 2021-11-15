import tkinter as tk
import os
from tkinter.constants import BOTH, VERTICAL

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")


# Panels

# border, relief, backgroundcolor
panel1 = tk.PanedWindow(bd=4, relief="sunken", bg="red")
panel1.pack(fill=BOTH, expand=1)

left_label = tk.Label(panel1, text="Left Panel")
panel1.add(left_label)

panel2 = tk.PanedWindow(panel1, orient=VERTICAL, bd=4, relief="raised", bg="blue")
panel1.add(panel2)

top_label = tk.Label(panel2, text="Top Panel")
panel2.add(top_label)

bottom_label = tk.Label(panel2, text="Bottom Panel")
panel2.add(bottom_label)


root.mainloop()