"""
    This is for assignment GUI: 1.5 a simple GUI application
"""

import tkinter as tk

root = tk.Tk()
root.title("Weight Converter")

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Add a label and input field for the amount
amount_label = tk.Label(frame, text="Enter the amount:")
amount_label.pack()

amount_entry = tk.Entry(frame) # Whatever the user enters gets passed to the calculate() function
amount_entry.pack()

# Add radio buttons for conversion type
conversion_type = tk.StringVar(value="lb_to_kg") # Sets the default selection to lb_to_kg, passed to calculate() function

lb_to_kg_radio = tk.Radiobutton(frame, text="Pounds to Kilograms", variable=conversion_type, value="lb_to_kg")
lb_to_kg_radio.pack()

kg_to_lb_radio = tk.Radiobutton(frame, text="Kilograms to Pounds", variable=conversion_type, value="kg_to_lb")
kg_to_lb_radio.pack()

# Add a calculate button
def calculate():
    try:
        amount = float(amount_entry.get())
        if conversion_type.get() == "lb_to_kg":
            result = amount * 0.453592
            result_label.config(text=f"{amount} lbs is {result:.2f} kg")
        else:
            result = amount / 0.453592
            result_label.config(text=f"{amount} kg is {result:.2f} lbs")
    except ValueError:
        result_label.config(text="Please enter a valid number")

calculate_button = tk.Button(frame, text="Calculate", command=calculate) # calls calculate() when pressed
calculate_button.pack()

# Add a label to display the result
result_label = tk.Label(frame, text="")
result_label.pack()

root.mainloop()