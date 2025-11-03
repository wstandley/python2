"""
    This is for Assignment GUI: 3.1 Introduction to GUI Programming in Python
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Pocket Calculator")
root.geometry("200x200")

entry = tk.Entry(root, width=20, font=('Times New Roman', 14), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

def button_click(value):
    """
        Function to retrieve buttons value and add it to the display
    """
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_display():
    # Clear current entries
    entry.delete(0, tk.END)

def calculate_result():
    """
        Function to retrieve whats in entry label and calculate results
    """
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

# Number Buttons
number_1 = tk.Button(root, text="1", command=lambda:button_click("1"))
number_1.grid(row=1, column=0)

number_2 = tk.Button(root, text="2", command=lambda:button_click("2"))
number_2.grid(row=1, column=1)

number_3 = tk.Button(root, text="3", command=lambda:button_click("3"))
number_3.grid(row=1, column=2)

number_4 = tk.Button(root, text="4", command=lambda:button_click("4"))
number_4.grid(row=2, column=0)

number_5 = tk.Button(root, text="5", command=lambda:button_click("5"))
number_5.grid(row=2, column=1)

number_6 = tk.Button(root, text="6", command=lambda:button_click("6"))
number_6.grid(row=2, column=2)

number_7 = tk.Button(root, text="7", command=lambda:button_click("7"))
number_7.grid(row=3, column=0)

number_8 = tk.Button(root, text="8", command=lambda:button_click("8"))
number_8.grid(row=3, column=1)

number_9 = tk.Button(root, text="9", command=lambda:button_click("9"))
number_9.grid(row=3, column=2)

number_0 = tk.Button(root, text="0", command=lambda:button_click("0"))
number_0.grid(row=4, column=1)

# Calculation Buttons
equals = tk.Button(root, text="=", command=calculate_result)
equals.grid(row=4, column=2)

clear = tk.Button(root, text="c", command=clear_display)
clear.grid(row=4, column=0)

divide = tk.Button(root, text="/", command=lambda:button_click("/"))
divide.grid(row=1, column=3)

multiply = tk.Button(root, text="x", command=lambda:button_click("*"))
multiply.grid(row=2, column=3)

minus = tk.Button(root, text="-", command=lambda:button_click("-"))
minus.grid(row=3, column=3)

addition = tk.Button(root, text="+", command=lambda:button_click("+"))
addition.grid(row=4, column=3)

root.mainloop()