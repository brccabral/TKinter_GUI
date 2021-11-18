import tkinter as tk
from tkinter import filedialog
import os
from tkinter.constants import ACTIVE, END
import pygame

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("700x300")

pygame.mixer.init()

song_box = tk.Listbox(root, bg="black", fg="green", width=80)
song_box.pack(pady=20)

back_img = tk.PhotoImage(file="images/previous.png")
play_img = tk.PhotoImage(file="images/play-button.png")
pause_img = tk.PhotoImage(file="images/pause-button.png")
forward_img = tk.PhotoImage(file="images/skip-button.png")
stop_img = tk.PhotoImage(file="images/stop-button.png")

controls_frame = tk.Frame(root)
controls_frame.pack()

def back_command():
    pass
def play_command():
    song = None
    for item in song_box.curselection():
        song = song_list[item]
    if not song:
        return
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop_command():
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)


back_btn = tk.Button(controls_frame, borderwidth=0, image=back_img, command=back_command)
play_btn = tk.Button(controls_frame, borderwidth=0, image=play_img, command=play_command)
pause_btn = tk.Button(controls_frame, borderwidth=0, image=pause_img, command=back_command)
forward_btn = tk.Button(controls_frame, borderwidth=0, image=forward_img, command=back_command)
stop_btn = tk.Button(controls_frame, borderwidth=0, image=stop_img, command=stop_command)

back_btn.grid(row=0, column=0, padx=10)
play_btn.grid(row=0, column=1, padx=10)
pause_btn.grid(row=0, column=2, padx=10)
forward_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

menu = tk.Menu(root)
root.config(menu=menu)

song_list = []
def add_one_song():
    song = filedialog.askopenfilename(initialdir="sounds", title="Choose audio file", filetypes=(("mp3 Files", "*.mp3"),))
    song_list.append(song)
    song_box.insert(END, os.path.basename(song))


add_song_menu = tk.Menu(menu)
menu.add_cascade(label="Add songs", menu=add_song_menu)
add_song_menu.add_command(label="Add one song to playlist", command=add_one_song)

root.mainloop()