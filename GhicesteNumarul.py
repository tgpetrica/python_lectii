import random

class JocGhicesteNumarul:
    """
    Utilizatorul trebuie sa ghiceasca un numar secret.

    Succes!
    """

    def __init__(self, jos: int = 1, sus: int = 100) -> None:
        # constructor
        self.jos = jos
        self.sus = sus
        self.numar_secret = random.randint(self.jos, self.sus)
        self.incercari = 0
    
    def afiseaza(self) -> None:
        """
        Logica jocului:
        Ma gandesc la un numar intre {self.jos} si {self.sus}.
        Incearca sa il ghicesti! Poti cere si indicii.
        """
    
    @staticmethod
    def este_prim(n: int) -> bool:
        if n <= 1:
            return False
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0:
                return False
        return True
    
    def ghiceste_numar(self) -> bool:
        # cerem input de la user
        raspuns = input(f"Introdu un numar intre {self.jos}-{self.sus}: ").strip()

        # validarea inputului
        try:
            ghicire = int(raspuns)
        except ValueError:
            print("Input invalid.")
            return False
        
        self.incercari += 1

        # corect

        if ghicire < self.numar_secret:
            print("Prea mic! Mai incearca!")
            return False
        
        if ghicire > self.numar_secret:
            print("Prea mare! Mai incearca!")
            return False
        
        print(f"Felicitari! Ai ghicit {self.numar_secret} in {self.incercari} incercari.")
        return True
    
    def arata_paritate(self) -> None:
        print("Numarul este par." if self.numar_secret % 2 == 0 else "Numarul este impar.")
    
    def arata_prim(self) -> None:
        print("Numarul este prim. " if self.este_prim(self.numar_secret) else "Numarul nu este prim.")

    def meniu(self) -> None:
        print(
"""
Meniul jocului:
- 1: ghicire
- 2: afla paritatea
- 3: afla daca e prim
- 4: iesire
"""
        )
    def ruleaza(self) -> None:
        
        self.meniu()

        self.afiseaza()

        while True:
            self.meniu()

            optiune = input("Alege o optiune: "). strip()

            if optiune == "1":
                if self.ghiceste_numar():
                    break
            elif optiune == "2":
                self.arata_paritate()
            elif optiune == "3":
                self.arata_prim()
            elif optiune == "4":
                print("La revedere")
                break
            else:
                print("Optiune invalida.")

if __name__ == "__main__":
    joc = JocGhicesteNumarul()
    joc.ruleaza()