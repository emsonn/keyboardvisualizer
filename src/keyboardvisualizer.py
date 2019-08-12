import tkinter as tk

def on_return(event):
	print("Return Pressed")

def on_a_press(event):
	print("a Pressed")

def on_b_press(event):
	print("b Pressed")

def on_c_press(event):
	print("c Pressed")

def on_d_press(event):
	print("d Pressed")

def on_e_press(event):
	print("e Pressed")

def on_f_press(event):
	print("f Pressed")

def on_g_press(event):
	print("g Pressed")

def on_h_press(event):
	print("h Pressed")

def on_i_press(event):
	print("i Pressed")

def on_j_press(event):
	print("j Pressed")

def on_k_press(event):
	print("k Pressed")

def on_l_press(event):
	print("l Pressed")

def on_m_press(event):
	print("m Pressed")

def on_n_press(event):
	print("n Pressed")

def on_o_press(event):
	print("o Pressed")

def on_p_press(event):
	print("p Pressed")

def on_q_press(event):
	print("q Pressed")

def on_r_press(event):
	print("r Pressed")

def on_s_press(event):
	print("s Pressed")

def on_t_press(event):
	print("t Pressed")

def on_u_press(event):
	print("u Pressed")

def on_v_press(event):
	print("v Pressed")

def on_w_press(event):
	print("w Pressed")

def on_x_press(event):
	print("x Pressed")

def on_y_press(event):
	print("y Pressed")

def on_z_press(event):
	print("z Pressed")

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

root.bind("<Return>", on_return)
root.bind("a", on_a_press)
root.bind("b", on_b_press)
root.bind("c", on_c_press)
root.bind("d", on_d_press)
root.bind("e", on_e_press)
root.bind("f", on_f_press)
root.bind("g", on_g_press)
root.bind("h", on_h_press)
root.bind("i", on_i_press)
root.bind("j", on_j_press)
root.bind("k", on_k_press)
root.bind("l", on_l_press)
root.bind("m", on_m_press)
root.bind("n", on_n_press)
root.bind("o", on_o_press)
root.bind("p", on_p_press)
root.bind("q", on_q_press)
root.bind("r", on_r_press)
root.bind("s", on_s_press)
root.bind("t", on_t_press)
root.bind("u", on_u_press)
root.bind("v", on_v_press)
root.bind("w", on_w_press)
root.bind("x", on_x_press)
root.bind("y", on_y_press)
root.bind("z", on_z_press)




root.mainloop()