# Sa se creeze o clasa care sa reprezinte un angajat al unei companii.
# Clasa sa aiba atributele: nume, prenume, varsta, functie, salariu.
# Clasa sa aiba metodele:
# - afisare_angajat() - afiseaza toate atributele angajatului intr-un fisier text
# - marire_salariu(persoana) - creste salariul angajatului
# - schimbare_functie(noua_functie) - schimba functia angajatului

class Angajat:
    def __init__(self, nume: str, prenume: str, varsta: int, functie: str, salariu: float):
        self.nume       = nume
        self.prenume    = prenume
        self.varsta     = varsta
        self.functie    = functie
        self.salariu    = salariu

    def afisare_angajat(self, nume_fisier = "angajati.txt"):
        with open(nume_fisier, "w") as f:
            f.write(f"Nume: {self.nume}\n")
            f.write(f"Prenume: {self.prenume}\n")
            f.write(f"Varsta: {self.varsta}\n")
            f.write(f"Functia: {self.functie}\n")
            f.write(f"Salariul: {self.salariu}\n")
    
    # Obs. Daca nu se specifica numele fisierului la apelul afisare_angajat(), by default se va salva in angajati.txt
    # Daca se specifica un alt fisier destinatie, atunci in acela se va realiza afisarea.

    def marire_salariu(self, procent):
        if procent > 0:
            self.salariu += self.salariu * procent / 100
        else:
            print("Procentul trebuie sa fie pozitiv.")
    
    def schimbare_functie(self, noua_functie):
        self.functie = noua_functie

a1 = Angajat("Popescu", "Ion", 19, "Programator Junior", 3500)

a1.afisare_angajat() # by default se salveaza in angajati.txt

a1.marire_salariu(10)
a1.afisare_angajat("angajati_1.txt")

a1.schimbare_functie("Tester")
a1.afisare_angajat("angajati_2.txt")