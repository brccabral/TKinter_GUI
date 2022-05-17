import tkinter as tk
import os
from tkinter.constants import DISABLED, NORMAL


class TkinterApp:
    def __init__(self, appname="TkinterApp", width=400, heigth=400):
        self.root = tk.Tk()
        self.appname = appname
        self.root.title(appname)
        if os.name == "nt":
            self.root.wm_iconbitmap(bitmap="python3.ico")
        else:
            self.root.wm_iconbitmap(bitmap="@python3.xbm")
        self.root.iconphoto(self.root._w, tk.PhotoImage(file="python3.png"))

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(
            f"{width}x{heigth}+{screen_width//2-width//2}+{screen_height//2-heigth//2}"
        )

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=lambda: 1 + 1)
        self.file_menu.add_command(label="Open", command=lambda: 1 + 1)

        self.button_disable_new = tk.Button(
            self.root, text="Disable 'New'", command=self.disable_new
        )
        self.button_disable_new.pack(pady=10)

        self.button_enable_new = tk.Button(
            self.root, text="Enable 'New'", command=self.enable_new
        )
        self.button_enable_new.pack(pady=10)

        self.button_disable_file = tk.Button(
            self.root, text="Disable 'File'", command=self.disable_file
        )
        self.button_disable_file.pack(pady=10)

        self.button_enable_file = tk.Button(
            self.root, text="Enable 'File'", command=self.enable_file
        )
        self.button_enable_file.pack(pady=10)

        self.button_delete_new = tk.Button(
            self.root, text="Delete 'New'", command=self.delete_new
        )
        self.button_delete_new.pack(pady=10)

        self.button_delete_file = tk.Button(
            self.root, text="Delete 'File'", command=self.delete_file
        )
        self.button_delete_file.pack(pady=10)

    def disable_new(self):
        self.file_menu.entryconfig("New", state=DISABLED)

    def enable_new(self):
        self.file_menu.entryconfig("New", state=NORMAL)

    def disable_file(self):
        self.menu.entryconfig("File", state=DISABLED)

    def enable_file(self):
        self.menu.entryconfig("File", state=NORMAL)

    def delete_new(self):
        self.file_menu.delete("New")

    def delete_file(self):
        self.menu.delete("File")

    def start(self):
        self.root.mainloop()


def main():
    app = TkinterApp("TkinterApp", 500, 500)
    app.start()


if __name__ == "__main__":
    main()
