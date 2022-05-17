import tkinter as tk
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("900x500")


def get_entry(entry: tk.Entry):
    if entry.get():
        return entry.get()
    return ""


def show_entries():
    map_text = " ".join(filter(None, list(map(get_entry, my_entries))))

    my_label.config(text=map_text)
    my_label.config(bg="red")


my_entries = []

for r in range(5):
    for c in range(5):
        my_entry = tk.Entry(root)
        my_entry.grid(row=r, column=c, padx=5, pady=20)
        my_entries.append(my_entry)

my_button = tk.Button(root, text="Click me", command=show_entries)
my_button.grid(row=r + 1, column=0, pady=20)

my_label = tk.Label(root, text="")
my_label.grid(row=r + 2, column=0, pady=20)

root.mainloop()
