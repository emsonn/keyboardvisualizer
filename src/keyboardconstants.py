# Code is grouped by the key in each column, starting at the top left key
# and moving to the rightmost key on the right hand.
# Code is then ordered by layers - starting at LOWER layer, and ascending
# to BOTH layer.
# Key cluster is the very last row and reads left-to-right.

from sys import platform

if platform == "linux" or platform == "linux2":
	OS_TYPE = "linux"
elif platform == "darwin":
	OS_TYPE = "macOS"
else:
	OS_TYPE = "windows"

WINDOW_HEIGHT = 210
WINDOW_WIDTH = 510
BACKGROUND_IMAGE_OFFSET_DOWN = 0
BACKGROUND_IMAGE_OFFSET_HEIGHT = 108
BACKGROUND_IMAGE_OFFSET_WIDTH = 257
DEFAULT_COLOR = "red"

IMG_PRIMARY_PATH = "../images/minidox-primary-layer.png"
IMG_LOWER_PATH = "../images/minidox-lower-layer.png"
IMG_RAISE_PATH = "../images/minidox-raise-layer.png"
IMG_BOTH_PATH = "../images/minidox-BOTH-layer.png"

LOWER = "lower"
PRIMARY = "primary"
RAISE = "raise"
BOTH = "both"

SQUARE = "square"
POLYGON = "polygon"

# SQUARE: (SQUARE, x1, y1, x2, y2, LAYER)
# POLYGON: (POLYGON, (x1, y1), (x2, y2), (x3, y3), (x4, y4), LAYER)
# 	Polygon points start at the leftmost point, going clockwise after.

'''
 KEY COORDINATES
''' 
# Top row (QWERTYUIOP)
KEY_EXCLAMATION = (SQUARE, 8, 21, 47, 60, LOWER)
KEY_Q = (SQUARE, 8, 21, 47, 60, PRIMARY)
KEY_1 = (SQUARE, 8, 21, 47, 60, RAISE)
KEY_F1 = (SQUARE, 8, 21, 47, 60, BOTH)

KEY_ATSIGN = (SQUARE, 49, 11, 87, 50, LOWER)
KEY_W = (SQUARE, 49, 11, 87, 50, PRIMARY)
KEY_2 = (SQUARE, 49, 11, 87, 50, RAISE)
KEY_F2 = (SQUARE, 49, 11, 87, 50, BOTH)

KEY_POUNDSIGN = (SQUARE, 89, 6, 127, 44, LOWER)
KEY_E = (SQUARE, 89, 6, 127, 44, PRIMARY)
KEY_3 = (SQUARE, 89, 6, 127, 44, RAISE)
KEY_F3 = (SQUARE, 89, 6, 127, 44, BOTH)

KEY_DOLLARSIGN = (SQUARE, 130, 11, 167, 50, LOWER)
KEY_R = (SQUARE, 130, 11, 167, 50, PRIMARY)
KEY_4 = (SQUARE, 130, 11, 167, 50, RAISE)
KEY_F4 = (SQUARE, 130, 11, 167, 50, BOTH)

KEY_PERCENTSIGN = (SQUARE, 170, 16, 208, 54, LOWER)
KEY_T = (SQUARE, 170, 16, 208, 54, PRIMARY)
KEY_5 = (SQUARE, 170, 16, 208, 54, RAISE)
KEY_F5 = (SQUARE, 170, 16, 208, 54, BOTH)

KEY_CARET = (SQUARE, 304, 16, 342, 54, LOWER)
KEY_Y = (SQUARE, 304, 16, 342, 54, PRIMARY)
KEY_6 = (SQUARE, 304, 16, 342, 54, RAISE)
KEY_F6 = (SQUARE, 304, 16, 342, 54, BOTH)

KEY_AMPERSAND = (SQUARE, 345, 11, 382, 50, LOWER)
KEY_U = (SQUARE, 345, 11, 382, 50, PRIMARY)
KEY_7 = (SQUARE, 345, 11, 382, 50, RAISE)
KEY_F7 = (SQUARE, 345, 11, 382, 50, BOTH)

KEY_ASTERISK = (SQUARE, 384, 6, 422, 44, LOWER)
KEY_I = (SQUARE, 384, 6, 422, 44, PRIMARY)
KEY_8 = (SQUARE, 384, 6, 422, 44, RAISE) 
KEY_F8 = (SQUARE, 384, 6, 422, 44, BOTH)

KEY_LEFTPAREN = (SQUARE, 425, 11, 462, 50, LOWER)
KEY_O = (SQUARE, 425, 11, 462, 50, PRIMARY)
KEY_9 = (SQUARE, 425, 11, 462, 50, RAISE)
KEY_F9 = (SQUARE, 425, 11, 462, 50, BOTH)

