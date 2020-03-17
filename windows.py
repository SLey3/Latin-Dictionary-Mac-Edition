### Imports
import tkinter as tk
from tkinter import *
from PIL import Image
from pathlib import Path

### Extra Code
picturePath1 = str(Path.home())+'/Latin_app/Pictures/Logo.jpeg'
picturePath2 = str(Path.home())+'/Latin_app/Pictures/Icon.png'
picturePath3 = str(Path.home())+'/Latin_app/Pictures/Icon.ico'
### Application screen code
window = tk.Tk()


## Window Title and Icon
# Window Icon
img = Image.open(picturePath1)
img.save("Icon.ico")
window.iconbitmap(picturePath3)
# Task Bar Icon

window.iconphoto('wm', tk.PhotoImage(file=picturePath2))
# Window Title
window.title("Latin Unit 1 Dictionary - Based on Orion Academy Latin I , Unit 1")
window.geometry('1110x950')

## Window Main Loop
window.mainloop()