import tkinter as tk
import random

def add_Label():
    list1 = (name1, name2, name3, name4, name5)
    f = random.choice(list1)
    list = (kwad, krug, trel, trap, zwezd)
    i = random.choice(list)
    label2 = tk.Button(win, text=f).grid(row=1, column=1)
    label1 = tk.Button(win, image=i).grid(row=1, column=2)

win = tk.Tk()

win.config(bg="white")
win.title("Угадай число/POKS44b")
win.geometry("655x600+100+200")
win.resizable(False, False)

name1= "Кислый"
name2= "Сладкий"
name3= "Горький"
name4= "Соленый"
name5= "Острый"

list1 = (name1,name2, name3, name4, name5 )
f = random.choice(list1)
kwad = tk.PhotoImage(file="kwad.png")
krug = tk.PhotoImage(file="krug.png")
trel = tk.PhotoImage(file="trel.png")
trap = tk.PhotoImage(file="trap.png")
zwezd = tk.PhotoImage(file="zwezd.png")
list = (kwad, krug,trel,trap, zwezd)
i = random.choice(list)
bkt = tk.Button(win, text="Нажми",command=add_Label ).grid()

win.mainloop()
