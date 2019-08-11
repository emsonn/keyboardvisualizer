import tkinter as tk
from tkinter import PhotoImage, Label

HEIGHT = 210
WIDTH = 510

# ws = root.winfo_screenwidth()
# hs = root.winfo_screenheight()

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# frame = tk.Frame(root, )
filename = PhotoImage(file = "/home/eddie/Downloads/minidox.png")
background_picture = Label(root, image=filename)
background_picture.place(x=0, y=0, relwidth=1, relheight=1)

canvas.pack()

root.mainloop()