KEY_RIGHTPAREN = (SQUARE, 465, 21, 503, 60, LOWER)
KEY_P = (SQUARE, 465, 21, 503, 60, PRIMARY)
KEY_0 = (SQUARE, 465, 21, 503, 60, RAISE)
KEY_F10 = (SQUARE, 465, 21, 503, 60, BOTH) 

# Second row (ASDFGHJKL;)
KEY_ESCAPE = (SQUARE, 8, 61, 47, 100, LOWER) 
KEY_A = (SQUARE, 8, 61, 47, 100, PRIMARY) 
KEY_TAB = (SQUARE, 8, 61, 47, 100, RAISE) 
KEY_F11 = (SQUARE, 8, 61, 47, 100, BOTH) 

KEY_S = (SQUARE, 49, 51, 87, 90, PRIMARY)
KEY_LEFTARROW = (SQUARE, 49, 51, 87, 90, RAISE)
KEY_F12 = (SQUARE, 49, 51, 87, 90, BOTH)

KEY_D = (SQUARE, 89, 45, 127, 85, PRIMARY)
KEY_DOWNARROW = (SQUARE, 89, 45, 127, 85, RAISE)

KEY_F = (SQUARE, 130, 51, 167, 90, PRIMARY)
KEY_UPARROW = (SQUARE, 130, 51, 167, 90, RAISE)

KEY_G = (SQUARE, 170, 56, 208, 95, PRIMARY)
KEY_RIGHTARROW = (SQUARE, 170, 56, 208, 95, RAISE)

KEY_H = (SQUARE, 304, 56, 342, 95, PRIMARY)

KEY_UNDERSCORE = (SQUARE, 345, 51, 382, 90, LOWER)
KEY_J = (SQUARE, 345, 51, 382, 90, PRIMARY)
KEY_HYPHEN = (SQUARE, 345, 51, 382, 90, RAISE) 

KEY_PLUSSIGN = (SQUARE, 384, 45, 422, 85, LOWER)
KEY_K = (SQUARE, 384, 45, 422, 85, PRIMARY)
KEY_EQUALSSIGN = (SQUARE, 384, 45, 422, 85, RAISE)

KEY_LEFTCURLY = (SQUARE, 425, 51, 462, 90, LOWER)
KEY_L = (SQUARE, 425, 51, 462, 90, PRIMARY)
KEY_LEFTBRACKET = (SQUARE, 425, 51, 462, 90, RAISE)

KEY_RIGHTCURLY = (SQUARE, 465, 61, 503, 100, LOWER)
KEY_SEMICOLON = (SQUARE, 465, 61, 503, 100, PRIMARY)
KEY_RIGHTBRACKET = (SQUARE, 465, 61, 503, 100, RAISE)

# Third row (ZXCVBN,./)
KEY_CAPSLOCK = (SQUARE, 8, 101, 47, 140, LOWER)
KEY_Z = (SQUARE, 8, 101, 47, 140, PRIMARY)

KEY_TILDE = (SQUARE, 49, 91, 87, 130, LOWER)
KEY_X = (SQUARE, 49, 91, 87, 130, PRIMARY)
KEY_BACKTICK = (SQUARE, 49, 91, 87, 130, RAISE)

KEY_C = (SQUARE, 89, 86, 127, 124, PRIMARY)
KEY_SUPER = (SQUARE, 89, 86, 127, 124, RAISE)

KEY_V = (SQUARE, 130, 91, 167, 130, PRIMARY)
KEY_LEFTALT = (SQUARE, 130, 91, 167, 130, RAISE)

KEY_B = (SQUARE, 170, 97, 208, 134, PRIMARY)

KEY_N = (SQUARE, 304, 96, 342, 134, PRIMARY)

KEY_M = (SQUARE, 345, 91, 382, 130, PRIMARY)

KEY_COMMA = (SQUARE, 384, 86, 422, 124, PRIMARY)

KEY_PIPE = (SQUARE, 425, 91, 462, 130, LOWER)
KEY_PERIOD = (SQUARE, 425, 91, 462, 130, PRIMARY)
KEY_BACKSLASH = (SQUARE, 425, 91, 462, 130, RAISE)

KEY_DOUBLEQUOTE = (SQUARE, 465, 101, 503, 140, LOWER)
KEY_FORWARDSLASH = (SQUARE, 465, 101, 503, 140, PRIMARY)
KEY_SINGLEQUOTE = (SQUARE, 465, 101, 503, 140, RAISE)

