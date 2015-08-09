"""
Graphical User Interface with Tkinter

1. Our first GUI
2. TKinter concepts
3. Packing multiple widgets
"""

import Tkinter as tk

root = tk.Tk()

# Create UI
label = tk.Label(root, text="Hello Tk")
label.pack()

# Connect UI -> Python code


# Run the mainloop
root.mainloop()

