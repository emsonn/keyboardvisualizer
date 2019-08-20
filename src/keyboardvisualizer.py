# References:
# 	https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
# 	https://www.tcl.tk/man/tcl8.6/TkCmd/keysyms.htm
# 	http://zetcode.com/tkinter/drawing/

import tkinter as tk
from PIL import ImageTk
import keyboardconstants as kbc
import pyxhook
import sys

def window_properties():
	root.title("Keyboard Visualizer")
	root.attributes("-topmost", True)

def window_size():
	top_right_dimension = root.winfo_screenwidth()
	root.geometry("+{}+{}".format(top_right_dimension, kbc.OFFSET_DOWN))

def print_key(key):
	print("Key pressed: " + key)

def reset_canvas(layer):
	c.delete("all")
	
	if layer == kbc.LOWER:
		layer = img_lower
	
	elif layer == kbc.RAISE:
		layer = img_raise

	elif layer == kbc.BOTH:
		layer = img_both

	else:
		layer = img_primary

	c.create_image(kbc.BACKGROUND_IMAGE_OFFSET_WIDTH, 
				   kbc.BACKGROUND_IMAGE_OFFSET_HEIGHT, image=layer)	
	c.pack()

def red_letter_box(key_coords):
	return c.create_rectangle(key_coords[1], key_coords[2], 
							  key_coords[3], key_coords[4], 
							  fill=kbc.DEFAULT_COLOR)

def red_letter_polygon(key_coords):
	return c.create_polygon(key_coords[1], key_coords[2],
							key_coords[3], key_coords[4],
							fill=kbc.DEFAULT_COLOR)

def visualize_keyboard_square(key, keycode, layer):
	print_key(key)
	reset_canvas(layer)
	red_letter_box(keycode)

def visualize_keyboard_polygon(key, keycode, layer):
	print_key(key)
	reset_canvas(layer)
	red_letter_polygon(keycode)

def test_function(event):
	key = event.Key
	key = key.lower()
	dict = kbc.all_keys

	if key not in dict:
		return

	key_shape = dict[key][0]
	key_location = dict[key]
	key_layer = dict[key][-1]

	if key_shape is kbc.SQUARE:
		visualize_keyboard_square(key, key_location, key_layer)

	else:
		visualize_keyboard_polygon(key, key_location, key_layer)
			
	if event.Key == "Shift_R":
		hookman.cancel() 
		sys.exit(0)

def main():
	reset_canvas(img_primary)
	hookman.KeyDown = test_function
	root.mainloop()


root = tk.Tk() 
window_properties()
window_size()

c = tk.Canvas(root, height=kbc.WINDOW_HEIGHT, 
			  width=kbc.WINDOW_WIDTH)

img_primary = ImageTk.PhotoImage(file=kbc.IMG_PRIMARY_PATH)
img_lower = ImageTk.PhotoImage(file=kbc.IMG_LOWER_PATH)
img_raise = ImageTk.PhotoImage(file=kbc.IMG_RAISE_PATH)
img_both = ImageTk.PhotoImage(file=kbc.IMG_BOTH_PATH)

hookman = pyxhook.HookManager()
hookman.HookKeyboard()

hookman.start()
main()
