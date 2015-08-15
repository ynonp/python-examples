"""
Geometry Management

1. pack
2. grid
"""

import Tkinter as tk

root = tk.Tk()

tk.Label(root,bg='red',height=4,width=40).pack(fill="both", side="top")
tk.Label(root,bg='blue',height=4,width=40).pack(fill="both")
tk.Label(root,bg='red',height=4,width=40).pack(fill="both")
tk.Label(root,bg='blue',height=4,width=40).pack(fill="both")


tk.Label(root,bg='green',height=4,width=20).pack(fill="both", side='left')
tk.Label(root,bg='gold',height=4,width=20).pack(fill="both", side='left')

tk.Label(root,bg='gold',height=4,width=20).pack(fill="both", side='right')
tk.Label(root,bg='green',height=4,width=20).pack(fill="both", side='right')

tk.Label(root,bg='blue',height=4,width=5).pack(fill="both")
tk.Label(root,bg='red',height=4,width=5).pack(fill="both")
tk.Label(root,bg='blue',height=4,width=5).pack(fill="both")
tk.Label(root,bg='red',height=4,width=5).pack(fill="both")


root.mainloop()

