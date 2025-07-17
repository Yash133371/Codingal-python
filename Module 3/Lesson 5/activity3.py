import tkinter as tk

def make_toplevel():
    toplevel = tk.Toplevel(win)
    toplevel.title("Toplevel window")
    toplevel.geometry("200x200")
    label = tk.Label(toplevel, text="Hello this is a toplevel window")
    label.pack()


win = tk.Tk()
win.title("Toplevel example")
win.geometry("200x200")


button = tk.Button(win, text="Open toplevel window", command=make_toplevel)
button.pack()


win.mainloop()