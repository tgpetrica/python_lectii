import tkinter as tk
from tkinter import messagebox
from colors import CULORI, LUMINA_CULORI, BG_APP
from simon import SimonGame
import storage

class SimonSaysUI:
    def __init__ (self, root):
        self.root = root
        self.root.title("Simon Says")
        self.root.geometry("520x620")
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