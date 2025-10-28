"""
    This is for Assignment GUI 2.4: Shaping the main window and conversing with the user
"""

import tkinter as tk
from tkinter import messagebox

# Set root to make window
root = tk.Tk()

# Create Window Title
root.title("GUI 2.4 Assignment")

# Create Window Icon
root.iconbitmap() # Put path to icon, has to have .ico

# Show an error message box with a custom title and message
def error_message():
    response = messagebox.askokcancel("Confirmation", "Do you want to continue?")
    if response:
        messagebox.showerror("Error", "An error has occurred!") # Implementation of ok/cancel
    else:
        print("User chose Cancel")

error_button = tk.Button(root, text="Error Message", command=error_message)
error_button.pack()

# Show a warning message box with a custom title and message
def warning_message():
    response = messagebox.askokcancel("Confirmation", "Do you want to continue?")
    if response:
        messagebox.showwarning("Warning", "There was a warning")
    else:
        print("User chose Cancel")

warning_button = tk.Button(root, text="Warning Message", command=warning_message)
warning_button.pack()

# Show an informational message box with a custom title and message
def informational_message():
    response = messagebox.askokcancel("Confirmation", "Do you want to continue?")
    if response:
        messagebox.showinfo("Error", "This has information")
    else:
        print("User chose Cancel")

informational_button = tk.Button(root, text="Informational Message", command=informational_message)
informational_button.pack()

def retry_window():
    # Implement the askretrycancel function to ask the user a retry/cancel question and handle the response
    response = messagebox.askretrycancel("Retry", "Do you want to retry?")
    if response:
        print("User chose Retry")
    else:
        print("User chose Cancel")

retry_button = tk.Button(root, text="Retry Button", command=retry_window)

# Define function to ask if the user wants to quit
def close_window():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

# Create Close Window Button
close_window_button = tk.Button(root, text="Close Window", command=close_window)
close_window_button.pack()

# Implement the askyesno function to ask the user a yes/no question and handle the response
response = messagebox.askyesno("Question", "Do you want to proceed and open the app?")
if response:
    print("User chose Yes")
else:
    root.destroy()

root.mainloop()