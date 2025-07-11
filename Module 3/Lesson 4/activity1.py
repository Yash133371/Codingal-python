import tkinter as tk

win = tk.Tk()
win.title("Tkinter window")
win.geometry("300x200")
win.config(background="chocolate")

my_frame = tk.Frame(win)
label = tk.Label(my_frame, foreground="white", text="This is a label", background="lightblue")
label.pack(pady=5)
my_frame.pack(pady=10)

my_frame2 = tk.Frame(win)
label2 = tk.Label(win, foreground="white", text="This is another label", background="orange")
label2.pack(pady=5)
my_frame2.pack(pady=10)

win.mainloop()