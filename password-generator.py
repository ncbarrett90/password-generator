import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    # Get values from the GUI
    length = int(length_var.get())
    num_count = int(numbers_var.get())
    special_count = int(specials_var.get())

    # Create pool of characters
    letters = string.ascii_letters
    numebers = string.digits
    specials = string.punctuation

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Variables to store user input
length_var = tk.StringVar(value="12")
numbers_var = tk.StringVar(value="2")
specials_var = tk.StringVar(value="2")

# Title 
title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Password length section
length_frame = tk.Frame(root)
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length:").pack(side=tk.LEFT)
length_spinbox = tk.Spinbox(length_frame, from_=4, to=50, textvariable=length_var, width=5)
length_spinbox.pack(side=tk.LEFT, padx=5)

# Number count section
numbers_frame = tk.Frame(root)
numbers_frame.pack(pady=5)
tk.Label(numbers_frame, text="Number of Numebrs:").pack(side=tk.LEFT)
numbers_spinbox = tk.Spinbox(numbers_frame, from_=0, to=20, textvariable=numbers_var, width=5)
numbers_spinbox.pack(side=tk.LEFT, padx=5)

# Special character count section
specials_frame = tk.Frame(root)
specials_frame.pack(pady=5)
tk.Label(specials_frame, text="Number of Special Characters:").pack(side=tk.LEFT)
specials_spinbox = tk.Spinbox(specials_frame, from_=0, to=20, textvariable=specials_var, width=5)
specials_spinbox.pack(side=tk.LEFT, padx=5)

# Generate button
generate_btn = tk.Button(root, text="Generate Password", bg="lightblue", font=("Arial, 12"))
generate_btn.pack(pady=20)

# Start the GUI
root.mainloop()