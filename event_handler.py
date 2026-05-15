from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("100x100")
def handle_keypress(event):
    "print the character associated with the key press"
    print(event.char)
window.bind("<Key>", handle_keypress)
def handle_click(event):
    print("Button clicked!")
def handle_click2(event):
    print("Good Boyyyy!")
button = Button(window, text="Click Me")
button2 = Button(window, text="Click Me Too")
button.pack()
button.bind("<Button-1>", handle_click)
button2.pack()
button2.bind("<Button-1>", handle_click2)
window.mainloop()