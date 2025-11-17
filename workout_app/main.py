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

#TODO Functions
def display_workout():
    """
        This function will take what body area the user wants to workout
        Find the JSON data that correlates with that body area
        And will display the workout, sets, and reps that is recommended for the user
    """

#TODO UI Design
# Height and Weight Entry
height_lable = tk.Label(root, text="Height(in.):").grid(row=1, column=1)
height_entry = tk.Entry(root, width=4).grid(row=1, column=1, columnspan=3)

weight_lable = tk.Label(root, text="Weight(lbs.):").grid(row=2, column=1)
weight_entry = tk.Entry(root, width=4).grid(row=2, column=1, columnspan=3)

# Body Area Options
choice_text = tk.Label(root, text="Choose what area you want to workout:")
choice_text.grid(row=3, column=2, columnspan=3, padx=5, pady=5)

chest_button = tk.Checkbutton(root, text="Chest")
chest_button.grid(row=4,column=1, padx=10, pady=10)
arms_button = tk.Checkbutton(root, text="Arms")
arms_button.grid(row=4, column=2, padx=10, pady=10)
back_button = tk.Checkbutton(root, text="Back")
back_button.grid(row=4, column=3, padx=10, pady=10)
legs_button = tk.Checkbutton(root, text="Legs")
legs_button.grid(row=4, column=4, padx=10, pady=10)
cardio_button = tk.Checkbutton(root, text="Cardio")
cardio_button.grid(row=4, column=5, padx=10, pady=10)

# Load Workout Button
load_workout = tk.Button(root, text="Workout", command=display_workout)
load_workout.grid(row=5, column=3)

# Run App
root.mainloop()