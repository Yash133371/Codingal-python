import tkinter as tk
from PIL import Image, ImageTk


win = tk.Tk()
win.title("Tkinter images")
content = Image.open("colorful_image.jpg")
photo_image = ImageTk.PhotoImage(content)


label = tk.Label(win, image=photo_image)
label.pack()

win.mainloop()