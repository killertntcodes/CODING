from tkinter import *
from tkinter import messagebox as Message
root = Tk()
root.geometry("250x200")
textbox = Text(root, height=5, width=30, bg="#BEBEBE", fg="red")
def convert():
    try:
        centimeters = float(entry.get())
        inches = centimeters / 2.54
        textbox.delete(1.0, END)
        textbox.insert(END, f"{centimeters} centimeters is equal to {inches:.2f} inches.")
    except ValueError:
        Message.showerror("Error", "Please enter a valid number.")
label = Label(root, text="Enter length in centimeters:")
entry = Entry(root)
button = Button(root, text="Convert to Inches", command=convert)
button.config(bg="blue", fg="white")
label.pack(pady=10)
entry.pack(pady=5)
button.pack(pady=10)
textbox.pack(pady=10)
root.mainloop()