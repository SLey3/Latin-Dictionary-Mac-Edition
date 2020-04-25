from tkinter import *
from pathlib import Path
import tkinter as tk

# Paths
picturePath1 = str(Path.home()) + '/Latin_app/Pictures/Logo.png'


    

# Window Object
app = tk.Tk()
app.title("Latin Unit I Dictionary - based on Latin I of Orion Academy")
app.geometry('1110x950')
app.iconphoto('wm', tk.PhotoImage(file=picturePath1))


# Functions
def clearEntry():
    lbl_entry.delete(0, END)
    newTemplate = " "
    lbl_entry.insert(END, newTemplate)
    return print("Text deleted")

    
    

        
       
# Label#1
title_lbl = Label(app, text="Latin Dictionary for Latin I" ,font=('bold', 35))
title_lbl.grid(row=0, column=0)

# Label#2
global lbl_entry
lbl_text = StringVar()
text_lbl = Label(app, text="Search word:", font=('Times', 14), pady=20)
text_lbl.grid(row=1, column=0, sticky=W)
lbl_entry = Entry(app, textvariable=lbl_text)
lbl_entry.grid(row=1, column=0)
# Word list
word_box = Listbox(app, height=25, width=115 , border=2)
word_box.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
word_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=word_box.yview)

# clear Button
clear_btn = Button(app, text='Clear', command=clearEntry)
clear_btn.grid(row=1, column=1, pady=20)

# Program Runner
app.mainloop()