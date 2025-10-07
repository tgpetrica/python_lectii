import tkinter as tk

CELULA = 25

# X = perete, ' ' = drum

LABIRINT = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X        XX        X",
    "X         XXX      X",
    "X           X      X",
    "X   X       XXX  X X",
    "X   X      X       X",
    "X   X  XXXX    X   X",
    "X      X       X   X",
    "X    X             X",
    "XXXXXXXXXXXXXXXXXXXX"
]

CULOARE_JUCATOR = "orange"
CULOARE_PERETE = "indigo"
CULOARE_TARGET = "lime"
CULOARE_FUNDAL = "lightgreen"

class Labirint:
    def __init__(self):
        self.randuri = len(LABIRINT)
        self.coloane = len(LABIRINT[0])

        self.fereastra = tk.Tk()
        self.fereastra.title("Joc Labirint")

        self.canvas = tk.Canvas (
            self.fereastra,
            width = self.coloane * CELULA
            height = self.randuri * CELULA,
            bg = CULOARE_FUNDAL
        )
        self.canvas.pack()

        self.pereti = []
        self.tinta = None

        # l = linie, c = coloana
        self.jucator_l = 1
        self.jucator_c = 1

        self.tinta_l = self.randuri - 2
        self.tinta_c = self.coloane - 2

    def construieste_labirint(self):
        for r, linie in enumerate(LABIRINT):
            for c, coloana in enumerate(linie):
                x1, y1 = c * CELULA, r * CELULA
                x2, y2 = x1 + CELULA, y1 + CELULA
                if coloana == "X":
                    self.pereti.append(
                        self.canvas.create_rectangle(
                            x1, y1, x2, y2, 
                            fill = CULOARE_PERETE,
                            width = 0
                        )
                    )
        
        x1, y1 = self.tinta_c * CELULA, self.tinta_l * CELULA
        x2, y2 = x1 + CELULA, x2 + CELULA
        self.tinta = self.canvas.create_rectangle(
            x1, y1, x2, y2,
            fill = CULOARE_TARGET,
            width = 0
        )

