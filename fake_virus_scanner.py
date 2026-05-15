from tkinter import *
from tkinter import messagebox
from playsound import playsound

root = Tk()
root.geometry("250x200")

def msg():

    # Play sound
    playsound("spongebob-oh-no!-made-with-Voicemod.mp3")

    # Show warning
    messagebox.showwarning("Alert", "Stop! Virus Found.")

button = Button(root,
                text="Scan for Virus",
                command=msg)

button.place(x=60, y=80)

root.mainloop()from tkinter import *
from tkinter import messagebox
from playsound import playsound

root = Tk()
root.geometry("250x200")

def msg():

    # Play sound
    playsound("spongebob-oh-no!-made-with-Voicemod.mp3")

    # Show warning
    messagebox.showwarning("Alert", "Stop! Virus Found.")

button = Button(root,
                text="Scan for Virus",
                command=msg)

button.place(x=60, y=80)

root.mainloop()