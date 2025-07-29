import tkinter as tk
import random

parent = tk.Tk()
parent.title("Parent")
parent.geometry("400x400")

canvas = tk.Canvas(parent, width = 400, height = 400, bg = "white")
canvas.pack()

canvas.create_rectangle(200, 50, 350, 150, fill = "red", outline = "black") # static

circle = canvas.create_oval(50, 50, 130, 130, fill = "blue", outline = "green") # dinamic

def draw_circle(event):
    x = event.x
    y = event.y
    r = 15
    canvas.create_oval(x - r, y - r, x + r, y + r, fill = "green")

canvas.bind("<Button-1>", draw_circle)

canvas.itemconfig(circle, fill = "red", outline = "black", width = 5)

def move_circle():
    dx = random.choice([-20, 20])
    dy = random.choice([-20, 20])
    canvas.move(circle, dx, dy)
    parent.after(1000, move_circle) # 1000 ms = 1 s

move_circle()

parent.mainloop()