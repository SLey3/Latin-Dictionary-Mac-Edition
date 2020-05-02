from tkinter import *
from pathlib import Path
import tkinter as tk
import csv

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
    return print("Text deleted", flush=True)

def clearBox():
    word_box.delete(0, END)
    newTemplate = " "
    word_box.insert(END, newTemplate)
    return print("Box cleared", flush=True)

# Csv file reader
with open('LatinWordRef.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} and {row[1]} and {row[2]}')
            line_count += 1
    print(f'Processed {line_count} lines.')
       
        
       
# Label#1
title_lbl = Label(app, text="Latin Dictionary for Latin I" ,font=('bold', 35))
title_lbl.grid(row=0, column=0)

# Label#2
global lbl_entry
global word_box
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

# clear Buttons
clear_btn1 = Button(app, text='Clear Entry', command=clearEntry)
clear_btn1.grid(row=1, column=1, pady=20)
clear_btn2 = Button(app, text='Clear box', command=clearBox)
clear_btn2.grid(row=2, column=1, pady=20)
# Program Runner
app.mainloop()