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
	root.geometry("+{}+{}".format(top_right_dimension, 
				  kbc.BACKGROUND_IMAGE_OFFSET_DOWN))

# Removes canvas of all shaded boxes before (possibly) changing layers
# and drawing a new one.  Causes window to flicker sometimes on redraw (?)
# REDO functionality if you update with key press/key release instead.
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

def highlight_square_key(key_coords):
	c.create_rectangle(key_coords[1], key_coords[2], 
							  key_coords[3], key_coords[4], 
							  fill=kbc.DEFAULT_COLOR)

def highlight_polygon_key(key_coords):
	c.create_polygon(key_coords[1], key_coords[2],
							key_coords[3], key_coords[4],
							fill=kbc.DEFAULT_COLOR)

def visualize_keyboard_square(key, keycode, layer):
	reset_canvas(layer)
	highlight_square_key(keycode)

def visualize_keyboard_polygon(key, keycode, layer):
	reset_canvas(layer)
	highlight_polygon_key(keycode)

def process_keyboard_input(event):
	key = event.Key.lower()
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

def main():
	reset_canvas(img_primary)
	hookman.KeyDown = process_keyboard_input
	root.mainloop()


# Initializes actual window for the program.
root = tk.Tk() 
window_properties()
window_size()

c = tk.Canvas(root, height=kbc.WINDOW_HEIGHT, 
			  width=kbc.WINDOW_WIDTH)

img_primary = ImageTk.PhotoImage(file=kbc.IMG_PRIMARY_PATH)
img_lower = ImageTk.PhotoImage(file=kbc.IMG_LOWER_PATH)
img_raise = ImageTk.PhotoImage(file=kbc.IMG_RAISE_PATH)
img_both = ImageTk.PhotoImage(file=kbc.IMG_BOTH_PATH)

# Sets up and starts global keyboard listener
hookman = pyxhook.HookManager()
hookman.HookKeyboard()
hookman.start()

main()
