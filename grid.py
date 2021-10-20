import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

# Creating a label Widget
myLabel1 = tk.Label(root, text="Hello World!")
myLabel2 = tk.Label(root, text="I am Iron Man")
myLabel3 = tk.Label(root, text="Label 3")
myLabel4 = tk.Label(root, text="             ")

# keeps label always on the left
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel4.grid(row=1, column=1)
myLabel3.grid(row=1, column=5)

root.mainloop()