from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x100")

def msg():

    # Show warning
    messagebox.showwarning("Alert", "Stop! Virus Found.")

button = Button(root,
                text="Scan for Virus",
                command=msg)

button.pack(pady=20)

root.mainloop()