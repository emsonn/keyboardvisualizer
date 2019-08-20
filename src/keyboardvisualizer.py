# References:
# 	https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
# 	https://www.tcl.tk/man/tcl8.6/TkCmd/keysyms.htm
# 	http://zetcode.com/tkinter/drawing/

import tkinter as tk
from PIL import ImageTk
import keyboardconstants as kbc
import pyxhook
import time

def window_properties():
	root.title("Keyboard Visualizer")
	root.attributes("-topmost", True)
	root.focus_set()

def window_size():
	top_right_dimension = root.winfo_screenwidth()
	root.geometry("+{}+{}".format(top_right_dimension, kbc.OFFSET_DOWN))

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
	
	if kbc.OS_TYPE is "linux" or kbc.OS_TYPE is "windows":
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
	
	if kbc.OS_TYPE is "linux" or kbc.OS_TYPE is "windows":
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

	if kbc.OS_TYPE is "linux":
		root.bind("<Super_L>", on_super_press)
	elif kbc.OS_TYPE is "macOS":
		root.bind("<Command>", on_command_press)
	else:
		root.bind("<Win_L>", on_windows_press)

	if kbc.OS_TYPE is "linux" or kbc.OS_TYPE is "windows":
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

def listen_for_keyboard(event):
	lower_layer()
	primary_layer()
	raise_layer()
	both_layer()

def print_key(key):
	print("Key pressed: " + key)

def reset_canvas(layer):
	c.delete("all")
	
	c.create_image(kbc.INSIDE_OFFSET_WIDTH, 
				   kbc.INSIDE_OFFSET_HEIGHT, image=layer)	
	c.pack()

def red_letter_box(key_coords):
	return c.create_rectangle(key_coords[0], key_coords[1], 
							  key_coords[2], key_coords[3], 
							  fill=kbc.DEFAULT_COLOR)

def red_letter_polygon(key_coords):
	return c.create_polygon(key_coords[0], key_coords[1],
							key_coords[2], key_coords[3],
							fill=kbc.DEFAULT_COLOR)

def visualize_keyboard_square(key, keycode, layer):
	print_key(key)
	reset_canvas(layer)
	red_letter_box(keycode)

def visualize_keyboard_polygon(key, keycode, layer):
	print_key(key)
	reset_canvas(layer)
	red_letter_polygon(keycode)

def on_exclamation_press(event):
	visualize_keyboard_square('!', kbc.KEY_EXCLAMATION, img_lower)

def on_atsign_press(event):
	visualize_keyboard_square('@', kbc.KEY_ATSIGN, img_lower)

def on_poundsign_press(event):
	visualize_keyboard_square('#', kbc.KEY_POUNDSIGN, img_lower)

def on_dollarsign_press(event):
	visualize_keyboard_square('$', kbc.KEY_DOLLARSIGN, img_lower)

def on_percentsign_press(event):
	visualize_keyboard_square('%', kbc.KEY_PERCENTSIGN, img_lower)

def on_caret_press(event):
	visualize_keyboard_square('^', kbc.KEY_CARET, img_lower)

def on_ampersand_press(event):
	visualize_keyboard_square('&', kbc.KEY_AMPERSAND, img_lower)

def on_asterisk_press(event):
	visualize_keyboard_square('*', kbc.KEY_ASTERISK, img_lower)

def on_leftparen_press(event):
	visualize_keyboard_square('(', kbc.KEY_LEFTPAREN, img_lower)

def on_rightparen_press(event):
	visualize_keyboard_square(')', kbc.KEY_RIGHTPAREN, img_lower)

def on_q_press(event):
	visualize_keyboard_square('q', kbc.KEY_Q, img_primary)

def on_w_press(event):
	visualize_keyboard_square('w', kbc.KEY_W, img_primary)

def on_e_press(event):
	visualize_keyboard_square('e', kbc.KEY_E, img_primary)

def on_r_press(event):
	visualize_keyboard_square('r', kbc.KEY_R, img_primary)

def on_t_press(event):
	visualize_keyboard_square('t', kbc.KEY_T, img_primary)

def on_y_press(event):
	visualize_keyboard_square('y', kbc.KEY_Y, img_primary)

def on_u_press(event):
	visualize_keyboard_square('u', kbc.KEY_U, img_primary)

def on_i_press(event):
	visualize_keyboard_square('i', kbc.KEY_I, img_primary)

def on_o_press(event):
	visualize_keyboard_square('o', kbc.KEY_O, img_primary)

def on_p_press(event):
	visualize_keyboard_square('p', kbc.KEY_P, img_primary)

