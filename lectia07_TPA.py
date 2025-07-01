# Sa se descrie o clasa care sa reprezinte o masina.
# Clasa sa aiba atributele: marca, model, an_fabricatie,
# culoare, viteza_maxima, pret.
# Clasa sa aiba metodele:
# - afisare_masina() - afiseaza toate atributele masinii
# - accelereaza(viteza) - creste viteza masinii cu valoarea data
# - franeaza(viteza) - scade viteza masinii cu valoarea data
# - setare_pret(pret) - seteaza pretul masinii

class Masina:
    def __init__(self, marca: str, model: str, an_fabricatie: int,
                 culoare: str, viteza_maxima: int, pret: int):
        self.marca = marca
        self.model = model
        self.an_fabricatie = an_fabricatie
        self.culoare = culoare
        self.viteza_maxima = viteza_maxima
        self.pret = pret
        self.viteza_actuala = 0
    
    def afisare_masina(self):
        print (f"Marca: {self.marca}")
        print (f"Model: {self.model}")
        print (f"An fabricatie: {self.an_fabricatie}")
        print (f"Culoare: {self.culoare}")
        print (f"Viteza maxima: {self.viteza_maxima} km/h")
        print (f"Pret: {self.pret} EUR")
        print (f"Viteza curenta: {self.viteza_actuala} km/h")
    
    def accelereaza(self, viteza):
        self.viteza_actuala += viteza
        if self.viteza_actuala > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        print (f"Masina accelereaza pana la {self.viteza_actuala} km/h.")
    
    def franeaza(self, viteza):
        self.viteza_actuala -= viteza
        if self.viteza_actuala < 0:
            self.viteza_actuala = 0
        print (f"Masina a decelerat pana la {self.viteza_actuala} km/h.")
    
    def seteaza_pret(self, pret_nou):
        self.pret = pret_nou
        print(f"Pretul masinii a fost actualizat la {self.pret} EUR.")

masina1 = Masina("Toyota", "Corolla", 2015, "albastru", 180, 8000)
masina1.afisare_masina()
masina1.accelereaza(60)
masina1.franeaza(30)
masina1.franeaza(50)
masina1.seteaza_pret(7500)