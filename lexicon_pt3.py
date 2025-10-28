"""
    This is for Assignment GUI: 2.3 A small lexicon of widgets - Part 3
"""

import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Coffee Shop Menu")

# Step 1: Create the Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Variables to store order details
num_coffees = tk.IntVar(value=0)
num_cream = tk.IntVar(value=0)
num_sugar = tk.IntVar(value=0)
num_teas = tk.IntVar(value=0)
num_lemon = tk.IntVar(value=0)
num_honey = tk.IntVar(value=0)
num_powdered_donuts = tk.IntVar(value=0)
num_glazed_donuts = tk.IntVar(value=0)
num_chocolate_donuts = tk.IntVar(value=0)
num_plain_bagels = tk.IntVar(value=0)
num_blueberry_bagels = tk.IntVar(value=0)
num_everything_bagels = tk.IntVar(value=0)

# Step 2: Create Menus
def show_drinks():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    drinks_frame = tk.Frame(root)
    drinks_frame.pack(padx=10, pady=10)

    tk.Label(drinks_frame, text="Number of Coffees:").grid(row=0, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_coffees, *range(11)).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Cream:").grid(row=1, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_cream, *range(11)).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Sugar:").grid(row=2, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_sugar, *range(11)).grid(row=2, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Teas:").grid(row=3, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_teas, *range(11)).grid(row=3, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Lemon:").grid(row=4, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_lemon, *range(11)).grid(row=4, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Honey:").grid(row=5, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_honey, *range(11)).grid(row=5, column=1, padx=10, pady=5)

def show_donuts():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    donuts_frame = tk.Frame(root)
    donuts_frame.pack(padx=10, pady=10)
    #TODO complete this section
    tk.Label(donuts_frame, text="Number of Powdered Donuts:").grid(row=0, column=0, padx=10, pady=5)
    tk.OptionMenu(donuts_frame, num_powdered_donuts, *range(11)).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(donuts_frame, text="Number of Glazed Donuts:").grid(row=1, column=0, padx=10, pady=5)
    tk.OptionMenu(donuts_frame, num_glazed_donuts, *range(11)).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(donuts_frame, text="Number of Chocolate Donuts:").grid(row=2, column=0, padx=10, pady=5)
    tk.OptionMenu(donuts_frame, num_chocolate_donuts, *range(11)).grid(row=2, column=1, padx=10, pady=5)

def show_bagels():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    bagels_frame = tk.Frame(root)
    bagels_frame.pack(padx=10, pady=10)
    #TODO complete this section
    tk.Label(bagels_frame, text="Number of Plain Bagels:").grid(row=0, column=0, padx=10, pady=5)
    tk.OptionMenu(bagels_frame, num_plain_bagels, *range(11)).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(bagels_frame, text="Number of Blueberry Bagels:").grid(row=1, column=0, padx=10, pady=5)
    tk.OptionMenu(bagels_frame, num_blueberry_bagels, *range(11)).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(bagels_frame, text="Number of Everything Bagels:").grid(row=2, column=0, padx=10, pady=5)
    tk.OptionMenu(bagels_frame, num_everything_bagels, *range(11)).grid(row=2, column=1, padx=10, pady=5)

# Create Menus and add to Menu Bar
drinks_menu = tk.Menu(menu_bar, tearoff=0)
donuts_menu = tk.Menu(menu_bar, tearoff=0)
bagels_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Drinks", menu=drinks_menu)
menu_bar.add_cascade(label="Donuts", menu=donuts_menu)
menu_bar.add_cascade(label="Bagels", menu=bagels_menu)

# Add menu items and assign commands to the menus
drinks_menu.add_command(label="Show Drinks", command=show_drinks)
donuts_menu.add_command(label="Show Donuts", command=show_donuts)
bagels_menu.add_command(label="Show Bagels", command=show_bagels)

# Function to display the order summary
def show_order():
    total_cost = num_coffees.get() * 2 + num_teas.get() * 2 + num_powdered_donuts.get() * 2 + num_glazed_donuts.get() * 1 + num_chocolate_donuts.get() * 2 + num_plain_bagels.get() * 1 + num_blueberry_bagels.get() * 2 + num_everything_bagels.get() * 4
    order = (f"Coffees: {num_coffees.get()}, Cream: {num_cream.get()}, Sugar: {num_sugar.get()}\n"
             f"Teas: {num_teas.get()}, Lemon: {num_lemon.get()}, Honey: {num_honey.get()}\n"
             f"Powdered Donuts: {num_powdered_donuts.get()}\n"
             f"Glazed Donuts: {num_glazed_donuts.get()}\n"
             f"Chocolate Donuts: {num_chocolate_donuts.get()}\n"
             f"Plain Bagels: {num_plain_bagels.get()}\n"
             f"Blueberry Bagels: {num_blueberry_bagels.get()}\n"
             f"Bagels: {num_everything_bagels.get()}\n"
             f"Total Cost: ${total_cost}")
    messagebox.showinfo("Order Summary", order)

# Create a Button to complete the order
complete_order_button = tk.Button(root, text="Complete Order", command=show_order)
complete_order_button.pack(pady=10)

# Run the application
root.mainloop()