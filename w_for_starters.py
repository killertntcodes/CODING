from tkinter import *

root = Tk()
root.title("Product Calculator")
root.geometry("400x300")

# Labels
title_lbl = Label(root, text="Multiply Two Numbers",
                  fg="white", bg="#072f5f",
                  height=2, width=30)
title_lbl.pack()

num1_lbl = Label(root, text="Enter First Number")
num1_lbl.pack()

num1_entry = Entry(root)
num1_entry.pack()

num2_lbl = Label(root, text="Enter Second Number")
num2_lbl.pack()

num2_entry = Entry(root)
num2_entry.pack()

def calculate():
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())

    product = num1 * num2

    result_lbl.config(text="Product = " + str(product))

btn = Button(root, text="Calculate",
             command=calculate,
             bg="#1261a0", fg="white")
btn.pack(pady=10)

result_lbl = Label(root, text="")
result_lbl.pack()
root.mainloop()