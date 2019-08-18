# References:
# https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
# https://www.tcl.tk/man/tcl8.6/TkCmd/keysyms.htm

import tkinter as tk
from PIL import ImageTk
from sys import platform

if platform == "linux" or platform == "linux2":
	OS_CODE = "linux"
elif platform == "darwin":
	OS_CODE = "macOS"
else:
	OS_CODE = "windows"

WINDOW_HEIGHT = 210
WINDOW_WIDTH = 510
OFFSET_DOWN = 0
INSIDE_OFFSET_HEIGHT = 108
INSIDE_OFFSET_WIDTH = 257
DEFAULT_COLOR = "red"

# x1, y1, x2, y2
KEY_Q = (8, 21, 47, 60)
KEY_W = (49, 11, 87, 50)
KEY_E = (89, 6, 127, 44)
KEY_R = (130, 11, 167, 50)
KEY_T = (170, 16, 208, 54)
KEY_Y = (304, 16, 342, 54)
KEY_U = (345, 11, 382, 50) 
KEY_I = (384, 6, 422, 44)
KEY_O = (425, 11, 462, 50)
KEY_P = (465, 21, 503, 60) 

KEY_A = (8, 61, 47, 100) 
KEY_S = (49, 51, 87, 90)
KEY_D = (89, 45, 127, 85)
KEY_F = (130, 51, 167, 90)
KEY_G = (170, 56, 208, 95)
KEY_H = (304, 56, 342, 95)
KEY_J = (345, 51, 382, 90) 
KEY_K = (384, 45, 422, 85)
KEY_L = (425, 51, 462, 90) 
KEY_SEMICOLON = (465, 61, 503, 100)

KEY_Z = (8, 101, 47, 140)
KEY_X = (49, 91, 87, 130)
KEY_C = (89, 86, 127, 124)
KEY_V = (130, 91, 167, 130)
KEY_B = (170, 97, 208, 134)
KEY_N = (304, 96, 342, 134)
KEY_M = (345, 91, 382, 130)
KEY_COMMA = (384, 86, 422, 124)
KEY_PERIOD = (425, 91, 462, 130)
KEY_FORWARDSLASH = (465, 101, 503, 140)

KEY_CONTROL = (105, 136, 142, 174)

# Bottom left, top left, top right, bottom right
KEY_LOWER = ((144, 175), (154, 138), (191, 148), (181, 185))
KEY_SPACE = ((182, 186), (217, 127), (250, 146), (216, 205))

KEY_BACKSPACE = ((262, 145), (295, 126), (329, 185), (296, 205))
KEY_RAISE = ((331, 184), (321, 148), (358, 138), (368, 174))
KEY_SHIFT = (370, 135, 407, 173)

root = tk.Tk() 
root.title("Keyboard Visualizer")
root.attributes("-topmost", True)
root.focus_set()

top_right_dimension = root.winfo_screenwidth()

root.geometry("+{}+{}".format(top_right_dimension, OFFSET_DOWN))

c = tk.Canvas(root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)

img_primary_path = "../images/minidox-primary-layer.png"
img_primary = ImageTk.PhotoImage(file=img_primary_path)

img_lower_path = "../images/minidox-lower-layer.png"
img_lower = ImageTk.PhotoImage(file=img_lower_path)

img_raise_path = "../images/minidox-raise-layer.png"
img_raise = ImageTk.PhotoImage(file=img_raise_path)

img_both_path = "../images/minidox-BOTH-layer.png"
img_both = ImageTk.PhotoImage(file=img_both_path)

def listen_for_keyboard():
	lower_layer()
	primary_layer()
	raise_layer()
	both_layer()

def lower_layer():
	root.bind('!', on_lower_press)
	root.bind('@', on_lower_press)
	root.bind('#', on_lower_press)
	root.bind('$', on_lower_press)
	root.bind('%', on_lower_press)
	root.bind('^', on_lower_press)
	root.bind('&', on_lower_press)
	root.bind('*', on_lower_press)
	root.bind('(', on_lower_press)
	root.bind(')', on_lower_press)

	root.bind("<Escape>", on_lower_press)
	root.bind('_', on_lower_press)
	root.bind('+', on_lower_press)
	root.bind('{', on_lower_press)
	root.bind('}', on_lower_press)

	root.bind("<Caps_Lock>", on_lower_press)
	root.bind('~', on_lower_press)
	root.bind(',', on_lower_press)
	root.bind('|', on_lower_press)
	root.bind('"', on_lower_press)
	root.bind("<Return>", on_lower_press)
	
	if OS_CODE is "linux" or OS_CODE is "windows":
		root.bind("<Delete>", on_lower_press)

def primary_layer():

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

	root.bind("<space>", on_space_press)
	
	if OS_CODE is "linux" or OS_CODE is "windows":
		root.bind("<BackSpace>", on_backspace_press)
	else:
		root.bind("<Delete>", on_backspace_press)

	root.bind("<Shift_L>", on_shift_press)

def raise_layer():
	root.bind('1', on_raise_press)
	root.bind('2', on_raise_press)
	root.bind('3', on_raise_press)
	root.bind('4', on_raise_press)
	root.bind('5', on_raise_press)
	root.bind('6', on_raise_press)
	root.bind('7', on_raise_press)
	root.bind('8', on_raise_press)
	root.bind('9', on_raise_press)
	root.bind('0', on_raise_press)

	root.bind("<Tab>", on_raise_press)
	root.bind("<Left>", on_raise_press)
	root.bind("<Down>", on_raise_press)
	root.bind("<Up>", on_raise_press)
	root.bind("<Right>", on_raise_press)
	root.bind('-', on_raise_press)
	root.bind('=', on_raise_press)
	root.bind('[', on_raise_press)
	root.bind(']', on_raise_press)

	root.bind('`', on_raise_press)

	if OS_CODE is "linux":
		root.bind("<Super_L>", on_raise_press)
	elif OS_CODE is "macOS":
		root.bind("<Command>", on_raise_press)
	else:
		root.bind("<Win_L>", on_raise_press)

	if OS_CODE is "linux" or OS_CODE is "windows":
		root.bind("<Alt_L>", on_raise_press)
	# else:
	# 	root.bind("<>", on_raise_press)

	root.bind('\\', on_raise_press)
	root.bind('\'', on_raise_press)

