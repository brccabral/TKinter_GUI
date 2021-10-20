import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

# Creating a label Widget
myLabel = tk.Label(root, text="Hello World!")
# Shoving it ont the screen
myLabel.pack()

root.mainloop()