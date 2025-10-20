"""
    This is for assignment GUI: 1.8 Interacting with widget methods
"""

import tkinter as tk

root = tk.Tk()
root.title("Form")
root.geometry("400x400")
root.configure(bg="black")

# Change background color to white
def change_bg_color():
    root.configure(bg="white")

# Change window size
def change_window_size():
    root.geometry("600x600")

# Change Goodbye Text
def change_goodbye_text():
    goodbye_button.config(text="Destroy!")

root.after(5000, change_bg_color)

# Goodbye Button
goodbye_button = tk.Button(root, text="Goodbye!", command=root.destroy)
goodbye_button.pack(pady=20)

# Window Size Button
window_size_button = tk.Button(root, text="Change Window Size", command=change_window_size)
window_size_button.pack(pady=20)

# Goodbye Text Button
goodbye_text_button = tk.Button(root, text="Change Goodbye Text", command=change_goodbye_text)
goodbye_text_button.pack(pady=20)

# Focus
goodbye_button.focus_set()

root.mainloop()