# Bottom row - key cluster.
# Left Hand
KEY_CONTROL = (SQUARE, 105, 136, 142, 174, PRIMARY)

KEY_LOWER = (POLYGON, (144, 175), (154, 138), (191, 148), (181, 185), PRIMARY)

KEY_SPACE = (POLYGON, (182, 186), (217, 127), (250, 146), (216, 205), PRIMARY)

# Right Hand
KEY_RETURN = (POLYGON, (262, 145), (295, 126), (329, 185), (296, 205), LOWER)
KEY_BACKSPACE = (POLYGON, (262, 145), (295, 126), (329, 185), (296, 205), PRIMARY)

KEY_RAISE = (POLYGON, (331, 184), (321, 148), (358, 138), (368, 174), PRIMARY)

KEY_DELETE = (SQUARE, 370, 135, 407, 173, LOWER)
KEY_SHIFT = (SQUARE, 370, 135, 407, 173, PRIMARY)


# Keys are grouped by rows, and ordered from LOWER layer to BOTH.
# Rows are separated by a line break.
all_keys = {
	"exclam": KEY_EXCLAMATION,
	"at": KEY_ATSIGN,
	"numbersign": KEY_POUNDSIGN,
	"dollar": KEY_DOLLARSIGN,
	"percent": KEY_PERCENTSIGN,
	"asciicircum": KEY_CARET,
	"ampersand": KEY_AMPERSAND,
	"asterisk": KEY_ASTERISK,
	"parenleft": KEY_LEFTPAREN,
	"parenright": KEY_RIGHTPAREN,
	'q': KEY_Q,
	'w': KEY_W,
	'e': KEY_E,
	'r': KEY_R,
	't': KEY_T,
	'y': KEY_Y,
	'u': KEY_U,
	'i': KEY_I,
	'o': KEY_O,
	'p': KEY_P,
	'1': KEY_1,
	'2': KEY_2,
	'3': KEY_3,
	'4': KEY_4,
	'5': KEY_5,
	'6': KEY_6,
	'7': KEY_7,
	'8': KEY_8,
	'9': KEY_9,
	'0': KEY_0,
	"f1": KEY_F1,
	"f2": KEY_F2,
	"f3": KEY_F3,
	"f4": KEY_F4,
	"f5": KEY_F5,
	"f6": KEY_F6,
	"f7": KEY_F7,
	"f8": KEY_F8,
	"f9": KEY_F9,
	"f10": KEY_F10,

	"escape": KEY_ESCAPE,
	"underscore": KEY_UNDERSCORE,
	"plus": KEY_PLUSSIGN,
	"braceleft": KEY_LEFTCURLY,
	"braceright": KEY_RIGHTCURLY,
	'a': KEY_A,
	's': KEY_S,
	'd': KEY_D,
	'f': KEY_F,
	'g': KEY_G,
	'h': KEY_H,
	'j': KEY_J,
	'k': KEY_K,
	'l': KEY_L,
	"semicolon": KEY_SEMICOLON,
	"tab": KEY_TAB,
	"left": KEY_LEFTARROW,
	"down": KEY_DOWNARROW,
	"up": KEY_UPARROW,
	"right": KEY_RIGHTARROW,
	"minus": KEY_HYPHEN,
	"equal": KEY_EQUALSSIGN,
	"bracketleft": KEY_LEFTBRACKET,
	"bracketright": KEY_RIGHTBRACKET,
	"f11": KEY_F11,
	"f12": KEY_F12,

	"caps_lock": KEY_CAPSLOCK,
	"shift_l": KEY_SHIFT,
	"asciitilde": KEY_TILDE,
	"bar": KEY_PIPE,
	"quotedbl": KEY_DOUBLEQUOTE,
	"return": KEY_RETURN,
	'z': KEY_Z,
	'x': KEY_X,
	'c': KEY_C,
	'v': KEY_V,
	'b': KEY_B,
	'n': KEY_N,
	'm': KEY_M,
	"comma": KEY_COMMA,
	"period": KEY_PERIOD,
	"slash": KEY_FORWARDSLASH,
	"grave": KEY_BACKTICK,
	"super_l": KEY_SUPER,
	"alt_l": KEY_LEFTALT,
	"backslash": KEY_BACKSLASH,
	"apostrophe": KEY_SINGLEQUOTE,

	"control_l": KEY_CONTROL,
	"space": KEY_SPACE,
	"backspace": KEY_BACKSPACE,
	"return": KEY_RETURN,
	"shift_l": KEY_SHIFT,
	"delete": KEY_DELETE
}
