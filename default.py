#default
from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import pygame
import os
import time
from mutagen.mp3 import MP3
import random
class MusicPlayer:

  # Defining Constructor
  def __init__(self,root):
    self.root = root
    # Title of the window
    self.root.title("Nolae")
    #icon
    self.root.iconbitmap(r'n1.ico')
    # Window Geometry
    self.root.geometry("900x500")
    # Disable resizing
    self.root.resizable(False,False)
    # Icon 
    
    # Initiating Pygame
    pygame.init()
    # Initiating Pygame Mixer
    pygame.mixer.init()
    # Declaring track Variable
    self.track = StringVar()
    # Declaring Status Variable
    self.status = StringVar()
  
    # Creating Track Frame for Song label & status label
    trackframe = LabelFrame(self.root,text="",font=("Fixedsys",15,"bold"),bg="#ff86c8",fg="#eeb1b1",bd=5,relief=FLAT)
    trackframe.place(x=0,y=400,width=600,height=100)
    # Inserting Song Track Label
    songtrack = Label(trackframe,textvariable=self.track,width=25,font=("Fixedsys",15,"bold"),bg="#ff66dd",fg="white").grid(row=0,column=0,padx=10,pady=10)
    # Inserting Status Label
    trackstatus = Label(trackframe,textvariable=self.status,font=("Fixedsys",15,"italic"),bg="#ff66dd",fg="white").grid(row=0,column=1,padx=10,pady=10)

    # Creating Button Frame
    buttonframe = LabelFrame(self.root,text="",font=("times new roman",15,"bold"),bg="#ff86c8",fg="black",bd=5,relief=FLAT)
    buttonframe.place(x=450,y=400,width=550,height=100)
    playbtn = Button(buttonframe,text="|◀◀",command=self.prevsong,width=3,height=1,font=("times new roman",16,"bold"),
                    fg="white",bg="#ff66dd",relief=FLAT, activebackground="#ff86c8").grid(row=0,column=1,padx=10,pady=15)

    # Inserting Play Button
    playbtn = Button(buttonframe,text="▶",command=self.playsong,width=2,height=1,font=("times new roman",16,"bold"),
                    fg="white",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=3,padx=10,pady=15)
    # Inserting Pause Button
    playbtn = Button(buttonframe,text="||",command=self.pausesong,width=2,height=1,font=("times new roman",16,"bold"),
                    fg="white",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=5,padx=10,pady=15)
    # Inserting Unpause Button
    playbtn = Button(buttonframe,text="▶||",command=self.unpausesong,width=2,height=1,font=("times new roman",16,"bold"),
                    fg="white",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=7,padx=10,pady=15)
    playbtn = Button(buttonframe,text="▶▶|",command=self.nextsong,width=3,height=1,font=("times new roman",16,"bold"),
                    fg="white",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=11,padx=10,pady=15)
   
    # Creating Playlist Frame
    songsframe = LabelFrame(self.root,text="Song Playlist",font=("Fixedsys",18,"bold"),bg="#ff92ed",fg="black",bd=5,relief=FLAT)
    songsframe.place(x=0,y=0,width=900,height=400)
    # Inserting scrollbar
    scrol_y = Scrollbar(songsframe,orient=VERTICAL) 
    # Inserting Playlist listbox
    self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="#ff92ed",
                            selectmode=SINGLE,font=("Fixedsys",18,"bold"),bg="#ffc7ee",fg="BLACK",bd=2,relief=FLAT,height=10)
    # Applying Scrollbar to listbox
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=self.playlist.xview)
    self.playlist.pack(fill=BOTH)

    # Create Status Bar
    self.status_bar = Label(root,font=("Fixedsys",4),text='',bd=1,relief=FLAT,anchor=E,bg="#100c09",fg="white")
    self.status_bar.pack(fill=X,side=BOTTOM,ipady=2)
    selectbtn = Button(self.status_bar,text="SELECT",command=self.selectfolder,width=5,height=1,font=("Fixedsys",4,"bold"),
                    fg="white",bg="#100c09",relief=FLAT, activebackground="white").grid(row=0,column=1,padx=2,pady=2)

  # Grab Song Length Time Info
  def play_time(self):
    # Check for double timing
    if self.status.get() == "-Stopped":
      return 
    # Grab Current Song Elapsed Time
    current_time = pygame.mixer.music.get_pos() / 1000

    # throw up temp label to get data
    #slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Pos: {int(current_time)}')
    # convert to time format
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    # Get Currently Playing Song
    #current_song = song_box.curselection()
    #Grab song title from playlist
    song = self.playlist.get(ACTIVE)
    # add directory structure and mp3 to song title
    #song = f'{files}'
    # Load Song with Mutagen
    song_mut = MP3(song)
    # Get song Length
    global song_length
    song_length = song_mut.info.length
    # Convert to Time Format
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    # Increase current time by 1 second
    current_time +=1
    self.status_bar.config(text=f' {converted_current_time}  of  {converted_song_length}  ')
    self.status_bar.after(1000, self.play_time)

  ''''
    if int(my_slider.get()) == int(song_length):
      status_bar.config(text=f'Time Elapsed: {converted_song_length}  of  {converted_song_length}  ')
    elif paused:
      pass
    elif int(my_slider.get()) == int(current_time):
      # Update Slider To position
      slider_position = int(song_length)
      my_slider.config(to=slider_position, value=int(current_time))

    else:
      # Update Slider To position
      slider_position = int(song_length)
      my_slider.config(to=slider_position, value=int(my_slider.get()))
    
      # convert to time format
      converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))

      # Output time to status bar
      status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}  ')

      # Move this thing along by one second
      next_time = int(my_slider.get()) + 1
      my_slider.config(value=next_time)'''

    # Output time to status bar
     #status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}  ')

    # Update slider position value to current song position...
     #my_slider.config(value=int(current_time))
  
  
    # update time
    
  # Defining Play Song Function
  def playsong(self):
    # Displaying Selected Song title
    self.track.set(self.playlist.get(ACTIVE))
    # Displaying Status
    self.status.set("-Playing")
    # Loading Selected Song
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    # Playing Selected Song
    pygame.mixer.music.play()
    #
    self.play_time()

  

  def pausesong(self):
    # Displaying Status
    self.status.set("-Paused")
    # Paused Song
    pygame.mixer.music.pause()

  def unpausesong(self):
    # Displaying Status
    self.status.set("-Playing")
    # Playing back Song
    pygame.mixer.music.unpause()

  def selectfolder(self):
    # Remove previous folder in the beginning
    dir = None
    # Select directory, 'dir' variable as folder
    dir = fd.askdirectory()
    # Music files in the folder as 'files'
    files = os.listdir(dir)
    if not files:
      return
    os.chdir(dir)
    self.playlist.delete(0,END)
    for file in files:
      if file.endswith(".mp3"):
        self.playlist.insert(END,file)
  def nextsong(self):
    # Reset Slider and Status Bar
    self.status_bar.config(text='')
    #my_slider.config(value=0)

    # Get the current song tuple number
    next_one = self.playlist.curselection() 
    # Add one to the current song number
    next_one = next_one[0]+1
    #Grab song title from playlist
    song = self.playlist.get(next_one)
    # add directory structure and mp3 to song title
    #song = f'{files}'
    # Displaying Selected Song title
    self.track.set(self.playlist.get(next_one))
    # Displaying Status
    self.status.set("-Playing")
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear active bar in playlist listbox
    self.playlist.selection_clear(0, END)

    # Activate new song bar
    self.playlist.activate(next_one)

    # Set Active Bar to Next Song
    self.playlist.selection_set(next_one, last=None)
  def prevsong(self):
    # Reset Slider and Status Bar
    self.status_bar.config(text='')
    #my_slider.config(value=0)

    # Get the current song tuple number
    prev_one = self.playlist.curselection() 
    # Add one to the current song number
    prev_one = prev_one[0]-1
    #Grab song title from playlist
    song = self.playlist.get(prev_one)
    # add directory structure and mp3 to song title
    #song = f'{files}'
    # Displaying Selected Song title
    self.track.set(self.playlist.get(prev_one))
    # Displaying Status
    self.status.set("-Playing")
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


    # Clear active bar in playlist listbox
    self.playlist.selection_clear(0, END)

    # Activate new song bar
    self.playlist.activate(prev_one)

    # Set Active Bar to Next Song
    self.playlist.selection_set(prev_one, last=None)



  """
  def randomPlaylist():
  stop()
  all_songs = song_box.get(0, END)
  all_songs = list(all_songs)
  shuffle(all_songs)
  song_box.delete(0, END)
  for song in all_songs:
    song_box.insert(END, song)

random_btn = Button(controls_frame, text="Random", width=10, command=randomPlaylist)
random_btn.grid(row=0, column=5)
    """