"""
Creating buttons in a loop
"""
import Tkinter as tk

def set_color(clr):
    f["background"] = clr

root = tk.Tk()
root.geometry("400x400")

f = tk.Frame(root)
f.pack(fill=tk.BOTH, expand=1)

colors = ['red', 'blue', 'green']

for clr in colors:
    tk.Button(f, text=clr, command=lambda color=clr: set_color(color)).pack()

f.mainloop()
