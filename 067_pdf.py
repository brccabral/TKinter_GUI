import tkinter as tk
import os
from tkinter.constants import END
import fitz as pymupdf  # fitz is pymupdf
from tkinter import Menu, filedialog
import logging

logging.basicConfig(
    format="%(levelname)s - %(asctime)s - %(name)s - %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)


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
        self.root.iconphoto(self.root._w, tk.PhotoImage(file="python3.png"))

        self.text = tk.Text(self.root, height=30, width=60)
        self.text.pack(pady=10)

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Clear", command=self.clear_text)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

    def clear_text(self):
        self.text.delete(1.0, END)

    def open_file(self):
        filename = filedialog.askopenfilename(
            initialdir=".", title="Open PDF file", filetypes=(("PDF files", "*.pdf"),)
        )
        if not filename:
            logging.debug("no file selected")
            return
        logging.debug(f"{filename=}")
        doc: pymupdf.Document
        with pymupdf.open(filename) as doc:
            text = ""
            for page in doc:
                logging.debug(f"{page}")
                # text += page.get_textpage().extractText()
                text += page.get_text()

        self.text.insert(1.0, text)

    def start(self):
        self.center_window()
        self.root.mainloop()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(
            f"{self.width}x{self.height}+{screen_width//2-self.width//2}+{screen_height//2-self.height//2}"
        )


def main():
    app = TkinterApp("TkinterApp", 700, 500)
    app.start()


if __name__ == "__main__":
    main()
