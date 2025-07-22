# Interfata grafica: Tkinter
# 
# Afiseaza titlul: Planul meu de weekend
# 
# - Contine 3 campuri text (Entry) pentru planurile de dimineata, pranz, seara 
# - un buton "Afiseaza planificarea" care preia textul din cele 3 casete si 
#       le afiseaza intr-o eticheta cu un mesaj: 
#   Dimineata: alerg | Pranz: programez | Seara: iau cina cu familia
# * extra: Daca unul dintre campuri nu a fost completat, sa se afiseze o eticheta rosie
#       "Te rog completeaza toate activitatile!"

import tkinter as tk

root = tk.Tk()
root.title("Planul meu de weekend")
root.geometry("300x400")

tk.Label(root, text = "Dimineata:").pack(anchor = "w", padx = 20)
entry_morning = tk.Entry(root, width = 40)
entry_morning.pack(pady = 5)
# entry_morning.insert(0, "Activitatea de dimineata")

tk.Label(root, text = "Pranz:").pack(anchor = "w", padx = 20)
entry_noon = tk.Entry(root, width = 40)
entry_noon.pack(pady = 5)
# entry_noon.insert(0, "Activitatea de la pranz")

tk.Label(root, text = "Seara:").pack(anchor = "w", padx = 20)
entry_evening = tk.Entry(root, width = 40)
entry_evening.pack(pady = 5)
# entry_evening.insert(0, "Activitatea de seara")

def show_schedule():
    morning = entry_morning.get().strip()
    noon    = entry_noon.   get().strip()
    evening = entry_evening.get().strip()

    if not morning or not noon or not evening:
        text.config(text = "Te rog completeaza toate activitatile!", fg = "red")
    else:
        mesaj = f"Dimineata: {morning}\nPranz: {noon}\nSeara: {evening}"
        text.config(text = mesaj, fg = "black")

button = tk.Button(root, text = "Afiseaza planificarea", command = show_schedule)
button.pack(pady = 10)

text = tk.Label(root, text = "", font = ("Arial", 12))
text.pack()

root.mainloop()
