"""
Label - Name
TextEntry

Labl - Email
TextEntry

Button - Submit
"""


import Tkinter as tk

root = tk.Tk()

tk.Label(root, text="Name:", anchor="w").pack(fill="x")
tk.Entry(root).pack(fill="x")

tk.Label(root,text="Email:", anchor="w").pack(fill="x")
tk.Entry(root).pack(fill="x")

tk.Button(root,text="Submit").pack(fill="x")

root.mainloop()

