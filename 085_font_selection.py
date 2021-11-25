import tkinter as tk
import os
from tkinter import Event, font
from tkinter.constants import END, SINGLE


class TkinterApp:
    def __init__(self, appname="TkinterApp", width=400, height=400):
        self.appname = appname
        self.width = width
        self.height = height

        self.root = tk.Tk()

        self.root.title(self.appname)
        if os.name == "nt":
            self.root.wm_iconbitmap(bitmap="python3.ico")
        else:
            self.root.wm_iconbitmap(bitmap="@python3.xbm")
        self.root.iconphoto(self.root._w, tk.PhotoImage(file='python3.png'))

        self.text_font = font.Font(family='DejaVu Sans', size=32)

        self.frame = tk.Frame(self.root, width=480, height=275)
        self.frame.pack(padx=5, pady=5)
        self.frame.grid_propagate(False)
        self.frame.columnconfigure(0, weight=10)

        self.textbox = tk.Text(self.frame, width=40,
                               height=10, font=self.text_font)
        self.textbox.grid(row=0, column=0)
        self.textbox.grid_rowconfigure(0, weight=1)
        self.textbox.grid_columnconfigure(0, weight=1)

        # the quick brown fox jumped over the lazy dog

        self.fonts_frame = tk.Frame(self.root)
        self.fonts_frame.pack(padx=5, pady=5)

        self.listbox_families = tk.Listbox(
            self.fonts_frame, selectmode=SINGLE, width=50)
        self.listbox_families.grid(row=0, column=0)
        fonts = list(font.families())  # "Noto Color Emoji" crashes Tkinter
        fonts.sort()
        self.listbox_families.insert(END, *fonts)
        self.listbox_families.bind("<ButtonRelease-1>", self.change_family)

        self.listbox_sizes = tk.Listbox(
            self.fonts_frame, selectmode=SINGLE, width=5)
        self.listbox_sizes.grid(row=0, column=1)
        self.listbox_sizes.insert(END, *range(8, 72))
        self.listbox_sizes.bind("<ButtonRelease-1>", self.change_size)

        font_weights = [font.NORMAL, font.BOLD]

        self.listbox_weights = tk.Listbox(
            self.fonts_frame, selectmode=SINGLE, width=10)
        self.listbox_weights.grid(row=0, column=2)
        self.listbox_weights.insert(END, *font_weights)
        self.listbox_weights.bind("<ButtonRelease-1>", self.change_weight)

        font_slants = [font.ROMAN, font.ITALIC]

        self.listbox_slants = tk.Listbox(
            self.fonts_frame, selectmode=SINGLE, width=10)
        self.listbox_slants.grid(row=0, column=3)
        self.listbox_slants.insert(END, *font_slants)
        self.listbox_slants.bind("<ButtonRelease-1>", self.change_slants)

        self.listbox_underline = tk.Listbox(
            self.fonts_frame, selectmode=SINGLE, width=5)
        self.listbox_underline.grid(row=0, column=4)
        self.listbox_underline.insert(END, *[0, 1])
        self.listbox_underline.bind("<ButtonRelease-1>", self.change_underline)
        self.listbox_slants.bind("<ButtonRelease-1>", self.change_slants)

        self.listbox_overstrike = tk.Listbox(
            self.fonts_frame, selectmode=SINGLE, width=5)
        self.listbox_overstrike.grid(row=0, column=5)
        self.listbox_overstrike.insert(END, *[0, 1])
        self.listbox_overstrike.bind(
            "<ButtonRelease-1>", self.change_overstrike)

    def change_family(self, event: Event):
        self.text_font.config(family=self.listbox_families.get(
            self.listbox_families.curselection()))
        return "break"

    def change_size(self, event: Event):
        self.text_font.config(size=self.listbox_sizes.get(
            self.listbox_sizes.curselection()))
        return "break"

    def change_weight(self, event: Event):
        self.text_font.config(weight=self.listbox_weights.get(
            self.listbox_weights.curselection()))
        return "break"

    def change_slants(self, event: Event):
        self.text_font.config(slant=self.listbox_slants.get(
            self.listbox_slants.curselection()))
        return "break"

    def change_underline(self, event: Event):
        self.text_font.config(underline=self.listbox_underline.get(
            self.listbox_underline.curselection()))
        return "break"

    def change_overstrike(self, event: Event):
        self.text_font.config(overstrike=self.listbox_overstrike.get(
            self.listbox_overstrike.curselection()))
        return "break"

    def start(self):
        self.center_window()
        self.root.mainloop()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(
            f"{self.width}x{self.height}+{screen_width//2-self.width//2}+{screen_height//2-self.height//2}")


def main():
    app = TkinterApp("TkinterApp", 900, 500)
    app.start()


if __name__ == "__main__":
    main()
