import tkinter as tk
from PIL import ImageTk

WINDOW_HEIGHT = 210
WINDOW_WIDTH = 510
OFFSET_DOWN = 0
INSIDE_OFFSET_HEIGHT = 108
INSIDE_OFFSET_WIDTH = 257
DEFAULT_COLOR = "red"

# x1, y1, x2, y2
Q_KEY = (8, 21, 47, 60)
W_KEY = (49, 11, 87, 50)
E_KEY = (89, 6, 127, 44)
R_KEY = ()
T_KEY = ()
Y_KEY = ()
U_KEY = () 
I_KEY = ()
O_KEY = ()
P_KEY = () 

A_KEY = () 
S_KEY = (49, 51, 87, 90)
D_KEY = (89, 45, 127, 85)
F_KEY = ()
G_KEY = ()
H_KEY = ()
J_KEY = () 
K_KEY = ()
L_KEY = () 

Z_KEY = ()
X_KEY = (49, 91, 87, 130)
C_KEY = (89, 86, 127, 124)
V_KEY = ()
B_KEY = ()
N_KEY = ()
M_KEY = ()

root = tk.Tk()
root.title("Keyboard Visualizer")

root.attributes("-topmost", True)

top_right_dimension = root.winfo_screenwidth()
root.geometry("+{}+{}".format(top_right_dimension, OFFSET_DOWN))

c = tk.Canvas(root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)

img_path = "../images/minidox.png"
img = ImageTk.PhotoImage(file=img_path)

c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img)
c.pack()

def red_letter_box(key_coords):
	return c.create_rectangle(key_coords[0], key_coords[1], 
								key_coords[2], key_coords[3], 
								fill=DEFAULT_COLOR)

def on_return(event):
	print("Return Pressed")

def on_a_press(event):
	print("a Pressed")

def on_b_press(event):
	print("b Pressed")

def on_c_press(event):
	c.delete("all")
	c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img)
	print("Key pressed: c")

	box = red_letter_box(C_KEY)

def on_d_press(event):
	c.delete("all")
	c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img)
	print("Key pressed: d")

	box = red_letter_box(D_KEY)

def on_e_press(event):
	c.delete("all")
	c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img)
	print("Key pressed: e")

	box = red_letter_box(E_KEY)

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
	c.delete("all")
	c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img)
	print("Key pressed: q")

	box = red_letter_box(Q_KEY)

def on_r_press(event):
	print("r Pressed")

def on_s_press(event):
	c.delete("all")
	c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img)
	print("Key pressed: s")

	box = red_letter_box(S_KEY)

def on_t_press(event):
	print("t Pressed")

def on_u_press(event):
	print("u Pressed")

def on_v_press(event):
	print("v Pressed")

def on_w_press(event):
	c.delete("all")
	c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img)
	print("Key pressed: w")

	box = red_letter_box(W_KEY)

def on_x_press(event):
	c.delete("all")
	c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img)
	print("x Pressed")

	box = red_letter_box(X_KEY)


def on_y_press(event):
	print("y Pressed")

def on_z_press(event):
	print("z Pressed")

def main():
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

main()
