class ListaCumparaturi:
    def __init__(self):
        self.produse = []
    
    def adauga_produs(self, produs: str):
        self.produse.append(produs)
        print(f"Produsul {produs} a fost adaugat in lista.")
    
    def afiseaza_lista(self):
        if not self.produse:
            print("Lista de cumparaturi este goala.\n")
        else:
            print("Lista de cumparaturi:\n")
            for i, produs in enumerate(self.produse, start = 1):
                print(f"{i}. {produs}")
            print()
    
    def sterge_produs(self, index):
        if 0 <= index < len(self.produse):
            sters = self.produse.pop(index)
            print(f"Produsul {sters} a fost sters.\n")
        else:
            print("Index invalid.\n")
    
def afiseaza_meniu():
    print("======== Meniu ========")
    print("1    Adauga produs")
    print("2    Afiseaza lista")
    print("3    Sterge produs")
    print("4    Iesire")
    print("=======================")

def ruleaza_aplicatia():
    lista = ListaCumparaturi() # apelez metoda __init__ din clasa

    while True:
        afiseaza_meniu()
        optiune: int = int(input("Alege o optiune (1-4): "))

        if optiune == 1:
            produs: str = input("Introdu numele produsului: ")
            lista.adauga_produs(produs)

        elif optiune == 2:
            lista.afiseaza_lista()
        
        elif optiune == 3:
            lista.afiseaza_lista()

            try:
                index: int = int(input("Introdu numarul produsului de sters: ")) - 1
                lista.sterge_produs(index)
            except ValueError:
                print("Introdu un numar valid.\n")
        
        elif optiune == 4:
            print("Aplicatia se inchide.")
            break

        else:
            print("Optiunea este invalida.\n")

ruleaza_aplicatia()


