"""
Some widgets create events when things
happen to them.
For example the entry also creates a <<Copy>> 
event when a user clicks Ctrl+C
"""
import Tkinter as tk

class App:
    def __init__(self):
        self.entry_text  = tk.StringVar()

        self.top    = tk.Frame()
        self.entry  = tk.Entry(self.top, textvar=self.entry_text)
        self.label  = tk.Label(self.top, text="...")

        self.entry.pack()
        self.label.pack()
        self.top.pack(ipadx=10, ipady=10)

        self.entry.bind("<<Copy>>", self.copy_handler)

    def copy_handler(self, ev):
        self.label["text"] = "Text Copied..."



root = tk.Tk()
app = App()
root.mainloop()
