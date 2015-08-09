import Tkinter as tk

root = tk.Tk()
top = tk.Frame()

lyrics = {
"Lucifer Sam" : """
Lucifer Sam, siam cat.
Always sitting by your side
Always by your side.""",

"Astronomy Domine" : 
"""Lime and limpid green, a second scene
A fight between the blue you once knew.
Floating down, the sound resounds
Around the icy waters underground.""",

    "See Emily Play": 
"""Emily tries but misunderstands, ah ooh
She often inclined to borrow somebody's dreams till tomorrow
There is no other day
Let's try it another way
You'll lose your mind and play
Free games for may
See Emily play""",

    "Time": 
"""Ticking away the moments that make up a dull day
Fritter and waste the hours in an off-hand way
Kicking around on a piece of ground in your home town
Waiting for someone or something to show you the way
"""
}

def show_lyrics(ev):
    sel = l.curselection()
    key = l.get(sel)
    m["text"] = lyrics[key]


lv = tk.StringVar()
l = tk.Listbox(top, listvariable=lv)
# Translate keys in lyrics to a word list wrapped in quotes
lv.set(" ".join(['"%s"' % k for k in lyrics.keys()]))
m = tk.Message(top)

l.pack(side="left", fill=tk.BOTH, expand=1)
m.pack(side="right", fill=tk.BOTH, expand=1)
top.pack()

l.bind("<<ListboxSelect>>", show_lyrics)

top.mainloop()

