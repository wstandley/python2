"""
    This is for Assignment GUI 2.5: Working with the Canvas
"""

import tkinter as tk

root = tk.Tk()
root.title("Christmas Tree")

canvas = tk.Canvas(root, width=400, height=400, bg='white', borderwidth=2)
canvas.pack()

# Create triangle for branches
canvas.create_polygon(200, 50, 250, 135, 150, 135, outline='green', fill='green', width=2)
canvas.create_polygon(200, 100, 275, 200, 125, 200, outline='green', fill='green', width=2)
canvas.create_polygon(200, 150, 300, 275, 100, 275, outline='green', fill='green', width=2)

# Create the trunk
canvas.create_rectangle(175, 275, 225, 335, outline='brown', fill='brown', width=2)

# Create Ornaments
canvas.create_oval(125, 240, 160, 275, outline='black', fill='yellow', width=2) # bottom
canvas.create_oval(170, 100, 195, 125, outline='black', fill='red', width=2) # top
canvas.create_oval(140, 175, 165, 200, outline='black', fill='red', width=2) # middle

canvas.create_oval(200, 220, 235, 255, outline='black', fill='blue', width=2) # bottom
canvas.create_oval(210, 110, 235, 135, outline='black', fill='blue', width=2) # top
canvas.create_oval(220, 165, 245, 190, outline='black', fill='yellow', width=2) # middle

# Text Message
canvas.create_text(200, 25, text="Merry Christmas!", font=('Times New Roman', 24), fill='black')

root.mainloop()