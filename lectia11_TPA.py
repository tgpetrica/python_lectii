# Creeaza o aplicatie GUI folosing tkinter care sa permita utilizatorului sa gestioneze
# o lista de cumparaturi, folosind urmatoarele functionalitati:
#   O caseta de text (Entry) unde utilizatorul poate introduce un produs nou.
#   Un buton "Adauga" care adauga produsul in lista si actualizeaza afisajul.
#   O eticheta (Label) care afiseaza in timp real continutul listei.
#   Un buton "Sterge produsul ales" care sterge un produs dupa indexul introdus intr-o caseta text.
#   Un slider (Scale) pentru a modifica dimensiunea fontului in zona de afisare a listei.
#   Trei radiobutton-uri pentru schimbarea temei aplicatiei (ex. Lighter, Darker, Black-Yellow)

# Aplica principiul incapsularii folosind o clasa ListaCumparaturi pentru a gestiona lista efectiva.
# Toate actiunile trebuie sa se faca prin metodele clasei.
# Afisarea trebuie sa se actualizeze automat, dupa fiecare adaugare sau stergere.

import tkinter as tk

class ListaCumparaturi:
    def __init__(Self):
        Self.produse = []

    def adauga_produs(Self, produs: str):
        if produs.strip():
            Self.produse.append(produs.strip())
    
    def sterge_produs(Self, index: int) -> bool:
        if 0 <= index < len(Self.produse):
            Self.produse.pop(index)
            return True
        return False
    
    def get_lista_formatata(Self) -> str:
        if not Self.produse:
            return "Lista este goala."
        
        text = ""
        for index, produs in enumerate(Self.produse, start = 1):
            text += f"{index}. {produs}\n"
        return text.strip()

def actualizare_afisaj():
    lista_label.config(text = lista.get_lista_formatata())

def adauga():
    produs = entry_produs.get()
    lista.adauga_produs(produs)
    entry_produs.config(text = "")
    actualizare_afisaj()

def sterge():
    try:
        index = int(entry_index.get()) - 1
        if lista.sterge_produs(index):
            lista_label.config(fg = "black")
        else:
            lista_label.config(text = "Index invalid!", fg = "red")
        # entry_index.config(text = "")
        entry_index.delete(0, tk.END)
        actualizare_afisaj()
    except ValueError:
        lista_label.config(text = "Index invalid!", fg = "red")

def schimba_font(val):
    lista_label.config(font = ("Arial", int(val)))

def schimba_tema():
    t = tema.get()
    if t == "Luminos":
        root.config(bg = "white")
        lista_label.config(bg = "white", fg = "black", font = ("Arial", 12, "normal"))
    elif t == "Intunecat":
        root.config(bg = "#222222")
        lista_label.config(bg = "#222222", fg = "lightgray", font = ("Arial", 12, "normal"))
    elif t == "Special":
        root.config(bg = "black")
        lista_label.config(bg = "black", fg = "yellow", font = ("Arial", 12, "bold"))

lista = ListaCumparaturi()

root = tk.Tk()
root.title("Lista de cumparaturi")
root.geometry("300x500")

entry_produs = tk.Entry(root, width = 30)
entry_produs.pack(pady = 5)

buton_adauga = tk.Button(root, text = "Adauga produs", command = adauga)
buton_adauga.pack()

entry_index = tk.Entry(root, width = 5)
entry_index.pack(pady = 5)

buton_sterge = tk.Button(root, text = "Sterge produsul ales", command = sterge)
buton_sterge.pack()

lista_label = tk.Label(root, text = "Lista este goala", font = ("Arial", 12), justify = "left", fg = "black")
lista_label.pack(pady = 10)

tk.Label(root, text = "Dimensiune font: ").pack()
font_slider = tk.Scale(root, from_ = 10, to = 22, orient = "horizontal", command = schimba_font)
font_slider.set(12)
font_slider.pack()

tema = tk.StringVar(value = "Luminos")

tk.Label(root, text = "Alege tema: ").pack(pady = 5)
tk.Radiobutton(root, text = "Luminos", variable = tema, value = "Luminos", command = schimba_tema)      .pack()
tk.Radiobutton(root, text = "Intunecat", variable = tema, value = "Intunecat", command = schimba_tema)  .pack()
tk.Radiobutton(root, text = "Special", variable = tema, value = "Special", command = schimba_tema)      .pack()

root.mainloop()