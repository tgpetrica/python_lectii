import tkinter as tk
from tkinter import messagebox
from colors import CULORI, LUMINA_CULORI, BG_APP
from simon import SimonGame
import storage

class SimonSaysUI:
    def __init__ (self, root):
        self.root = root
        self.root.title("Simon Says")
        self.root.geometry("520x660")
        self.root.configure(bg = BG_APP)

        self.game = SimonGame()
        self.highscore = storage.citeste_highscore()

        self.construieste_ui()
    
    def construieste_ui(self):
        self.titlu = tk.Label(self.root,
                            text = "Simon Says",
                            font = ("Arial", 24, "bold"),
                            bg = BG_APP,
                            fg = "white")

        self.titlu.pack(pady = 10)

        self.scor_label = tk.Label(self.root,
                                text = "Scor: 0     |   Highscore: " + str(self.highscore),
                                font = ("Arial", 16),
                                bg = BG_APP,
                                fg = "white")
        
        self.scor_label.pack(pady = 5)

        self.canvas = tk.Canvas(self.root,
                            width = 420,
                            height = 420,
                            bg = BG_APP,
                            highlightthickness = 0)

        self.canvas.pack(pady = 20)

        self.butoane = {}

        coordonate = [
            # culoare   x       y
            ("red",     40,     40),
            ("green",   220,    40),
            ("blue",    40,     220),
            ("yellow",  220,    220)
        ]

        for culoare, x, y in coordonate:
            patrat = self.canvas.create_rectangle(x, y, x + 160, y + 160,
                                                fill = CULORI[culoare],
                                                outline = "white", width = 3)
            self.butoane[culoare] = patrat

        self.buton_start = tk.Button(self.root, text = "Start", 
                                     font = ("Arial", 16),
                                     bg = "#55d924",
                                     fg = "white",
                                     command = self.start_joc,
                                     borderwidth = 3)
        
        self.buton_start.pack(pady = 10)

        self.info = tk.Label(self.root,
                             text = "Apasa culorile in ordinea aratata.",
                             font = ("Arial", 16),
                             bg = BG_APP,
                             fg = "white")
        
        self.info.pack()

        self.leaga_evenimente()

    def start_joc(self):
        self.game.start()
        self.buton_start.config(state = "disabled")
        self.afiseaza_secventa(index = 0)

    def afiseaza_secventa(self, index):
        if index < len(self.game.secventa):
            culoare = self.game.secventa[index]
            self.aprinde(culoare)
            self.root.after(500, self.stinge_next, culoare, index)
        else:
            pass
    
    def aprinde(self, culoare):
        self.canvas.itemconfig(self.butoane[culoare], 
                               fill = LUMINA_CULORI[culoare])
    
    def stinge(self, culoare):
        self.canvas.itemconfig(self.butoane[culoare],
                               fill = CULORI[culoare])
    
    def stinge_next(self, culoare, index):
        self.stinge(culoare)
        self.root.after(250, self.afiseaza_secventa, index + 1)

    def verifica_input(self, culoare):
        if not self.game.joc_inceput:
            return

        corect, runda_completa = self.game.inregistrare_input(culoare)

        if not corect:
            self.game_over()
            return
        
        self.aprinde(culoare)
        self.root.after(200, self.stinge, culoare)

        if runda_completa:
            self.actualizeaza_scor()
            self.root.after(500, self.pasul_urmator)

    def actualizeaza_scor(self):
        if self.game.scor > self.highscore:
            self.highscore = self.game.scor
            storage.scrie_highscore(self.highscore)

        self.scor_label.config(text = "Scor: " + 
                                str(self.game.scor) +
                                "     |   Highscore: " +
                                str(self.highscore))
    
    def pasul_urmator(self):
        self.game.adauga_pas()
        self.afiseaza_secventa(index = 0)

    def game_over(self):
        self.game.joc_inceput = False
        mesaj = "Ai pierdut! Scor final " + str(self.game.scor)
        messagebox.showinfo("Game over!", mesaj)
        self.buton_start.config(state = "normal")

    def leaga_evenimente(self):
        for culoare, item in self.butoane.items():
            def handler(event, c = culoare):
                self.verifica_input(c)
            self.canvas.tag_bind(item, "<Button-1>", handler)
