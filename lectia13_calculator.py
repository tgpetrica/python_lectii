# Scrie un program care creeaza o fereastra Tkinter cu un mini calculator care
#   sa permita utilizatorului sa efectueze doua operatii: adunarea si scaderea.
# Fereastra are doua campuri Entry pentru doua numere.
# Fereastra are doua butoane pentru cele doua operatii.
# Cand unul dintre butoane a fost apasat, sa se afiseze rezultatul operatiei
#   intr-un Label.

import tkinter as tk

root = tk.Tk()
root.title ("Calculator")

tk.Label(root, text = "Primul numar:").grid(row = 0, column = 0, padx = 10, pady = 5)
entry1 = tk.Entry(root)
entry1.grid(row = 0, column = 1, padx = 10, pady = 5)

tk.Label(root, text = "Al doilea numar:").grid(row = 1, column = 0, padx = 10, pady = 5)
entry2 = tk.Entry(root)
entry2.grid(row = 1, column = 1, padx = 10, pady = 5)

def summ():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.config(text = f"Rezultat: {num1 + num2}")
    except ValueError:
        result.config(text = "Introdu numere valide!")

def diff():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.config(text = f"Rezultat: {num1 - num2}")
    except ValueError:
        result.config(text = "Introdu numere valide!")

btn_sum = tk.Button(root, text = "Adunare", command = summ)
btn_sum.grid(row = 2, column = 0, padx = 10, pady = 5)

btn_diff = tk.Button(root, text = "Scadere", command = diff)
btn_diff.grid(row = 2, column = 1, padx = 10, pady = 5)

result = tk.Label(root, text = "Rezultat: ")
result.grid(row = 3, column = 0, columnspan = 2, pady = 15)

root.mainloop()