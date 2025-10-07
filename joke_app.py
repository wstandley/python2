"""
    This is for Assignment GUI: 1.1 and 1.2 Introduction to GUI programming
"""

import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Joke")
root.geometry("300x150")

# Add a label with the joke setup
joke_label = tk.Label(root, text="Want to hear a construction joke?")
joke_label.pack(pady=20)

# Define the function to show the punchline
def show_punchline():
    messagebox.showinfo("Punchline", "Too bad, I'm still working on it 🥁")
    root.destroy()

# Add a button to show the punchline
punchline_button = tk.Button(root, text="Yes", command=show_punchline)
punchline_button.pack(pady=10)

# Run the application
root.mainloop()