import tkinter as tk
import tkinter.filedialog

class App:
    def __init__(self):
        self.top = tk.Frame()
        self.btn = tk.Button(self.top, text="Choose File", command=self.select_file)
        self.text = tk.Text(self.top)

        self.btn.pack()
        self.text.pack()
        self.top.pack()

    def select_file(self):
        fname = tkinter.filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("Python files", "*.py")])
        with open(fname, "r") as f:
            txt = f.read()
            self.text.delete(1.0, tk.END)
            self.text.insert(1.0, txt)

root = tk.Tk()
app = App()
root.mainloop()
