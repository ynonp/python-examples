"""
Adding actions

1. Pass command to buttons
2. Connect python variable to widget
3. Handle events and virtual events
"""

def onclick():
    btn["text"] = "Ouch!"

import Tkinter as tk

root = tk.Tk()

btn = tk.Button(root, text="Click Me", command=onclick)
btn.pack()



root.mainloop()

