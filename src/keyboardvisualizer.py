import tkinter as tk
from tkinter import PhotoImage, Label

HEIGHT = 210
WIDTH = 510
DOWN = 0

# Window initialization
root = tk.Tk()

# Window placement
top_right = root.winfo_screenwidth()
root.geometry("+{}+{}".format(top_right, DOWN))

# Window sizing
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

# Image loading + adding
filename = PhotoImage(file = "../images/minidox.png")
background_picture = Label(root, image=filename)
background_picture.place(relwidth=1, relheight=1)

canvas.pack()


root.mainloop()