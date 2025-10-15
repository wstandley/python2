"""
    This is for assignment GUI: 1.6 Events and how to handle them
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Form")
root.geometry("400x400")
root.configure(bg = "#1f4529")
root.background_color = "#1f4529"

# Play Song list of lyrics
september_lyrics = ["Do you remember", "The 21st night of September?", "Love was changin' the minds of pretenders", "While chasin' the clouds away", "Our hearts were ringin'", "In the key that our souls were singin'", "As we danced in the night, remember", "How the stars stole the night away, oh, yeah"]

# Lyrics Counter
lyric_counter = 0

# Button Click Counter
button_counter = 0

# Functions for buttons
def change_background():
    # Function to change background color
        if root.background_color == "#1f4529":
            new_color = "#1f2645"
        else:
            new_color = "#1f4529"

        root.configure(bg = new_color) # Configures the background color
        root.background_color = new_color # Allows for every time the button is clicked to set the new color

def play_song():
    # Function to play song lyrics one line at a time
    global lyric_counter # gets global counter

    display_lyric = september_lyrics[lyric_counter]
    song_window.config(text=display_lyric) # Display Lyric
    lyric_counter = (lyric_counter + 1) % len(september_lyrics) # continue to next lyric, will restart once all lines have printed

def count_click():
    # Function to count how many times a button is clicked
    global button_counter # gets global counter

    button_counter = (button_counter + 1) # adds it up
    counter_window.config(text = f"You've clicked this button: {button_counter} times") # Display


# Buttons to be clicked
# Background Button
change_background_button = tk.Button(root, text = "Change Background Color", command = change_background)
change_background_button.pack(pady = 10)

# Play Song Button
play_song_button = tk.Button(root, text = "Play Song", command = play_song)
play_song_button.pack(pady = 10)
# Song Window
song_window = tk.Label(root, text="", bg=root.background_color, fg="white")
song_window.pack(pady=20)

# Counter Button
count_click_button = tk.Button(root, text = "How much can you click?", command = count_click)
count_click_button.pack(pady = 10)
# Counter Window
counter_window = tk.Label(root, text="Current Count: ", bg=root.background_color, fg="white")
counter_window.pack(pady=20)

root.mainloop()