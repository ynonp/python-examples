
class App(object):
    def __init__(self, root):
        self.btn = tk.Button(root, text="Click Me", command=self.onclick)
        self.txt = tk.Label(root, text="Hello")
        self.btn.pack()
        self.txt.pack()

    def onclick(self):
        self.btn["text"] = "Ouch!"
        self.txt["text"] = "Ouch!"

import Tkinter as tk

root = tk.Tk()
app = App(root)

root.mainloop()


