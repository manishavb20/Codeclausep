import os
import sys
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title("Simpli Music Player")
root.geometry("450x700+250+8")
root.configure(background='#003366')
root.resizable(False, False)
mixer.init()

# Create a function to open a file
def AddMusic():
    path = filedialog.askdirectory()
    if path:
       os.chdir(path)
       songs = os.listdir(path)

       for song in songs:
              if song.endswith(".mp3"):
                     Playlist.insert(END, song)


def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


# icon
lower_frame = Frame(root , bg = "#FFFFFF", width = 485 , height = 150 )
lower_frame.place ( x = 0 , y = 400)




image_icon = PhotoImage(file="logo png.png")
root.iconphoto(False, image_icon)




# Button
ButtonPlay = PhotoImage(file="play1.png")
Button(root, image=ButtonPlay, bg="#FFFFFF", bd=0, height = 100, width =100,
       command=PlayMusic).place(x=215, y=400)

ButtonStop = PhotoImage(file="stop1.png")
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height = 100, width =100,
       command=mixer.music.stop).place(x=130, y=400)

Buttonvolume = PhotoImage(file="volume.png")
Button(root, image=Buttonvolume, bg="#FFFFFF", bd=0, height = 100, width =100,
       command=mixer.music.unpause).place(x=30, y=400)

ButtonPause = PhotoImage(file="pause1.png")
Button(root, image=ButtonPause, bg="#FFFFFF", bd=0, height = 100, width =100,
       command=mixer.music.pause).place(x=300, y=400)

Buttonmain = PhotoImage(file="logo png.png")
Button(root, image=Buttonmain, bg="#FFFFFF", bd=0, height = 110, width =110,
       command=mixer.music.pause).place(x=700, y=800)

# Label       
Menu = PhotoImage(file="menu.png")
Label(root, image=Menu).place(x=0, y=580, width=485, height=120)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=200, width=485, height=200)



Button(root, text="Browse Music", width=50, height=3, font=("calibri", 15, "bold"), fg="Black", bg="#FBEAEA", command=AddMusic).place(x=0, y=120)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="light pink", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command = Playlist.yview)
Scroll.pack(side = RIGHT, fill = Y)
Playlist.pack(side = RIGHT, fill = BOTH)

# Execute Tkinter

root.mainloop()