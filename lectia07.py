# OBIECTE
# Obiectele au ATRIBUTE (caracteristici, proprietati)
# Obiectele au METODE (comportamente)

class Film:
    def __init__(self, titlu: str, gen: str, durata: int):
        self.titlu = titlu
        self.gen = gen
        self.durata = durata

    def descriere(self) -> str:
        return f"{self.titlu} - {self.gen}, {self.durata} minute"

filme = []  # lista de filme
n : int = int (input("Cate filme vrei sa adaugi? "))

for i in range(n):
    titlu = input ("Titlul filmului: ")
    gen = input ("Genul filmului: ")
    durata = int (input ("Durata filmului (in minute): "))
    obiect = Film(titlu, gen, durata)
    filme.append(obiect)

print("\nLista filmelor introduse:")
for film in filme:
    print(film.descriere())
