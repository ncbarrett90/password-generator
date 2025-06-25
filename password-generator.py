import tkinter as tk
from tkinter import ttk
import random
import string

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Variables to store user input
length_var = tk.StringVar(value="12")

# Title 
title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Password length section
length_frame = tk.Frame(root)
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length:").pack(side=tk.LEFT)
length_spinbox = tk.Spinbox(length_frame, from_=4, to=50, textvariable=length_var, width=5)
length_spinbox.pack(side=tk.LEFT, padx=5)

# Main function for tkinter
root.mainloop()