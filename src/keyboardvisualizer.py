import tkinter as tk

HEIGHT = 210
WIDTH = 510
DOWN = 0

# Window initialization
root = tk.Tk()
root.title("Keyboard Visualizer")

# Window placement
top_right = root.winfo_screenwidth()
root.geometry("+{}+{}".format(top_right, DOWN))

# Window sizing
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

# Image loading + adding
filename = tk.PhotoImage(file = "../images/minidox.png")
background_picture = tk.Label(root, image=filename)
background_picture.place(relwidth=1, relheight=1)

canvas.pack()



root.mainloop()