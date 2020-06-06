"""
Main Application frame
"""
# Imports
from tkinter import *
from pathlib import Path
import tkinter as tk
import csv
from Modules.LatinRef import Initial
from tkinter import messagebox
import Modules.functionRef as functionRef
import Quartz
import keyboard

# Paths
picturePath1 = str(Path.home()) + '/Latin_app/Contents/Pictures/Logo.png'
csvPath = str(Path.home()) + '/Latin_app/Contents/LatinWordRef.csv'
# Window Object
app = tk.Tk()
app.title("Latin I Dictionary")
app.geometry('1110x950')
app.iconphoto('wm', tk.PhotoImage(file=picturePath1))

# Variable definitions
cmd_find_is_true = False

find_hotkey = keyboard.add_hotkey('cmd + f', None)

# Functions
def clearEntry(variable):
    """
    Clears the entry of the user
    """
    lbl_entry.delete(0, END)
    word_box.insert(0, "Entry Deleted.")
    

def clearBox(target):
    """
    Clears the action log of the application.
    """
    word_box.delete(0, END)
    word_box.insert(END, None)
    print("Box cleared")


      
        

def findReference(Log, ref, indexRef, entry):
    print("Hi")
    responce = entry.get().lower()
    print(responce)
    Log.insert(0, "Find tab created")
    try:
        index = indexRef.index(responce)
        print(index)
        ref.select_clear(0, 'end')
        ref.selection_set(index+1)
        ref.activate(index+1)
        ref.see(index+1)
        ref.selection_anchor(index+1)
    except ValueError:
        messagebox.showerror("Error 3", f'{responce} was not in mapObject')
    except UnboundLocalError as e:
        print(e)
        
        

    
def findWord(root, actionLog, userRef, indexReference, dictRef):
    """
    Finds the word or letter of the userInput and transports and higlights the word or letter.
    """
    global cmd_find_is_true
    if not cmd_find_is_true:
        fd_lbl = Label(root, text="Find:", font=('Times', 11))
        fd_lbl.grid(column=0, row=23)
        fd_ent = Entry(root)
        fd_ent.grid(column=1, row=23)
    
        fd_btn = Button(root, text="Enter", font=('Times', 11), command=lambda: findReference(actionLog, userRef, indexReference, fd_ent))
        fd_btn.grid(column=2, row=23)
        cmd_find_is_true = True

   
        
  
            
      
def wordList(listBox, dictRaw):
    """
    Opens a word list of all latin words.
    """
    global cmd_find_is_true
    global find_hotkey
    cmd_find_is_true = False
    word_box.insert(0, "List pop up created.")
    reference = functionRef.words()
    pop_up = Toplevel()
    pop_up.title("List")
    pop_up.geometry('650x925')
    print(pop_up)
    listbox = Listbox(pop_up, height=40, width=60, border=0)
    listbox.grid(row=3, column=0, columnspan=3, rowspan=7, pady=20, padx=20)
    scroll = Scrollbar(pop_up)
    scroll.grid(row=4, column=3)
    listbox.configure(yscrollcommand=scroll.set)
    scroll.configure(command=listbox.yview)
    for word in reference:
        listbox.insert('end', word)
    exit_btn = Button(pop_up, text="ok", command=pop_up.destroy)
    exit_btn.grid(column=2, row=20)  
    word_box.insert(0, "List Pop up deleted") 
    keyboard.remove_hotkey(find_hotkey)
    find_hotkey = keyboard.add_hotkey('cmd + f', findWord, args=(pop_up, word_box, listBox, reference, dictRaw))
    pop_up.update()

def help(Box):
    word_box.insert(0, "Help pop up created.")
    Help = functionRef.help()
    pop_window = Toplevel()
    pop_window.title("Help")
    pop_window.geometry('610x600')
    helpbox = Listbox(pop_window, height=30, width=60, border=0)
    helpbox.grid(column=0, row=0, columnspan=2, rowspan=3, pady=20, padx=20)
    for command in Help:
        helpbox.insert('end', command)
    
    exit_btn = Button(pop_window, text="ok", command=pop_window.destroy)
    exit_btn.grid(column=0,row=4)
    word_box.insert(0, "Help pop_up deleted")
    pop_window.update()
    
# Csv file reader
with open(csvPath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    ref = {}
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            print('\t'+ " | ".join(row[i] for i in range(len(row)) if row[i] != " "))
            word = Initial(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            ref[row[0]] = word
        line_count += 1
    print(f'Processed {line_count} lines.')
  
def call(callResponce):
    responce = lbl_entry.get()
    word = ref.get(responce, None)
    messagebox.showinfo("Definition", word)
    
    word_box.insert(0, "Word Loaded.")
    if not word and lbl_text.get():
        messagebox.showerror("Error 1", "Word either not defined or does not exist")
        word_box.delete(0, None)
        word_box.insert(0, "Error 1 Loaded")
    if not lbl_text.get():
        messagebox.showerror("Error 2", "Word not detected.")
        word_box.delete(0, None)
        word_box.insert(0, "Error 2 Loaded")
# Label#1
title_lbl = Label(app, text="Latin Dictionary for Latin I" ,font=('bold', 35))
title_lbl.grid(row=0, column=0)

# Label#2
lbl_text = StringVar()
text_lbl = Label(app, text="Search word:", font=('Times', 14), pady=20)
text_lbl.grid(row=1, column=0, sticky=W)
lbl_entry = Entry(app, textvariable=lbl_text)
lbl_entry.grid(row=1, column=0)
# Label#3
info_lbl = Label(app, text="The box is mean't as a action log for buttons to log commands.", font=('Times', 12), pady=20)
info_lbl.grid(row=2, column=0, sticky=W)
# "Enter" Button
ent_btn = Button(app, text='Enter', command=lambda: call(callResponce=lbl_entry))
ent_btn.grid(column=1 ,row=1, pady=20)
# clear Buttons
clear_btn1 = Button(app, text='Clear Entry', command=lambda: clearEntry(variable=lbl_entry))
clear_btn1.grid(row=1, column=2, pady=20)
clear_btn2 = Button(app, text='Clear Log', command=lambda: clearBox(target=word_box))
clear_btn2.grid(row=2, column=2, pady=20)
# word list button
list_btn = Button(app, text='Word List', command=lambda: wordList(word_box, ref))
list_btn.grid(column=1, row=2, pady=20)
# help button
help_btn = Button(app, text='Help', command=lambda: help(Box=word_box))
help_btn.grid(column=0, row=20, pady=20)
# Word list
word_box = Listbox(app, height=25, width=115 , border=2)
word_box.grid(row=3, column=0, columnspan=3, rowspan=4, pady=20, padx=20)
word_box.insert(1, None)
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
word_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=word_box.yview)

# Program Runner
app.mainloop()