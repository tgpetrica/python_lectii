import tkinter as tk

def change_theme():
    selected_theme = theme.get()

    if selected_theme == "Classic":
        root.config(bg = "#f0f0f0")
        label.config(bg = "#f0f0f0", fg = "#000000")
    
    elif selected_theme == "Navy":
        root.config(bg = "#000851")
        label.config(bg = "#000851", fg = "#FFFFFF")
    
    elif selected_theme == "Coal":
        root.config(bg = "#7e7e7e")
        label.config(bg = "#7e7e7e", fg = "#090909")

def toggle_message():
    if message_var.get():
        label.config(text = "Message enabled!")
    else:
        label.config(text = "")

def change_font_size(value):
    label.config(font = ("Arial", int(value)))

root = tk.Tk()
root.title("Interactive Interface")
root.geometry("400x300")

theme = tk.StringVar(value = "Classic")

rb1 = tk.Radiobutton(root, text = "Classic", variable = theme, value = "Classic", command = change_theme)
rb1.pack()

rb2 = tk.Radiobutton(root, text = "Navy", variable = theme, value = "Navy", command = change_theme)
rb2.pack()

rb3 = tk.Radiobutton(root, text = "Coal", variable = theme, value = "Coal", command = change_theme)
rb3.pack()

message_var = tk.BooleanVar()
check = tk.Checkbutton(root, text = "Show message", variable = message_var, command = toggle_message)
check.pack()

scale = tk.Scale(root, from_ = 10, to = 20, orient = "horizontal", command = change_font_size)
scale.pack()

label = tk.Label(root, text = "Choose your options!", font = ("Arial", 14))
label.pack()

root.mainloop()