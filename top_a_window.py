# root window
from tkinter import *
root = Tk()
root.geometry("200x300")
root.title("main")
l = Label(root, text = "This is root window")

# top window
def open_top():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = Label(top, text = "This is toplevel window")
    l2.pack(pady=10)
b = Button(root, text = "open top", command = open_top)
l.pack(pady=10)
b.pack(pady=10)
root.mainloop()