def on_1_press(event):
	visualize_keyboard_square('1', kbc.KEY_1, img_raise)

def on_2_press(event):
	visualize_keyboard_square('2', kbc.KEY_2, img_raise)

def on_3_press(event):
	visualize_keyboard_square('3', kbc.KEY_3, img_raise)

def on_4_press(event):
	visualize_keyboard_square('4', kbc.KEY_4, img_raise)

def on_5_press(event):
	visualize_keyboard_square('5', kbc.KEY_5, img_raise)

def on_6_press(event):
	visualize_keyboard_square('6', kbc.KEY_6, img_raise)

def on_7_press(event):
	visualize_keyboard_square('7', kbc.KEY_7, img_raise)

def on_8_press(event):
	visualize_keyboard_square('8', kbc.KEY_8, img_raise)

def on_9_press(event):
	visualize_keyboard_square('9', kbc.KEY_9, img_raise)

def on_0_press(event):
	visualize_keyboard_square('0', kbc.KEY_0, img_raise)

def on_F1_press(event):
	visualize_keyboard_square("F1", kbc.KEY_F1, img_both)

def on_F2_press(event):
	visualize_keyboard_square("F2", kbc.KEY_F2, img_both)

def on_F3_press(event):
	visualize_keyboard_square("F3", kbc.KEY_F3, img_both)

def on_F4_press(event):
	visualize_keyboard_square("F4", kbc.KEY_F4, img_both)

def on_F5_press(event):
	visualize_keyboard_square("F5", kbc.KEY_F5, img_both)

def on_F6_press(event):
	visualize_keyboard_square("F6", kbc.KEY_F6, img_both)

def on_F7_press(event):
	visualize_keyboard_square("F7", kbc.KEY_F7, img_both)

def on_F8_press(event):
	visualize_keyboard_square("F8", kbc.KEY_F8, img_both)

def on_F9_press(event):
	visualize_keyboard_square("F9", kbc.KEY_F9, img_both)

def on_F10_press(event):
	visualize_keyboard_square("F10", kbc.KEY_F10, img_both)

# ====================================================================

def on_escape_press(event):
	visualize_keyboard_square("Escape", kbc.KEY_ESCAPE, img_lower)

def on_underscore_press(event):
	visualize_keyboard_square('_', kbc.KEY_UNDERSCORE, img_lower)

def on_plussign_press(event):
	visualize_keyboard_square('+', kbc.KEY_PLUSSIGN, img_lower)

def on_leftcurly_press(event):
	visualize_keyboard_square('{', kbc.KEY_LEFTCURLY, img_lower)

def on_rightcurly_press(event):
	visualize_keyboard_square('}', kbc.KEY_RIGHTCURLY, img_lower)

def on_a_press(event):
	visualize_keyboard_square('a', kbc.KEY_A, img_primary)

def on_s_press(event):
	visualize_keyboard_square('s', kbc.KEY_S, img_primary)

def on_d_press(event):
	visualize_keyboard_square('d', kbc.KEY_D, img_primary)

def on_f_press(event):
	visualize_keyboard_square('f', kbc.KEY_F, img_primary)

def on_g_press(event):
	visualize_keyboard_square('g', kbc.KEY_G, img_primary)

def on_h_press(event):
	visualize_keyboard_square('h', kbc.KEY_H, img_primary)

def on_j_press(event):
	visualize_keyboard_square('j', kbc.KEY_J, img_primary)

def on_k_press(event):
	visualize_keyboard_square('k', kbc.KEY_K, img_primary)

def on_l_press(event):
	visualize_keyboard_square('l', kbc.KEY_L, img_primary)

def on_semicolon_press(event):
	visualize_keyboard_square(';', kbc.KEY_SEMICOLON, img_primary)

def on_tab_press(event):
	visualize_keyboard_square("tab", kbc.KEY_TAB, img_raise)

def on_leftarrow_press(event):
	visualize_keyboard_square("left arrow", kbc.KEY_LEFTARROW, img_raise)

def on_downarrow_press(event):
	visualize_keyboard_square("down arrow", kbc.KEY_DOWNARROW, img_raise)

def on_uparrow_press(event):
	visualize_keyboard_square("up arrow", kbc.KEY_UPARROW, img_raise)

def on_rightarrow_press(event):
	visualize_keyboard_square("right arrow", kbc.KEY_RIGHTARROW, img_raise)

def on_hyphen_press(event):
	visualize_keyboard_square('-', kbc.KEY_HYPHEN, img_raise)

def on_equalssign_press(event):
	visualize_keyboard_square('=', kbc.KEY_EQUALSSIGN, img_raise)

