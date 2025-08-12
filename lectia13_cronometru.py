import tkinter as tk

root = tk.Tk()
root.title("Cronometru")
root.geometry("300x300")

label = tk.Label(root, text = "0 s", font = ("Arial", 16))
label.pack(pady = 20)

time = 0
running = False # cronometrul nu functioneaza

def start_timer():
    global running
    if not running:
        running = True # cronometrul functioneaza
        update()

def stop_timer():
    global running
    running = False # cronometrul nu mai functioneaza

def reset_timer():
    global time, running
    running = False # cronometrul nu mai functioneaza
    time = 0 # functia de resetare
    label.config(text = "0 s")

def update():
    global time
    if running:
        time += 1
        label.config(text = f"{time} s")
        root.after(1000, update)

btn_start = tk.Button(root, text = "Start", width = 10, command = start_timer).pack(pady = 5)

btn_stop = tk.Button(root, text = "Stop", width = 10, command = stop_timer).pack(pady = 5)

btn_reset = tk.Button(root, text = "Reset", width = 10, command = reset_timer).pack(pady = 5)

root.mainloop()