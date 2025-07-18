import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Denomination Counter")
root.config(bg="lightblue")
root.geometry("650x400")


upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = tk.Label(root, image=image, bg="lightblue")
label.place(x=100, y=20)
label1 = tk.Label(
    root,
    text="Welcome to denomination counter application!"
)
label1.place(relx=0.5, y=340)


def msg():
    msgbox = messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count"
    )
    if msgbox == "ok":
        topwin()


button1 = tk.Button(
    root,
    text="Let's get started",
    command=msg,
    bg="brown",
    fg="white"
)
button1.place(x=250, y=360)


def topwin():
    top = tk.Toplevel()
    top.title("Denomination calculator")
    top.config(bg="lightgrey")
    top.geometry("600x350+50+50")


    label = tk.Label(top, text="Enter total amount")
    entry = tk.Entry()
    lbl = tk.Label(top, text="Here are number of notes for each denomination")
    l1 = tk.Label(top, text="2000", bg="lightgrey")
    l2 = tk.Label(top, text="500", bg="lightgrey")
    l3 = tk.Label(top, text="100", bg="lightgrey")

    t1 = tk.Entry(top)
    t2 = tk.Entry(top)
    t3 = tk.Entry(top)

    def calculate():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, tk.END)
            t2.delete(0, tk.END)
            t3.delete(0, tk.END)

            t1.insert(tk.END, str(note2000))
            t2.insert(tk.END, str(note500))
            t3.insert(tk.END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")


    btn = tk.Button(top, text="Calculate", command=calculate, bg="brown", fg="white")


    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()


root.mainloop()