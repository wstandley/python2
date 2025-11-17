"""
    This is designed to be an app that helps with working out

    Main features will be:
        - Selecting what body area the user wants to work out
        - Loading what workout, sets, reps, and weight the user should use

    Want to implement:
        - Track previous workouts
"""

import tkinter as tk
import json
import time

# Create the main window
root = tk.Tk()
root.title("Workout App")
root.geometry("450x300")
root.config(bg="black")

#TODO Functions
def display_workout(options):
    """
        This function will take what body area the user wants to workout
        Find the JSON data that correlates with that body area
        And will display the workout, sets, and reps that is recommended for the user
    """
    if options == "Chest":
        return
    elif options == "Arms":
        return
    elif options == "Back":
        return
    elif options == "Legs":
        return
    elif options == "Cardio":
        return

#TODO UI Design
# Height Entry
height_label = tk.Label(root, text="Height(in.):")
height_label.grid(row=1, column=1, sticky="w")
height_entry = tk.Entry(root, width=4)
height_entry.grid(row=1, column=2, sticky="w")
# Weight Entry
weight_label = tk.Label(root, text="Weight(lbs.):")
weight_label.grid(row=2, column=1, sticky="w")
weight_entry = tk.Entry(root, width=4)
weight_entry.grid(row=2, column=2, sticky="w")

# Body Area Options
choice_text = tk.Label(root, text="Choose what area you want to workout:")
choice_text.grid(row=3, column=2, columnspan=3, padx=5, pady=5)
# Buttons
chest_button = tk.Checkbutton(root, text="Chest", command=display_workout("Chest"))
chest_button.grid(row=4,column=1, padx=10, pady=10)
arms_button = tk.Checkbutton(root, text="Arms", command=display_workout("Arms"))
arms_button.grid(row=4, column=2, padx=10, pady=10)
back_button = tk.Checkbutton(root, text="Back", command=display_workout("Back"))
back_button.grid(row=4, column=3, padx=10, pady=10)
legs_button = tk.Checkbutton(root, text="Legs", command=display_workout("Legs"))
legs_button.grid(row=4, column=4, padx=10, pady=10)
cardio_button = tk.Checkbutton(root, text="Cardio", command=display_workout("Cardio"))
cardio_button.grid(row=4, column=5, padx=10, pady=10)


# Run App
root.mainloop()