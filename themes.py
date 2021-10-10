#themes for music player

##Pastel
# Creating Track Frame for Song label & status label
    trackframe = LabelFrame(self.root,text="Song Track",font=("Comic Sans MS",15,"bold"),bg="black",fg="#eeb1b1",bd=5,relief=SUNKEN)
    trackframe.place(x=0,y=400,width=500,height=100)
    # Inserting Song Track Label
    songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",15),bg="#E59090",fg="black").grid(row=0,column=0,padx=10,pady=5)
    # Inserting Status Label
    trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",10),bg="#E59090",fg="black").grid(row=0,column=1,padx=10,pady=5)

    # Creating Button Frame
    buttonframe = LabelFrame(self.root,text="",font=("times new roman",15,"bold"),bg="black",fg="black",bd=5,relief=SUNKEN)
    buttonframe.place(x=400,y=400,width=500,height=100)
    # Inserting Play Button
    playbtn = Button(buttonframe,text="▶",command=self.playsong,width=2,height=1,font=("times new roman",16,"bold"),fg="white",bg="black",relief=RAISED).grid(row=0,column=1,padx=15,pady=15)
    # Inserting Pause Button
    playbtn = Button(buttonframe,text="⏸",command=self.pausesong,width=2,height=1,font=("times new roman",16,"bold"),fg="white",bg="black",relief=RAISED).grid(row=0,column=5,padx=15,pady=15)
    # Inserting Unpause Button
    playbtn = Button(buttonframe,text="⏯",command=self.unpausesong,width=2,height=1,font=("times new roman",16,"bold"),fg="white",bg="black",relief=RAISED).grid(row=0,column=7,padx=15,pady=15)
    # Inserting Stop Button
    playbtn = Button(buttonframe,text="⏹",command=self.stopsong,width=2,height=1,font=("times new roman",16,"bold"),fg="white",bg="black",relief=RAISED).grid(row=0,column=9,padx=15,pady=15)
    # Inserting Next Button
    playbtn = Button(buttonframe,text="⏩",command=self.nextsong,width=2,height=1,font=("times new roman",16,"bold"),fg="white",bg="black",relief=RAISED).grid(row=0,column=11,padx=15,pady=15)
    # Inserting Select Button
    selectbtn = Button(buttonframe,text="SELECT",command=self.selectfolder,width=6,height=1,font=("times new roman",16,"bold"),fg="white",bg="black",relief=RAISED).grid(row=0,column=4,padx=10,pady=5)


    # Creating Playlist Frame
    songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="#eeb1b1",fg="black",bd=5,relief=SUNKEN)
    songsframe.place(x=0,y=0,width=1000,height=400)
    # Inserting scrollbar
    scrol_y = Scrollbar(songsframe,orient=VERTICAL)
    # Inserting Playlist listbox
    self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="green",
                            selectmode=SINGLE,font=("times new roman",12,"bold"),bg="#ffe9e9",fg="BLACK",bd=2,relief=SUNKEN,height=20)
    # Applying Scrollbar to listbox
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=self.playlist.xview)
    self.playlist.pack(fill=BOTH)


  ##Winter
  ##Summer
  ##Spring
  #Autumn
  ##Halloween
  ##