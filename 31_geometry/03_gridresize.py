"""
Resizing items in a grid requires
developer to call row/column configure
and mark cells as sticky
"""

import Tkinter as tk

root = tk.Tk()

tk.Label(root,bg='red',width=20,height=4).grid(row=0,column=0,sticky='nsew')
tk.Label(root,bg='blue',width=20,height=4).grid(row=1,column=0,sticky='nsew')
tk.Label(root,bg='green',width=20,height=4).grid(row=0,column=1,sticky='nsew')
tk.Label(root,bg='gold',width=20,height=4).grid(row=1,column=1,sticky='nsew')

root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)

root.mainloop()



