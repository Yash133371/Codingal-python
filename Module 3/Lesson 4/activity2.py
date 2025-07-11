import tkinter as tk


win = tk.Tk()
win.title("My window")
win.geometry("400x300")


for i in range(3):
    for j in range(3):
        frame = tk.Frame(win, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(frame, text=f"Row {i}\nColumn {j}")
        label.pack()


win.mainloop()