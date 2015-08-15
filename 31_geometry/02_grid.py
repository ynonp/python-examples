"""
Grid geometry manager is
activated by the function grid(row,col)
"""

import Tkinter as tk

root = tk.Tk()

tk.Label(root,bg='red',width=20,height=4).grid(row=0,column=0)
tk.Label(root,bg='blue',width=20,height=4).grid(row=1,column=0)
tk.Label(root,bg='green',width=20,height=4).grid(row=0,column=1)
tk.Label(root,bg='gold',width=20,height=4).grid(row=1,column=1)

root.mainloop()


