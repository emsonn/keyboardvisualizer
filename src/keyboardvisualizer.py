# References:
# 	https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
# 	https://www.tcl.tk/man/tcl8.6/TkCmd/keysyms.htm
# 	http://zetcode.com/tkinter/drawing/

import tkinter as tk
from PIL import ImageTk
from sys import platform

if platform == "linux" or platform == "linux2":
	OS_TYPE = "linux"
elif platform == "darwin":
	OS_TYPE = "macOS"
else:
	OS_TYPE = "windows"

WINDOW_HEIGHT = 210
WINDOW_WIDTH = 510
OFFSET_DOWN = 0
INSIDE_OFFSET_HEIGHT = 108
INSIDE_OFFSET_WIDTH = 257
DEFAULT_COLOR = "red"

# x1, y1, x2, y2
KEY_Q = KEY_EXCLAMATION = KEY_1 = KEY_F1 = (8, 21, 47, 60)
KEY_W = KEY_ATSIGN = KEY_2 = KEY_F2 = (49, 11, 87, 50)
KEY_E = KEY_POUNDSIGN = KEY_3 = KEY_F3 = (89, 6, 127, 44)
KEY_R = KEY_DOLLARSIGN = KEY_4 = KEY_F4 = (130, 11, 167, 50)
KEY_T = KEY_PERCENTSIGN = KEY_5 = KEY_F5 = (170, 16, 208, 54)
KEY_Y = KEY_CARET = KEY_6 = KEY_F6 = (304, 16, 342, 54)
KEY_U = KEY_AMPERSAND = KEY_7 = KEY_F7 = (345, 11, 382, 50) 
KEY_I = KEY_ASTERISK = KEY_8 = KEY_F8 = (384, 6, 422, 44)
KEY_O = KEY_LEFTPAREN = KEY_9 = KEY_F9 = (425, 11, 462, 50)
KEY_P = KEY_RIGHTPAREN = KEY_0 = KEY_F10 = (465, 21, 503, 60) 

KEY_A = KEY_ESCAPE = KEY_TAB = KEY_F11 = (8, 61, 47, 100) 
KEY_S = KEY_LEFTARROW = KEY_F12 = (49, 51, 87, 90)
KEY_D = KEY_DOWNARROW = (89, 45, 127, 85)
KEY_F = KEY_UPARROW = (130, 51, 167, 90)
KEY_G = KEY_RIGHTARROW = (170, 56, 208, 95)
KEY_H = (304, 56, 342, 95)
KEY_J = KEY_UNDERSCORE = KEY_HYPHEN = (345, 51, 382, 90) 
KEY_K = KEY_PLUSSIGN = KEY_EQUALSSIGN = (384, 45, 422, 85)
KEY_L = KEY_LEFTCURLY = KEY_LEFTBRACKET = (425, 51, 462, 90) 
KEY_SEMICOLON = KEY_RIGHTCURLY = KEY_RIGHTBRACKET = (465, 61, 503, 100)

KEY_Z = KEY_CAPSLOCK = (8, 101, 47, 140)
KEY_X = KEY_TILDE = KEY_BACKTICK = (49, 91, 87, 130)
KEY_C = KEY_SUPER = (89, 86, 127, 124)
KEY_V = KEY_LEFTALT = (130, 91, 167, 130)
KEY_B = (170, 97, 208, 134)
KEY_N = (304, 96, 342, 134)
KEY_M = (345, 91, 382, 130)
KEY_COMMA = (384, 86, 422, 124)
KEY_PERIOD = KEY_PIPE = KEY_BACKSLASH = (425, 91, 462, 130)
KEY_FORWARDSLASH = KEY_DOUBLEQUOTE = KEY_SINGLEQUOTE = (465, 101, 503, 140)

KEY_CONTROL = (105, 136, 142, 174)

