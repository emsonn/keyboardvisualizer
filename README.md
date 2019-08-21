# keybordvisualizer
A constant on-screen tool that uses global key listeners to help learn a new keyboard/layout (Minidox).  Developed on Ubuntu, should work for any Linux distribution.  Does not currently work on Windows, and I have not tested with MacOS.

A QWERTY layout is assumed for this project, but can be (manually) changed by supplying your own key layout and putting it in the images folder - just make sure you keep the names matching.  A template picture (images/minidox.png) is supplied for helping to visualize your own layouts.

The locations of each key are hard-coded and are kept the same from default Minidox layouts, so key locations and possibly image paths might have to be changed if any adjustments are made.

Not every key is easily read by the computer (ex. the Fn modifier key found on laptops), and is seen here with the "raise" and "lower" keys.
To see what each layer has, hold down the layer modifier(s) and then hit any key (top-left key is usually the safest) to see what you can do in that layer.

## Dependencies: 
```
pip install pillow
```
be sure to keep the pyxhook file within the same directory as keyboardvisualizer.py

## To run: 
python3 keyboardvisualizer.py





Future notes:
PyHook is a Windows library, so pyxhook was used here.  There are some differences between these two libraries as well as how tkinter functions, which makes supporting Windows more challenging than I thought it would have been.  

pyinstaller, which was going to be used to freeze the app into a single executable, is not able to do this for any pyhook project.  pyhook3 might be useful instead. 