def on_leftbracket_press(event):
	visualize_keyboard_square('[', kbc.KEY_LEFTBRACKET, img_raise)

def on_rightbracket_press(event):
	visualize_keyboard_square(']', kbc.KEY_RIGHTBRACKET, img_raise)

def on_F11_press(event):
	visualize_keyboard_square("F11", kbc.KEY_F11, img_both)

def on_F12_press(event):
	visualize_keyboard_square("F12", kbc.KEY_F12, img_both)

# ====================================================================

def on_capslock_press(event):
	visualize_keyboard_square("CAPSLOCK", kbc.KEY_CAPSLOCK, img_lower)

def on_tilde_press(event):
	visualize_keyboard_square('~', kbc.KEY_TILDE, img_lower)

def on_pipe_press(event):
	visualize_keyboard_square('|', kbc.KEY_PIPE, img_lower)

def on_doublequote_press(event):
	visualize_keyboard_square('"', kbc.KEY_DOUBLEQUOTE, img_lower)

def on_return_press(event):
	visualize_keyboard_square("Return", kbc.KEY_RETURN, img_lower)

def on_z_press(event):
	visualize_keyboard_square('z', kbc.KEY_Z, img_primary)

def on_x_press(event):
	visualize_keyboard_square('x', kbc.KEY_X, img_primary)

def on_c_press(event):
	visualize_keyboard_square('c', kbc.KEY_C, img_primary)

def on_v_press(event):
	visualize_keyboard_square('v', kbc.KEY_V, img_primary)

def on_b_press(event):
	visualize_keyboard_square('b', kbc.KEY_B, img_primary)

def on_n_press(event):
	visualize_keyboard_square('n', kbc.KEY_N, img_primary)

def on_m_press(event):
	visualize_keyboard_square('m', kbc.KEY_M, img_primary)

def on_comma_press(event):
	visualize_keyboard_square(',', kbc.KEY_COMMA, img_primary)

def on_period_press(event):
	visualize_keyboard_square('.', kbc.KEY_PERIOD, img_primary)

def on_forwardslash_press(event):
	visualize_keyboard_square('/', kbc.KEY_FORWARDSLASH, img_primary)

def on_backtick_press(event):
	visualize_keyboard_square('`', kbc.KEY_BACKTICK, img_raise)

def on_super_press(event):
	visualize_keyboard_square("SUPER", kbc.KEY_SUPER, img_raise)

def on_command_press(event):
	visualize_keyboard_square("COMMAND", kbc.KEY_SUPER, img_raise)

def on_windows_press(event):
	visualize_keyboard_square("WINDOWS", kbc.KEY_SUPER, img_raise)

def on_leftalt_press(event):
	visualize_keyboard_square("LEFT ALT", kbc.KEY_LEFTALT, img_raise)

def on_backslash_press(event):
	visualize_keyboard_square('\\', kbc.KEY_BACKSLASH, img_raise)

def on_singlequote_press(event):
	visualize_keyboard_square('\'', kbc.KEY_SINGLEQUOTE, img_raise)

# ====================================================================

def on_control_press(event):
	visualize_keyboard_square("control", kbc.KEY_CONTROL, img_primary)

def on_space_press(event):
	visualize_keyboard_polygon("space", kbc.KEY_SPACE, img_primary)

def on_backspace_press(event):
	visualize_keyboard_polygon("backspace", kbc.KEY_BACKSPACE, img_primary)

def on_return_press(event):
	visualize_keyboard_polygon("return", kbc.KEY_RETURN, img_lower)

def on_shift_press(event):
	visualize_keyboard_square("shift", kbc.KEY_SHIFT, img_primary)

def on_delete_press(event):
	visualize_keyboard_square("delete", kbc.KEY_DELETE, img_lower)

def main():
	reset_canvas(img_primary)
	# listen_for_keyboard()
	
	hookman = pyxhook.HookManager()
	hookman.HookKeyboard()
	hookman.start()
	running = True
	hookman.KeyDown = listen_for_keyboard

	while running:
		time.sleep(0.1)

	root.mainloop()
	hookman.cancel()



root = tk.Tk() 
window_properties()
window_size()

c = tk.Canvas(root, height=kbc.WINDOW_HEIGHT, 
			  width=kbc.WINDOW_WIDTH)

img_primary = ImageTk.PhotoImage(file=kbc.IMG_PRIMARY_PATH)
img_lower = ImageTk.PhotoImage(file=kbc.IMG_LOWER_PATH)
img_raise = ImageTk.PhotoImage(file=kbc.IMG_RAISE_PATH)
img_both = ImageTk.PhotoImage(file=kbc.IMG_BOTH_PATH)

main()
