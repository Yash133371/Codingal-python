import tkinter as tk
from tkinter import messagebox


win = tk.Tk()
win.title("Messagebox example")

button = tk.Button(win, text="Show messagebox", command=lambda: messagebox.showinfo("Infobox", "This is an infobox"))
button.place(x=50, y=50)

win.mainloop()