# Bottom left point, top left point, top right point, bottom right point
KEY_LOWER = ((144, 175), (154, 138), (191, 148), (181, 185))
KEY_SPACE = ((182, 186), (217, 127), (250, 146), (216, 205))

KEY_BACKSPACE = KEY_RETURN = ((262, 145), (295, 126), (329, 185), (296, 205))
KEY_RAISE = ((331, 184), (321, 148), (358, 138), (368, 174))
KEY_SHIFT = KEY_DELETE = (370, 135, 407, 173)

def window_properties():
	root.title("Keyboard Visualizer")
	root.attributes("-topmost", True)
	root.focus_set()

def window_size():
	top_right_dimension = root.winfo_screenwidth()
	root.geometry("+{}+{}".format(top_right_dimension, OFFSET_DOWN))

def lower_layer():
	root.bind('!', on_exclamation_press)
	root.bind('@', on_atsign_press)
	root.bind('#', on_poundsign_press)
	root.bind('$', on_dollarsign_press)
	root.bind('%', on_percentsign_press)
	root.bind('^', on_caret_press)
	root.bind('&', on_ampersand_press)
	root.bind('*', on_asterisk_press)
	root.bind('(', on_leftparen_press)
	root.bind(')', on_rightparen_press)

	root.bind("<Escape>", on_escape_press)
	root.bind('_', on_underscore_press)
	root.bind('+', on_plussign_press)
	root.bind('{', on_leftcurly_press)
	root.bind('}', on_rightcurly_press)

	root.bind("<Caps_Lock>", on_capslock_press)
	root.bind('~', on_tilde_press)
	root.bind('|', on_pipe_press)
	root.bind('"', on_doublequote_press)
	root.bind("<Return>", on_return_press)
	
	if OS_TYPE is "linux" or OS_TYPE is "windows":
		root.bind("<Delete>", on_delete_press)

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
	
	if OS_TYPE is "linux" or OS_TYPE is "windows":
		root.bind("<BackSpace>", on_backspace_press)
	else:
		root.bind("<Delete>", on_backspace_press)

	root.bind("<Shift_L>", on_shift_press)

def raise_layer():
	root.bind('1', on_1_press)
	root.bind('2', on_2_press)
	root.bind('3', on_3_press)
	root.bind('4', on_4_press)
	root.bind('5', on_5_press)
	root.bind('6', on_6_press)
	root.bind('7', on_7_press)
	root.bind('8', on_8_press)
	root.bind('9', on_9_press)
	root.bind('0', on_0_press)

	root.bind("<Tab>", on_tab_press)
	root.bind("<Left>", on_leftarrow_press)
	root.bind("<Down>", on_downarrow_press)
	root.bind("<Up>", on_uparrow_press)
	root.bind("<Right>", on_rightarrow_press)
	root.bind('-', on_hyphen_press)
	root.bind('=', on_equalssign_press)
	root.bind('[', on_leftbracket_press)
	root.bind(']', on_rightbracket_press)

	root.bind('`', on_backtick_press)

	if OS_TYPE is "linux":
		root.bind("<Super_L>", on_super_press)
	elif OS_TYPE is "macOS":
		root.bind("<Command>", on_command_press)
	else:
		root.bind("<Win_L>", on_windows_press)

	if OS_TYPE is "linux" or OS_TYPE is "windows":
		root.bind("<Alt_L>", on_leftalt_press)
	# else:
	# 	root.bind("<>", on_raise_press)

	root.bind('\\', on_backslash_press)
	root.bind('\'', on_singlequote_press)

def both_layer():
	root.bind("<F1>", on_F1_press)
	root.bind("<F2>", on_F2_press)
	root.bind("<F3>", on_F3_press)
	root.bind("<F4>", on_F4_press)
	root.bind("<F5>", on_F5_press)
	root.bind("<F6>", on_F6_press)
	root.bind("<F7>", on_F7_press)
	root.bind("<F8>", on_F8_press)
	root.bind("<F9>", on_F9_press)
	root.bind("<F10>", on_F10_press)

	root.bind("<F11>", on_F11_press)
	root.bind("<F12>", on_F12_press)

