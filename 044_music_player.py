import tkinter as tk
from tkinter import Label, Menu, filedialog
import os
from tkinter.constants import ACTIVE, ANCHOR, BOTTOM, E, END, GROOVE, X
import pygame
import time
from mutagen.mp3 import MP3

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("700x350")

pygame.mixer.init()

song_box = tk.Listbox(root, bg="black", fg="green", width=80)
song_box.pack(pady=20)

back_img = tk.PhotoImage(file="images/previous.png")
play_img = tk.PhotoImage(file="images/play-button.png")
pause_img = tk.PhotoImage(file="images/pause-button.png")
play_pause_img = tk.PhotoImage(file="images/play-pause-button.png")
forward_img = tk.PhotoImage(file="images/skip-button.png")
stop_img = tk.PhotoImage(file="images/stop-button.png")

controls_frame = tk.Frame(root)
controls_frame.pack()

current_song_index = None
is_playing = False
song_length = None
def play_song(item):
    global is_playing, is_paused, song_length
    song = song_list[item]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    is_playing = True
    is_paused = False
    pause_btn.config(image=pause_img)
    song_box.selection_clear(0, END)
    song_box.activate(item)
    song_box.selection_set(item, last=None)
    song_length = MP3(song).info.length

def play_command():
    global current_song_index
    if song_box.curselection():
        current_song_index = song_box.curselection()[0]
        play_song(current_song_index)
        get_play_time()

def back_command():
    global current_song_index
    if current_song_index is None:
        return
    if current_song_index == 0:
        return
    current_song_index -= 1
    play_song(current_song_index)

def forward_command():
    global current_song_index
    if current_song_index is None:
        return
    if current_song_index >= len(song_list)-1:
        return
    current_song_index += 1
    play_song(current_song_index)

def stop_command():
    global is_paused, is_playing
    status_bar.after_cancel(status_bar_after)
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)
    is_playing = False
    is_paused = False
    pause_btn.config(image=pause_img)
    status_bar.config(text="")

is_paused = False
def pause_command():
    global is_paused, is_playing
    if not is_playing:
        return
    if not is_paused:
        pygame.mixer.music.pause()
        is_paused = True
        pause_btn.config(image=play_pause_img)
    else:
        pygame.mixer.music.unpause()
        is_paused = False
        pause_btn.config(image=pause_img)

back_btn = tk.Button(controls_frame, borderwidth=0, image=back_img, command=back_command)
play_btn = tk.Button(controls_frame, borderwidth=0, image=play_img, command=play_command)
pause_btn = tk.Button(controls_frame, borderwidth=0, image=pause_img, command=pause_command)
forward_btn = tk.Button(controls_frame, borderwidth=0, image=forward_img, command=forward_command)
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

def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir="sounds", title="Choose audio file", filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        song_list.append(song)
        song_box.insert(END, os.path.basename(song))


add_song_menu = tk.Menu(menu)
menu.add_cascade(label="Add songs", menu=add_song_menu)
add_song_menu.add_command(label="Add one song to playlist", command=add_one_song)
add_song_menu.add_command(label="Add many songs to playlist", command=add_many_songs)

def remove_item(item):
    song_box.delete(item, None)

def remove_one_song():
    if song_box.curselection():
        remove_item(song_box.curselection()[0])
        stop_command()

def remove_many_songs():
    if song_box.curselection():
        for item in song_box.curselection():
            remove_item(item)
        stop_command()

def remove_all_songs():
    song_box.delete(0, END)
    stop_command()

remove_song_menu = Menu(menu)
menu.add_cascade(label="Remove songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete one song from playlist", command=remove_one_song)
remove_song_menu.add_command(label="Delete many songs from playlist", command=remove_many_songs)
remove_song_menu.add_command(label="Delete all songs from playlist", command=remove_all_songs)

status_bar_after = None
def get_play_time():
    global status_bar_after
    if not is_playing:
        return
    current_time = pygame.mixer.music.get_pos()//1000
    current_time_str = time.strftime('%H:%M:%S', time.gmtime(current_time))
    song_length_str = time.strftime('%H:%M:%S', time.gmtime(song_length))
    status_bar.config(text=f"Time elapsed {current_time_str} of {song_length_str}")
    status_bar_after = status_bar.after(1000, get_play_time)

status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)


root.mainloop()