import tkinter as tk
import os
from tkinter.constants import (
    BOTH,
    BOTTOM,
    HORIZONTAL,
    LEFT,
    # NONE,
    # NS,
    NSEW,
    NW,
    RIGHT,
    VERTICAL,
    X,
    Y,
)
from tkhtmlview import HTMLLabel


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

        self.label = tk.Label(self.root, text="Sample")
        self.label.pack(padx=5, pady=5)

        self.frame_pages = tk.Frame(self.root)
        self.frame_pages.pack(fill=BOTH, expand=1)
        self.frame_pages.grid_rowconfigure(0, weight=1)
        self.frame_pages.grid_columnconfigure(0, weight=1)
        self.frame_pages.grid_columnconfigure(1, weight=1)

        self.frame_left = tk.Frame(self.frame_pages)
        self.frame_left.grid(row=0, column=0, sticky=NSEW)

        self.outer_frame = tk.Frame(self.frame_left)
        self.outer_frame.pack(fill=BOTH, expand=1)

        self.canvas = tk.Canvas(self.outer_frame)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.bind(
            "<Configure>",
            lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.work_frame = tk.Frame(self.canvas, background="red")

        if os.name == "nt":
            self.work_frame.bind(
                "<MouseWheel>",
                lambda event: self.canvas.yview(
                    "scroll", -1 if event.num == 4 else 1, "units"
                ),
            )
        else:
            self.work_frame.bind(
                "<Button-4>",
                lambda event: self.canvas.yview(
                    "scroll", -1 if event.num == 4 else 1, "units"
                ),
            )
            self.work_frame.bind(
                "<Button-5>",
                lambda event: self.canvas.yview(
                    "scroll", -1 if event.num == 4 else 1, "units"
                ),
            )

        self.canvas.create_window((0, 0), window=self.work_frame, anchor=NW)

        self.vertical_scroll = tk.Scrollbar(
            self.canvas, orient=VERTICAL, command=self.canvas.yview
        )
        self.canvas.config(yscrollcommand=self.vertical_scroll.set)
        self.vertical_scroll.pack(side=RIGHT, fill=Y)

        self.horizontal_scroll = tk.Scrollbar(
            self.canvas, orient=HORIZONTAL, command=self.canvas.xview
        )
        self.canvas.config(xscrollcommand=self.horizontal_scroll.set)
        self.horizontal_scroll.pack(side=BOTTOM, fill=X)

        self.labelhtml = HTMLLabel(self.work_frame, html="<h1>Hello World</h1>")
        self.labelhtml.pack(fill=BOTH, expand=1)
        self.labelhtml.fit_height()

        self.labellink = HTMLLabel(
            self.work_frame,
            html='<a href="https://www.youtube.com">YouTube</a>',
            height=3,
        )
        self.labellink.pack(fill=BOTH, expand=1)
        self.labellink.fit_height()

        # self.label_img_online = HTMLLabel(self.work_frame, width=150, height=40, html='<img src="https://assets.ubuntu.com/v1/2fc45f60-laptop.png" />')
        # self.label_img_online.pack(fill=BOTH, expand=1)
        # self.label_img_online.fit_height()

        self.label_img_local = HTMLLabel(
            self.work_frame, html='<img src="images/0.jpg" />'
        )
        self.label_img_local.pack(fill=BOTH, expand=1)
        self.label_img_local.fit_height()

        self.frame_right = tk.Frame(self.frame_pages)
        self.frame_right.grid(row=0, column=1, sticky=NSEW)

        self.outer_frame_right = tk.Frame(self.frame_right)
        self.outer_frame_right.pack(fill=BOTH, expand=1)

        self.canvas_right = tk.Canvas(self.outer_frame_right)
        self.canvas_right.pack(side=LEFT, fill=BOTH, expand=1)

        self.canvas_right.configure(scrollregion=self.canvas_right.bbox("all"))
        self.canvas_right.bind(
            "<Configure>",
            lambda event: self.canvas_right.configure(
                scrollregion=self.canvas_right.bbox("all")
            ),
        )

        self.work_frame_right = tk.Frame(self.canvas_right, background="red")

        if os.name == "nt":
            self.work_frame_right.bind(
                "<MouseWheel>",
                lambda event: self.canvas_right.yview(
                    "scroll", -1 if event.num == 4 else 1, "units"
                ),
            )
        else:
            self.work_frame_right.bind(
                "<Button-4>",
                lambda event: self.canvas_right.yview(
                    "scroll", -1 if event.num == 4 else 1, "units"
                ),
            )
            self.work_frame_right.bind(
                "<Button-5>",
                lambda event: self.canvas_right.yview(
                    "scroll", -1 if event.num == 4 else 1, "units"
                ),
            )

        self.canvas_right.create_window((0, 0), window=self.work_frame_right, anchor=NW)

        self.vertical_scroll_right = tk.Scrollbar(
            self.canvas_right, orient=VERTICAL, command=self.canvas_right.yview
        )
        self.canvas_right.config(yscrollcommand=self.vertical_scroll_right.set)
        self.vertical_scroll_right.pack(side=RIGHT, fill=Y)

        self.horizontal_scroll_right = tk.Scrollbar(
            self.canvas_right, orient=HORIZONTAL, command=self.canvas_right.xview
        )
        self.canvas_right.config(xscrollcommand=self.horizontal_scroll_right.set)
        self.horizontal_scroll_right.pack(side=BOTTOM, fill=X)

        self.labelhtml_right = HTMLLabel(
            self.work_frame_right,
            html='<h1>Hello World</h1>\
            <a href="https://www.youtube.com">YouTube</a>\
                <br />\
                <img src="images/0.jpg" />',
        )
        self.labelhtml_right.pack(fill=BOTH, expand=1)
        self.labelhtml_right.fit_height()

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
    app = TkinterApp("TkinterApp", 1069, 636)
    app.start()


if __name__ == "__main__":
    main()
