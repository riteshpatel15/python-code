import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Clock")
clock = tk.Label(root, font=("Arial", 48))
clock.pack()

def update():
    clock.config(text=strftime("%H:%M:%S"))
    clock.after(1000, update)

update()
root.mainloop()