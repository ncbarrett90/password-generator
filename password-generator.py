import tkinter as tk
from tkinter import ttk
import random
import string

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Title 
title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Password length section
length_frame = tk.Frame(root)
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length:").pack(side=tk.LEFT)

# Main function for tkinter
root.mainloop()