def both_layer():
	root.bind("<F1>", on_both_press)
	root.bind("<F2>", on_both_press)
	root.bind("<F3>", on_both_press)
	root.bind("<F4>", on_both_press)
	root.bind("<F5>", on_both_press)
	root.bind("<F6>", on_both_press)
	root.bind("<F7>", on_both_press)
	root.bind("<F8>", on_both_press)
	root.bind("<F9>", on_both_press)
	root.bind("<F10>", on_both_press)

	root.bind("<F11>", on_both_press)
	root.bind("<F12>", on_both_press)

def reset_canvas(layer):
	c.delete("all")
	
	if layer is "raise":
		c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img_raise)
	elif layer is "lower":
		c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img_lower)
	elif layer is "both":
		c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img_both)
	else:
		c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT, image=img_primary)
	
	c.pack()

def red_letter_box(key_coords):
	return c.create_rectangle(key_coords[0], key_coords[1], 
							  key_coords[2], key_coords[3], 
							  fill=DEFAULT_COLOR)

def red_letter_polygon(key_coords):
	return c.create_polygon(key_coords[0], key_coords[1],
							key_coords[2], key_coords[3],
							fill=DEFAULT_COLOR)

def print_key(key):
	print("Key pressed: " + key)

def visualize_keyboard_square(key, keycode, layer):
	print_key(key)
	reset_canvas(layer)
	red_letter_box(keycode)

def visualize_keyboard_polygon(key, keycode, layer):
	print_key(key)
	reset_canvas(layer)
	red_letter_polygon(keycode)

def on_q_press(event):
	visualize_keyboard_square('q', KEY_Q, "primary")

def on_w_press(event):
	visualize_keyboard_square('w', KEY_W, "primary")

def on_e_press(event):
	visualize_keyboard_square('e', KEY_E, "primary")

def on_r_press(event):
	visualize_keyboard_square('r', KEY_R, "primary")

def on_t_press(event):
	visualize_keyboard_square('t', KEY_T, "primary")

def on_y_press(event):
	visualize_keyboard_square('y', KEY_Y, "primary")

def on_u_press(event):
	visualize_keyboard_square('u', KEY_U, "primary")

def on_i_press(event):
	visualize_keyboard_square('i', KEY_I, "primary")

def on_o_press(event):
	visualize_keyboard_square('o', KEY_O, "primary")

def on_p_press(event):
	visualize_keyboard_square('p', KEY_P, "primary")

# ================================================

def on_a_press(event):
	visualize_keyboard_square('a', KEY_A, "primary")

def on_s_press(event):
	visualize_keyboard_square('s', KEY_S, "primary")

def on_d_press(event):
	visualize_keyboard_square('d', KEY_D, "primary")

def on_f_press(event):
	visualize_keyboard_square('f', KEY_F, "primary")

def on_g_press(event):
	visualize_keyboard_square('g', KEY_G, "primary")

def on_h_press(event):
	visualize_keyboard_square('h', KEY_H, "primary")

def on_j_press(event):
	visualize_keyboard_square('j', KEY_J, "primary")

def on_k_press(event):
	visualize_keyboard_square('k', KEY_K, "primary")

def on_l_press(event):
	visualize_keyboard_square('l', KEY_L, "primary")

def on_semicolon_press(event):
	visualize_keyboard_square("semicolon", KEY_SEMICOLON, "primary")

# ================================================

def on_z_press(event):
	visualize_keyboard_square('z', KEY_Z, "primary")

def on_x_press(event):
	visualize_keyboard_square('x', KEY_X, "primary")

def on_c_press(event):
	visualize_keyboard_square('c', KEY_C, "primary")

def on_v_press(event):
	visualize_keyboard_square('v', KEY_V, "primary")

def on_b_press(event):
	visualize_keyboard_square('b', KEY_B, "primary")

def on_n_press(event):
	visualize_keyboard_square('n', KEY_N, "primary")

def on_m_press(event):
	visualize_keyboard_square('m', KEY_M, "primary")

def on_comma_press(event):
	visualize_keyboard_square(',', KEY_COMMA, "primary")

def on_period_press(event):
	visualize_keyboard_square('.', KEY_PERIOD, "primary")

def on_forwardslash_press(event):
	visualize_keyboard_square('/', KEY_FORWARDSLASH, "primary")

# ================================================

def on_control_press(event):
	visualize_keyboard_square("control", KEY_CONTROL, "primary")

def on_lower_press(event):
	visualize_keyboard_polygon("lower", KEY_LOWER, "lower")

def on_space_press(event):
	visualize_keyboard_polygon("space", KEY_SPACE, "primary")

def on_backspace_press(event):
	visualize_keyboard_polygon("backspace", KEY_BACKSPACE, "primary")

def on_raise_press(event):
	visualize_keyboard_polygon("raise", KEY_RAISE, "raise")

def on_shift_press(event):
	visualize_keyboard_square("shift", KEY_SHIFT, "primary")

def on_both_press(event):
	visualize_keyboard_polygon("both", KEY_RAISE, "both")
	# visualize_keyboard_polygon("", KEY_LOWER, "both")

def main():
	reset_canvas("primary")
	listen_for_keyboard()

	root.mainloop()

main()
