# this is not the correct way to change a label
# need to use "label.config(text='')"
# in future examples we start to use .config()
import tkinter as tk
import os
from tkinter.constants import DISABLED, NORMAL

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")

def myDelete():
    # myLabel.pack_forget()
    try:
        if myLabel.winfo_exists() == 1:
            myLabel.destroy()
            myButton['state'] = NORMAL
    except:
        pass

def myClick():
    # make myLabel global to be accessed by myDelete()
    global myLabel
    hello = f'Hello {e.get()}'
    myLabel = tk.Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.pack(pady=10)
    myButton['state'] = DISABLED

e = tk.Entry(root, width=50, font=('Helvetica', 30))
e.pack()

myButton = tk.Button(root, text="Enter Your Name", command=myClick)
myButton.pack(pady=10)

DeleteButton = tk.Button(root, text="Delete Text", command=myDelete)
DeleteButton.pack(pady=10)

root.mainloop()