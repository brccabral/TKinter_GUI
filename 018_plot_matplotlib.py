import tkinter as tk
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(200_000, 25_000, 5_000)
    
    figure, axs = plt.subplots(1,1)
    axs.hist(house_prices, 50)
    chart_type = FigureCanvasTkAgg(figure, root)
    chart_type.get_tk_widget().pack()


button = tk.Button(root, text="Graph it", command=graph)
button.pack()

root.mainloop()