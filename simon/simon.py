import random
from colors import CULORI

class SimonGame:
    def __init__(self):
        self.secventa = []
        self.input_utilizator = []
        self.scor = 0
        self.joc_inceput = False
    
    def start(self):
        self.secventa = []
        self.input_utilizator = []
        self.scor = 0
        self.joc_inceput = True
        self.adauga_pas()

    def adauga_pas(self):
        culori_disponibile = list(CULORI.keys())
        culoare = random.choice(culori_disponibile)
        self.secventa.append(culoare)
        self.input_utilizator = []
    
    def inregistrare_input(self, culoare):
        # tuple (corect, runda)
        if not self.joc_inceput:
            return (False, False)

        self.input_utilizator.append(culoare)

        index = len(self.input_utilizator) - 1
        corect = (self.input_utilizator[index] == self.secventa[index])

        if not corect:
            self.joc_inceput = False
            return (False, False)

        runda = (len(self.input_utilizator) == len(self.secventa))
        if runda:
            self.scor += 1
        
        return (True, runda)