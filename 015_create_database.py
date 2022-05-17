import tkinter as tk
import os
import sqlite3

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("400x400")

conn = sqlite3.connect("address_book.db")

c = conn.cursor()
c.execute(
    """CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)
"""
)


conn.commit()
conn.close()

root.mainloop()
