"""
    This is for Assignment GUI 1.3: Settling Widgets in the Window's Interior
"""

import tkinter as tk

root = tk.Tk()
root.title("Form")

# Create Label Widgets
name_label = tk.Label(root, text="Name")
email_label = tk.Label(root, text="Email")
password_label = tk.Label(root, text="Password")

# Create Entry Widgets
name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
password_entry = tk.Entry(root)

# Place Name
name_label.grid(row=1, column=1)
name_entry.grid(row=1, column=2)

# Place Email
email_label.grid(row=2, column=1)
email_entry.grid(row=2, column=2)

# Place Password
password_label.grid(row=3, column=1)
password_entry.grid(row=3, column=2)

root.mainloop()