def listen_for_keyboard():
	lower_layer()
	primary_layer()
	raise_layer()
	both_layer()

def print_key(key):
	print("Key pressed: " + key)

def reset_canvas(layer):
	c.delete("all")
	
	c.create_image(INSIDE_OFFSET_WIDTH, INSIDE_OFFSET_HEIGHT,
					   image=layer)	
	c.pack()

def red_letter_box(key_coords):
	return c.create_rectangle(key_coords[0], key_coords[1], 
							  key_coords[2], key_coords[3], 
							  fill=DEFAULT_COLOR)

def red_letter_polygon(key_coords):
	return c.create_polygon(key_coords[0], key_coords[1],
							key_coords[2], key_coords[3],
							fill=DEFAULT_COLOR)

def visualize_keyboard_square(key, keycode, layer):
	print_key(key)
	reset_canvas(layer)
	red_letter_box(keycode)

def visualize_keyboard_polygon(key, keycode, layer):
	print_key(key)
	reset_canvas(layer)
	red_letter_polygon(keycode)

def on_exclamation_press(event):
	visualize_keyboard_square('!', KEY_EXCLAMATION, img_lower)

def on_atsign_press(event):
	visualize_keyboard_square('@', KEY_ATSIGN, img_lower)

def on_poundsign_press(event):
	visualize_keyboard_square('#', KEY_POUNDSIGN, img_lower)

def on_dollarsign_press(event):
	visualize_keyboard_square('$', KEY_DOLLARSIGN, img_lower)

def on_percentsign_press(event):
	visualize_keyboard_square('%', KEY_PERCENTSIGN, img_lower)

def on_caret_press(event):
	visualize_keyboard_square('^', KEY_CARET, img_lower)

def on_ampersand_press(event):
	visualize_keyboard_square('&', KEY_AMPERSAND, img_lower)

def on_asterisk_press(event):
	visualize_keyboard_square('*', KEY_ASTERISK, img_lower)

def on_leftparen_press(event):
	visualize_keyboard_square('(', KEY_LEFTPAREN, img_lower)

def on_rightparen_press(event):
	visualize_keyboard_square(')', KEY_RIGHTPAREN, img_lower)

def on_q_press(event):
	visualize_keyboard_square('q', KEY_Q, img_primary)

def on_w_press(event):
	visualize_keyboard_square('w', KEY_W, img_primary)

def on_e_press(event):
	visualize_keyboard_square('e', KEY_E, img_primary)

def on_r_press(event):
	visualize_keyboard_square('r', KEY_R, img_primary)

def on_t_press(event):
	visualize_keyboard_square('t', KEY_T, img_primary)

def on_y_press(event):
	visualize_keyboard_square('y', KEY_Y, img_primary)

def on_u_press(event):
	visualize_keyboard_square('u', KEY_U, img_primary)

def on_i_press(event):
	visualize_keyboard_square('i', KEY_I, img_primary)

def on_o_press(event):
	visualize_keyboard_square('o', KEY_O, img_primary)

def on_p_press(event):
	visualize_keyboard_square('p', KEY_P, img_primary)

def on_1_press(event):
	visualize_keyboard_square('1', KEY_1, img_raise)

def on_2_press(event):
	visualize_keyboard_square('2', KEY_2, img_raise)

def on_3_press(event):
	visualize_keyboard_square('3', KEY_3, img_raise)

def on_4_press(event):
	visualize_keyboard_square('4', KEY_4, img_raise)

def on_5_press(event):
	visualize_keyboard_square('5', KEY_5, img_raise)

def on_6_press(event):
	visualize_keyboard_square('6', KEY_6, img_raise)

def on_7_press(event):
	visualize_keyboard_square('7', KEY_7, img_raise)

