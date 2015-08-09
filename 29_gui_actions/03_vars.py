""" Connect python variables to widgets
Entry <-> Variable
"""

class App(object):
    def __init__(self, root):
        self.entry_text = tk.StringVar()

        self.btn = tk.Button(root, text="Click Me", command=self.onclick)
        self.txt = tk.Label(root, textvariable=self.entry_text)
        self.ent = tk.Entry(root, textvariable=self.entry_text)
        self.btn.pack()
        self.txt.pack()
        self.ent.pack()

    def onclick(self):
        self.txt["text"] = self.entry_text.get()
        

import Tkinter as tk

root = tk.Tk()
app = App(root)

root.mainloop()


