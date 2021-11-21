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

# define myLabel in main scope so it can be used
# right at the beginning of myClick and be destroyed
myLabel = tk.Label(root)

def myClick():
    global myLabel
    myLabel.grid_forget() # pack_forget() vs grid_forget()
        
    hello = f'Hello {e.get()}'
    myLabel = tk.Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.grid(row=3, column=0, pady=10)
    # myButton['state'] = DISABLED

e = tk.Entry(root, width=17, font=('Helvetica', 30))
e.grid(row=0, column=0, padx=10, pady=10)

myButton = tk.Button(root, text="Enter Your Name", command=myClick)
myButton.grid(row=1, column=0, pady=10)

root.mainloop()