def on_8_press(event):
	visualize_keyboard_square('8', KEY_8, img_raise)

def on_9_press(event):
	visualize_keyboard_square('9', KEY_9, img_raise)

def on_0_press(event):
	visualize_keyboard_square('0', KEY_0, img_raise)

def on_F1_press(event):
	visualize_keyboard_square("F1", KEY_F1, img_both)

def on_F2_press(event):
	visualize_keyboard_square("F2", KEY_F2, img_both)

def on_F3_press(event):
	visualize_keyboard_square("F3", KEY_F3, img_both)

def on_F4_press(event):
	visualize_keyboard_square("F4", KEY_F4, img_both)

def on_F5_press(event):
	visualize_keyboard_square("F5", KEY_F5, img_both)

def on_F6_press(event):
	visualize_keyboard_square("F6", KEY_F6, img_both)

def on_F7_press(event):
	visualize_keyboard_square("F7", KEY_F7, img_both)

def on_F8_press(event):
	visualize_keyboard_square("F8", KEY_F8, img_both)

def on_F9_press(event):
	visualize_keyboard_square("F9", KEY_F9, img_both)

def on_F10_press(event):
	visualize_keyboard_square("F10", KEY_F10, img_both)

# ====================================================================

def on_escape_press(event):
	visualize_keyboard_square("Escape", KEY_ESCAPE, img_lower)

def on_underscore_press(event):
	visualize_keyboard_square('_', KEY_UNDERSCORE, img_lower)

def on_plussign_press(event):
	visualize_keyboard_square('+', KEY_PLUSSIGN, img_lower)

def on_leftcurly_press(event):
	visualize_keyboard_square('{', KEY_LEFTCURLY, img_lower)

def on_rightcurly_press(event):
	visualize_keyboard_square('}', KEY_RIGHTCURLY, img_lower)

def on_a_press(event):
	visualize_keyboard_square('a', KEY_A, img_primary)

def on_s_press(event):
	visualize_keyboard_square('s', KEY_S, img_primary)

def on_d_press(event):
	visualize_keyboard_square('d', KEY_D, img_primary)

def on_f_press(event):
	visualize_keyboard_square('f', KEY_F, img_primary)

def on_g_press(event):
	visualize_keyboard_square('g', KEY_G, img_primary)

def on_h_press(event):
	visualize_keyboard_square('h', KEY_H, img_primary)

def on_j_press(event):
	visualize_keyboard_square('j', KEY_J, img_primary)

def on_k_press(event):
	visualize_keyboard_square('k', KEY_K, img_primary)

def on_l_press(event):
	visualize_keyboard_square('l', KEY_L, img_primary)

def on_semicolon_press(event):
	visualize_keyboard_square(';', KEY_SEMICOLON, img_primary)

def on_tab_press(event):
	visualize_keyboard_square("tab", KEY_TAB, img_raise)

def on_leftarrow_press(event):
	visualize_keyboard_square("left arrow", KEY_LEFTARROW, img_raise)

def on_downarrow_press(event):
	visualize_keyboard_square("down arrow", KEY_DOWNARROW, img_raise)

def on_uparrow_press(event):
	visualize_keyboard_square("up arrow", KEY_UPARROW, img_raise)

def on_rightarrow_press(event):
	visualize_keyboard_square("right arrow", KEY_RIGHTARROW, img_raise)

def on_hyphen_press(event):
	visualize_keyboard_square('-', KEY_HYPHEN, img_raise)

def on_equalssign_press(event):
	visualize_keyboard_square('=', KEY_EQUALSSIGN, img_raise)

def on_leftbracket_press(event):
	visualize_keyboard_square('[', KEY_LEFTBRACKET, img_raise)

def on_rightbracket_press(event):
	visualize_keyboard_square(']', KEY_RIGHTBRACKET, img_raise)

