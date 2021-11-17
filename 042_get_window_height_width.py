import tkinter as tk
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("500x500+500+300")

def get_info():
    geo = root.winfo_geometry()
    height = root.winfo_height()
    width = root.winfo_width()
    x = root.winfo_x()
    y = root.winfo_y()
    info_label = tk.Label(root, text=f"{geo=} {height=} {width=} {x=} {y=}")
    info_label.pack(pady=10)

my_button = tk.Button(root, text="Get info", command=get_info)
my_button.pack(pady=10)


root.mainloop()