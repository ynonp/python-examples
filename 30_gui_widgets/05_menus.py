import Tkinter as tk

root = tk.Tk()

def noop(): pass

menubar = tk.Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = tk.Menu(menubar)
filemenu.add_command(label="Open", command=noop)
filemenu.add_command(label="Save", command=noop)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = tk.Menu(menubar)
editmenu.add_command(label="Cut", command=noop)
editmenu.add_command(label="Copy", command=noop)
editmenu.add_command(label="Paste", command=noop)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = tk.Menu(menubar)
helpmenu.add_command(label="About", command=noop)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)
root.mainloop()

