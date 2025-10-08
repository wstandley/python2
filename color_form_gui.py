"""
    This is for assignment GUI: 1.4 Coloring your widgets
"""

import tkinter as tk

root = tk.Tk()
root.title("Form")

# Press and Release Functions
def buttonpress1(event):
    event.widget.config(bg='black', fg='white')
    
def buttonpress2(event):
    event.widget.config(bg='white', fg='red')

def buttonpress3(event):
    event.widget.config(bg='white', fg='blue')

def buttonrelease1(event):
    event.widget.config(bg='white', fg='black')
    
def buttonrelease2(event):
    event.widget.config(bg='red', fg='white')

def buttonrelease3(event):
    event.widget.config(bg='blue', fg='white')

# Create Buttons
button1 = tk.Button(root, text="Button 1", bg='white', fg='black', pady=5)
button2 = tk.Button(root, text="Button 2", bg='red', fg='white', pady=5)
button3 = tk.Button(root, text="Button 3", bg='blue', fg='white', pady=5)

# Bind Buttons
button1.bind("<ButtonPress-1>", buttonpress1)
button1.bind("<ButtonRelease-1>", buttonrelease1)

button2.bind("<ButtonPress-1>", buttonpress2)
button2.bind("<ButtonRelease-1>", buttonrelease2)

button3.bind("<ButtonPress-1>", buttonpress3)
button3.bind("<ButtonRelease-1>", buttonrelease3)

# Create Labels
button1_label = tk.Label(root, text="Press Button 1: ")
button2_label = tk.Label(root, text="Press Button 2: ")
button3_label = tk.Label(root, text="Press Button 3: ")

# Grid Layout
button1.grid(row=1, column=2, pady=5)
button1_label.grid(row=1, column=1, pady=5)

button2.grid(row=2, column=2, pady=5)
button2_label.grid(row=2, column=1, pady=5)

button3.grid(row=3, column=2, pady=5)
button3_label.grid(row=3, column=1, pady=5)

root.mainloop()