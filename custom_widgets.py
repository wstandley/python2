"""
    This is for Assignment GUI: 1.7 visiting widget properties
"""

import tkinter as tk

root = tk.Tk()
root.title("Form")
root.geometry("400x400")

# Buttons
button1 = tk.Button(root, text="Button 1", bg='white', fg='black', pady=5, cursor="hand2")
button2 = tk.Button(root, text="Button 2", bg='red', fg='white', pady=5, cursor="hand1")
button3 = tk.Button(root, text="Button 3", bg='blue', fg='white', pady=5, cursor="arrow")

# Labels
text1_label = tk.Label(root, text="Text 1", font=("Times New Roman", 12, "bold"), anchor="n")
text2_label = tk.Label(root, text="Text 2", font=("Arial", 24, "italic"), anchor="s")
text3_label = tk.Label(root, text="Text 3", font=("Georgia", 36, "underline"), anchor="e")

# Pack
button1.pack(pady=5)
button2.pack(pady=5)
button3.pack(pady=5)

text1_label.pack(pady=5)
text2_label.pack(pady=5)
text3_label.pack(pady=5)

root.mainloop()