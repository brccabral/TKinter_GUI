import tkinter as tk
from tkinter import Event, IntVar, Label, Menu, Scale, filedialog
import os
from tkinter.constants import ACTIVE, BOTTOM, DISABLED, E, END, GROOVE, HORIZONTAL, X
import pygame
import time
from mutagen.mp3 import MP3
import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

# need to call pygame.init() instead of pygame.mixer.init()
# because we need to use pygame.USEREVENT to then use pygame.mixer.music.set_endevent()
# and it needs to be called before tk.Tk()
pygame.init()
# pygame.mixer.init()
MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("700x450")

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
slider_start_position = None
def play_song(item, start_pos):
    global is_playing, is_paused, song_length, slider_start_position
    song = song_list[item]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=start_pos)
    is_playing = True
    is_paused = False
    pause_btn.config(image=pause_img)
    
    # select based on back and forward buttons
    song_box.selection_clear(0, END) 
    song_box.activate(item)
    song_box.selection_set(item, last=None)

    song_length = MP3(song).info.length
    slider.config(state=ACTIVE, to=song_length)
    slider_start_position = start_pos
    logging.debug(f'play_song {time.time()}')
    get_play_time()

def play_command():
    global current_song_index
    if song_box.curselection():
        current_song_index = song_box.curselection()[0]
        play_song(current_song_index, 0)

def back_command():
    global current_song_index
    if current_song_index is None:
        return
    if current_song_index == 0:
        return
    current_song_index -= 1
    play_song(current_song_index, 0)

def forward_command():
    global current_song_index
    if current_song_index is None:
        return
    if current_song_index >= len(song_list)-1:
        return
    current_song_index += 1
    play_song(current_song_index, 0)

def stop_command():
    global is_paused, is_playing
    logging.debug(f'Stop')
    status_bar.after_cancel(status_bar_after)
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)
    is_playing = False
    is_paused = False
    pause_btn.config(image=pause_img)
    status_bar.config(text="")
    set_slide(0)
    slider.config(state=DISABLED)

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
        logging.debug(f'Not playing {time.time()}')
        status_bar.after_cancel(status_bar_after)
        return
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            logging.debug(f'End {time.time()} {current_song_index=} {len(song_list) - 1=}')
            if current_song_index < len(song_list) - 1:
                forward_command()
            else:
                stop_command()
            return
    # need to check if busy otherwise get_pos() will return 0 and update 
    # labels with just slider_start_position
    if pygame.mixer.music.get_busy():
        current_time = pygame.mixer.music.get_pos()/1000 + slider_start_position
        current_time_str = time.strftime('%H:%M:%S', time.gmtime(current_time))
        song_length_str = time.strftime('%H:%M:%S', time.gmtime(song_length))
        status_bar.config(text=f"Time elapsed {current_time_str} of {song_length_str}")
        set_slide(current_time)
        
    # run again every 1000 ms
    logging.debug(f'get_play_time {time.time()}')
    status_bar_after = status_bar.after(1000, get_play_time)
    

status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

def set_slide(current_time: float):
    slider_var.set(current_time)
    slider.config(label=time.strftime('%H:%M:%S', time.gmtime(current_time)))

def set_slider_start_position(event: Event):
    global slider_start_position
    if not is_playing:
        return
    value = slider.get()
    slider_start_position = float(value)
    play_song(current_song_index, slider_start_position)
    set_slide(slider_start_position)

slider_var = IntVar(root, value=0)
# if we use Scale(command=FUNC), FUNC will be called at every slide
# and it will call many get_play_time(), which will call many after()
# and these many after will be called sometime even after song is finished.
# It is better to use bind() and get the slider position only when user
# releases it, so FUNC will be called only once
slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, length=550, variable=slider_var, showvalue=False, state=DISABLED)
slider.bind("<ButtonRelease-1>",set_slider_start_position)
slider.pack(pady=1)
slider.config(label=time.strftime('%H:%M:%S', time.gmtime(0)))

root.mainloop()
pygame.quit()