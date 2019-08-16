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
R_KEY = (130, 11, 167, 50)
T_KEY = (170, 16, 208, 54)
Y_KEY = ()
U_KEY = () 
I_KEY = ()
O_KEY = ()
P_KEY = () 

A_KEY = (8, 61, 47, 100) 
S_KEY = (49, 51, 87, 90)
D_KEY = (89, 45, 127, 85)
F_KEY = (130, 51, 167, 90)
G_KEY = (170, 56, 208, 95)
H_KEY = ()
J_KEY = () 
K_KEY = ()
L_KEY = () 

Z_KEY = (8, 101, 47, 140)
X_KEY = (49, 91, 87, 130)
C_KEY = (89, 86, 127, 124)
V_KEY = (130, 91, 167, 130)
B_KEY = (170, 97, 208, 134)
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


def reset_canvas():
	c.delete("all")
	c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img)

def red_letter_box(key_coords):
	return c.create_rectangle(key_coords[0], key_coords[1], 
								key_coords[2], key_coords[3], 
								fill=DEFAULT_COLOR)

def print_key(char):
	print("Key pressed: " + char)

def on_return(event):
	print("Return Pressed")

def on_a_press(event):
	print_key('a')
	reset_canvas()
	red_letter_box(A_KEY)

def on_b_press(event):
	print_key('b')
	reset_canvas()
	red_letter_box(B_KEY)

def on_c_press(event):
	print_key('c')
	reset_canvas()
	red_letter_box(C_KEY)

def on_d_press(event):
	print_key('d')
	reset_canvas()
	red_letter_box(D_KEY)

def on_e_press(event):
	print_key('e')	
	reset_canvas()
	red_letter_box(E_KEY)

def on_f_press(event):
	print_key('f')
	reset_canvas()
	red_letter_box(F_KEY)

def on_g_press(event):
	print_key('g')
	reset_canvas()
	red_letter_box(G_KEY)

def on_h_press(event):
	print_key('h')
	reset_canvas()

def on_i_press(event):
	print_key('i')
	reset_canvas()

def on_j_press(event):
	print_key('j')
	reset_canvas()

def on_k_press(event):
	print_key('k')
	reset_canvas()

def on_l_press(event):
	print_key('l')
	reset_canvas()

def on_m_press(event):
	print_key('m')
	reset_canvas()

def on_n_press(event):
	print_key('n')
	reset_canvas()

def on_o_press(event):
	print_key('o')
	reset_canvas()

def on_p_press(event):
	print_key('p')
	reset_canvas()

def on_q_press(event):
	print_key('q')
	reset_canvas()
	red_letter_box(Q_KEY)

def on_r_press(event):
	print_key('r')
	reset_canvas()
	red_letter_box(R_KEY)

def on_s_press(event):
	print_key('s')
	reset_canvas()
	red_letter_box(S_KEY)

def on_t_press(event):
	print_key('t')
	reset_canvas()
	red_letter_box(T_KEY)

def on_u_press(event):
	print_key('u')
	reset_canvas()

def on_v_press(event):
	print_key('v')
	reset_canvas()
	red_letter_box(V_KEY)

def on_w_press(event):
	print_key('w')
	reset_canvas()
	red_letter_box(W_KEY)

def on_x_press(event):
	print_key('x')
	reset_canvas()
	red_letter_box(X_KEY)

def on_y_press(event):
	print_key('y')
	reset_canvas()

def on_z_press(event):
	print_key('z')
	reset_canvas()
	red_letter_box(Z_KEY)

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
