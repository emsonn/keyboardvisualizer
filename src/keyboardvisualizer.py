# References:
# https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm

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
Y_KEY = (304, 16, 342, 54)
U_KEY = (345, 11, 382, 50) 
I_KEY = (384, 6, 422, 44)
O_KEY = (425, 11, 462, 50)
P_KEY = (465, 21, 503, 60) 

A_KEY = (8, 61, 47, 100) 
S_KEY = (49, 51, 87, 90)
D_KEY = (89, 45, 127, 85)
F_KEY = (130, 51, 167, 90)
G_KEY = (170, 56, 208, 95)
H_KEY = (304, 56, 342, 95)
J_KEY = (345, 51, 382, 90) 
K_KEY = (384, 45, 422, 85)
L_KEY = (425, 51, 462, 90) 
SEMICOLON_KEY = (465, 61, 503, 100)

Z_KEY = (8, 101, 47, 140)
X_KEY = (49, 91, 87, 130)
C_KEY = (89, 86, 127, 124)
V_KEY = (130, 91, 167, 130)
B_KEY = (170, 97, 208, 134)
N_KEY = (304, 96, 342, 134)
M_KEY = (345, 91, 382, 130)
COMMA_KEY = (384, 86, 422, 124)
PERIOD_KEY = (425, 91, 462, 130)
FORWARDSLASH_KEY = (465, 101, 503, 140)

CONTROL_KEY = (105, 136, 142, 174)
LOWER_KEY = ()
SPACE_KEY = ()

BACKSPACE_KEY = ()
RAISE_KEY = ()
SHIFT_KEY = (370, 135, 407, 173)

root = tk.Tk()
root.title("Keyboard Visualizer")
root.focus_set()

root.attributes("-topmost", True)

top_right_dimension = root.winfo_screenwidth()
root.geometry("+{}+{}".format(top_right_dimension, OFFSET_DOWN))

c = tk.Canvas(root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)

img_path = "../images/minidox-primary-layer.png"
img = ImageTk.PhotoImage(file=img_path)

c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img)
c.pack()

def listen_for_keyboard():
	root.bind('Q', on_q_press)
	root.bind('W', on_w_press)
	root.bind('E', on_e_press)
	root.bind('R', on_r_press)
	root.bind('T', on_t_press)
	root.bind('Y', on_y_press)
	root.bind('U', on_u_press)
	root.bind('I', on_i_press)
	root.bind('O', on_o_press)
	root.bind('P', on_p_press)	
	root.bind('q', on_q_press)
	root.bind('w', on_w_press)
	root.bind('e', on_e_press)
	root.bind('r', on_r_press)
	root.bind('t', on_t_press)
	root.bind('y', on_y_press)
	root.bind('u', on_u_press)
	root.bind('i', on_i_press)
	root.bind('o', on_o_press)
	root.bind('p', on_p_press)

	root.bind('A', on_a_press)
	root.bind('S', on_s_press)
	root.bind('D', on_d_press)
	root.bind('F', on_f_press)
	root.bind('G', on_g_press)
	root.bind('H', on_h_press)
	root.bind('J', on_j_press)
	root.bind('K', on_k_press)
	root.bind('L', on_l_press)
	root.bind(':', on_semicolon_press)
	root.bind('a', on_a_press)
	root.bind('s', on_s_press)
	root.bind('d', on_d_press)
	root.bind('f', on_f_press)
	root.bind('g', on_g_press)
	root.bind('h', on_h_press)
	root.bind('j', on_j_press)
	root.bind('k', on_k_press)
	root.bind('l', on_l_press)
	root.bind(';', on_semicolon_press)

	root.bind('Z', on_z_press)
	root.bind('X', on_x_press)
	root.bind('C', on_c_press)
	root.bind('V', on_v_press)
	root.bind('B', on_b_press)
	root.bind('N', on_n_press)
	root.bind('M', on_m_press)
	root.bind("<less>", on_comma_press)
	root.bind('>', on_period_press)
	root.bind('?', on_forwardslash_press)
	root.bind('z', on_z_press)
	root.bind('x', on_x_press)
	root.bind('c', on_c_press)
	root.bind('v', on_v_press)
	root.bind('b', on_b_press)
	root.bind('n', on_n_press)
	root.bind('m', on_m_press)
	root.bind(',', on_comma_press)
	root.bind('.', on_period_press)
	root.bind('/', on_forwardslash_press)

	root.bind("<Control_L>", on_control_press)

	root.bind("<Shift_L>", on_shift_press)

def reset_canvas():
	c.delete("all")
	c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img)

def red_letter_box(key_coords):
	return c.create_rectangle(key_coords[0], key_coords[1], 
								key_coords[2], key_coords[3], 
								fill=DEFAULT_COLOR)

def print_key(key):
	print("Key pressed: " + key)

def visualize_keyboard(key, keycode):
	print_key(key)
	reset_canvas()
	red_letter_box(keycode)

def on_q_press(event):
	visualize_keyboard('q', Q_KEY)

def on_w_press(event):
	visualize_keyboard('w', W_KEY)

def on_e_press(event):
	visualize_keyboard('e', E_KEY)

def on_r_press(event):
	visualize_keyboard('r', R_KEY)

def on_t_press(event):
	visualize_keyboard('t', T_KEY)

def on_y_press(event):
	visualize_keyboard('y', Y_KEY)

def on_u_press(event):
	visualize_keyboard('u', U_KEY)

def on_i_press(event):
	visualize_keyboard('i', I_KEY)

def on_o_press(event):
	visualize_keyboard('o', O_KEY)

def on_p_press(event):
	visualize_keyboard('p', P_KEY)

# ========================

def on_a_press(event):
	visualize_keyboard('a', A_KEY)

def on_s_press(event):
	visualize_keyboard('s', S_KEY)

def on_d_press(event):
	visualize_keyboard('d', D_KEY)

def on_f_press(event):
	visualize_keyboard('f', F_KEY)

def on_g_press(event):
	visualize_keyboard('g', G_KEY)

def on_h_press(event):
	visualize_keyboard('h', H_KEY)

def on_j_press(event):
	visualize_keyboard('j', J_KEY)

def on_k_press(event):
	visualize_keyboard('k', K_KEY)

def on_l_press(event):
	visualize_keyboard('l', L_KEY)

def on_semicolon_press(event):
	visualize_keyboard("semicolon", SEMICOLON_KEY)

# ========================

def on_z_press(event):
	visualize_keyboard('z', Z_KEY)

def on_x_press(event):
	visualize_keyboard('x', X_KEY)

def on_c_press(event):
	visualize_keyboard('c', C_KEY)

def on_v_press(event):
	visualize_keyboard('v', V_KEY)

def on_b_press(event):
	visualize_keyboard('b', B_KEY)

def on_n_press(event):
	visualize_keyboard('n', N_KEY)

def on_m_press(event):
	visualize_keyboard('m', M_KEY)

def on_comma_press(event):
	visualize_keyboard(',', COMMA_KEY)

def on_period_press(event):
	visualize_keyboard('.', PERIOD_KEY)

def on_forwardslash_press(event):
	visualize_keyboard('/', FORWARDSLASH_KEY)

# ========================

def on_control_press(event):
	visualize_keyboard("control", CONTROL_KEY)

def on_shift_press(event):
	visualize_keyboard("shift", SHIFT_KEY)

def main():
	listen_for_keyboard()

	root.mainloop()

main()
