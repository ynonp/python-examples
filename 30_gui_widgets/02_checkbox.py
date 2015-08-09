import Tkinter as tk

def toggle():
    print "Toggle. New state = %d" % s.get()

root = tk.Tk()
s = tk.IntVar()

m = tk.Checkbutton(
        text="Are you sure?", 
        variable=s,
        command=toggle)


m.pack()
m.mainloop()

