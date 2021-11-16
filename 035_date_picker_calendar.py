import tkinter as tk
from tkcalendar import Calendar
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")

cal = Calendar(root, selectmode="day", year=2020, month=5, day=22)
cal.pack(pady=20, fill="both", expand=True)

def grab_date():
    my_label.config(text=f"Selected date is {cal.get_date()}")

my_button = tk.Button(root, text="Get Date", command=grab_date)
my_button.pack(pady=10)

my_label = tk.Label(root, text="")
my_label.pack(pady=10)

root.mainloop()