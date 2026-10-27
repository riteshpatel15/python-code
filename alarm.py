import tkinter as tk
from tkinter import messagebox
from time import strftime, strptime

root = tk.Tk()
root.title("Alarm")
clock = tk.Label(root, font=("Arial", 36))
clock.pack()
alarm_time = tk.Entry(root)
alarm_time.insert(0, "07:00:00")
alarm_time.pack()
alarm = None

def update():
    global alarm
    now = strftime("%H:%M:%S")
    clock.config(text=now)
    if alarm == now:
        alarm = None
        root.bell()
        messagebox.showinfo("Alarm", "Time to wake up!")
    root.after(250, update)

def set_alarm():
    global alarm
    try:
        strptime(alarm_time.get(), "%H:%M:%S")
        alarm = alarm_time.get()
        messagebox.showinfo("Alarm", f"Alarm set for {alarm}")
    except ValueError:
        messagebox.showerror("Invalid time", "Enter time as HH:MM:SS")

tk.Button(root, text="Set alarm", command=set_alarm).pack()
update()
root.mainloop()