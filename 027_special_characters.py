import tkinter as tk
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("400x400")

my_label = tk.Label(root, text="42" + "\u00b0", font=("Helvetica", 32)).pack(pady=10)


root.mainloop()