def on_F11_press(event):
	visualize_keyboard_square("F11", KEY_F11, img_both)

def on_F12_press(event):
	visualize_keyboard_square("F12", KEY_F12, img_both)

# ====================================================================

def on_capslock_press(event):
	visualize_keyboard_square("CAPSLOCK", KEY_CAPSLOCK, img_lower)

def on_tilde_press(event):
	visualize_keyboard_square('~', KEY_TILDE, img_lower)

def on_pipe_press(event):
	visualize_keyboard_square('|', KEY_PIPE, img_lower)

def on_doublequote_press(event):
	visualize_keyboard_square('"', KEY_DOUBLEQUOTE, img_lower)

def on_return_press(event):
	visualize_keyboard_square("Return", KEY_RETURN, img_lower)

def on_z_press(event):
	visualize_keyboard_square('z', KEY_Z, img_primary)

def on_x_press(event):
	visualize_keyboard_square('x', KEY_X, img_primary)

def on_c_press(event):
	visualize_keyboard_square('c', KEY_C, img_primary)

def on_v_press(event):
	visualize_keyboard_square('v', KEY_V, img_primary)

def on_b_press(event):
	visualize_keyboard_square('b', KEY_B, img_primary)

def on_n_press(event):
	visualize_keyboard_square('n', KEY_N, img_primary)

def on_m_press(event):
	visualize_keyboard_square('m', KEY_M, img_primary)

def on_comma_press(event):
	visualize_keyboard_square(',', KEY_COMMA, img_primary)

def on_period_press(event):
	visualize_keyboard_square('.', KEY_PERIOD, img_primary)

def on_forwardslash_press(event):
	visualize_keyboard_square('/', KEY_FORWARDSLASH, img_primary)

def on_backtick_press(event):
	visualize_keyboard_square('`', KEY_BACKTICK, img_raise)

def on_super_press(event):
	visualize_keyboard_square("SUPER", KEY_SUPER, img_raise)

def on_command_press(event):
	visualize_keyboard_square("COMMAND", KEY_SUPER, img_raise)

def on_windows_press(event):
	visualize_keyboard_square("WINDOWS", KEY_SUPER, img_raise)

def on_leftalt_press(event):
	visualize_keyboard_square("LEFT ALT", KEY_LEFTALT, img_raise)

def on_backslash_press(event):
	visualize_keyboard_square('\\', KEY_BACKSLASH, img_raise)

def on_singlequote_press(event):
	visualize_keyboard_square('\'', KEY_SINGLEQUOTE, img_raise)

# ====================================================================

def on_control_press(event):
	visualize_keyboard_square("control", KEY_CONTROL, img_primary)

def on_space_press(event):
	visualize_keyboard_polygon("space", KEY_SPACE, img_primary)

def on_backspace_press(event):
	visualize_keyboard_polygon("backspace", KEY_BACKSPACE, img_primary)

def on_return_press(event):
	visualize_keyboard_polygon("return", KEY_RETURN, img_lower)

def on_shift_press(event):
	visualize_keyboard_square("shift", KEY_SHIFT, img_primary)

def on_delete_press(event):
	visualize_keyboard_square("delete", KEY_DELETE, img_lower)

def main():
	reset_canvas(img_primary)
	listen_for_keyboard()

	root.mainloop()

root = tk.Tk() 
window_properties()
window_size()

c = tk.Canvas(root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)

img_primary_path = "../images/minidox-primary-layer.png"
img_primary = ImageTk.PhotoImage(file=img_primary_path)

img_lower_path = "../images/minidox-lower-layer.png"
img_lower = ImageTk.PhotoImage(file=img_lower_path)

img_raise_path = "../images/minidox-raise-layer.png"
img_raise = ImageTk.PhotoImage(file=img_raise_path)

img_both_path = "../images/minidox-BOTH-layer.png"
img_both = ImageTk.PhotoImage(file=img_both_path)

main()
