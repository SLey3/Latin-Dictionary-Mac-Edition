### Imports
import tkinter as tk
from tkinter import *
from pathlib import Path
### Extra Code
picturePath1 = str(Path.home())+'/Latin_app/Pictures/Logo.jpeg'
picturePath2 = str(Path.home())+'/Latin_app/Pictures/Icon.png'
picturePath3 = str(Path.home())+'/Latin_app/Pictures/Logo.ico'
### Application screen code
root = tk.Tk()


## Window Title, Icon, and Display
# Window Display

# Window Icon
root.wm_iconbitmap('Icon.ico')

# Task Bar Icon
root.iconphoto('wm', tk.PhotoImage(file=picturePath2))

# Window Title
root.title("Latin Unit 1 Dictionary - Based on Orion Academy Latin I , Unit 1")
root.geometry('1110x950')

## Window Main Loop
root.mainloop()