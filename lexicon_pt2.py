"""
    This is for Assignment GUI: 2.2 A small lexicon of widgets - Part 2
"""

import tkinter as tk

root = tk.Tk()
root.title("Widget Form")
root.geometry("300x300")

#TODO Frame Widget
this_is_frame = tk.Frame(root, bd=1, relief=tk.SUNKEN)
this_is_frame.pack(padx=10,pady=10)

#TODO Label Widget
restaurant_label = tk.Label(this_is_frame, text="Restaurant Name")
restaurant_label.pack()

#TODO Message Widget
welcome_message = tk.Message(this_is_frame, text="Welcome to our Restaurant!")
welcome_message.pack()

#TODO Label Frame
menu_labelframe = tk.LabelFrame(root, text="Menu", padx=10, pady=10)
menu_labelframe.pack(padx=10, pady=10)

menu_items = tk.Label(menu_labelframe, text="Example Dishes")
menu_items.pack()

#TODO Entry Widget
dish_entry = tk.Entry(root)
dish_entry.pack()

dish_text = tk.StringVar()
dish_text.set("Your Dish will appear here")
dynamic_label = tk.Label(root, textvariable=dish_text)
dynamic_label.pack()

def show_dish_data():
    dish_entry_data = dish_entry.get()
    dish_text.set(dish_entry_data)

button = tk.Button(root, text="Show Dish Data", command=show_dish_data)
button.pack()

root.mainloop()