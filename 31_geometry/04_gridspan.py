import Tkinter as tk

root = tk.Tk()

name   = tk.Label(root, text="Name", anchor="w")
name_e = tk.Entry(root)

email = tk.Label(root, text="Email", anchor="w")
email_e = tk.Entry(root)

phone = tk.Label(root, text="Number", anchor="w")
phone_e = tk.Entry(root)

img = tk.PhotoImage(file="/Users/ynonperek/Downloads/cute.gif")
photo = tk.Label(root, image=img)
photo.image = img

name.grid(row=0, column=0, sticky="nswe")
name_e.grid(row=1, column=0, sticky="we")

email.grid(row=2, column=0, sticky="nswe")
email_e.grid(row=3, column=0, sticky="we")

phone.grid(row=4, column=0, sticky="nswe")
phone_e.grid(row=5, column=0, sticky="we")

photo.grid(row=0, column=1, rowspan=6)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

tk.mainloop()
