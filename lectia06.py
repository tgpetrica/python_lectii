# Liste

# - ordinea in care au fost introduse in lista valorile
# - adaug noi elemente, sterg elemente, modific elemente
# - sunt permise valori duplicate
# - accesul la fiecare element din cadrul listei se face cu operatorul de indexare []

fructe: list[str] = ["mere", "pere", "caise", "capsuni"]
print (fructe) # afiseaza continutul listei

print (fructe[1]) # al doilea element din lista

# indicele maxim (indexul) este dat de (dimensiune - 1)

print (fructe[0]) # primul element din lista

print (fructe[-1]) # ultimul element din lista

print (fructe[-2]) # penultimul element din lista

# Obs. Indexarea in cadrul listei incepe de la 0.
# Obs. Indexarea negativa reprezinta al x-lea element din coada (de la dreapta la stanga)

print (fructe)

# adaugarea se face folosind un apel al functiei append()
fructe.append("struguri")

print(fructe)
# Obs. append() adauga un element la finalul listei

# modificarea unui element se face prin referire la indexare

fructe[2] = "piersici"

print(fructe)

# stergerea unui element se face folosind un apel al functiei remove()
# Obs. Daca folosim remove() trebuie sa specificam ce element sa stergem.

fructe.remove("mere")
print(fructe)

# stergerea ultimului element din lista se face folosind un apel al functiei pop()
fructe.pop()
print(fructe)

# Obs. Nu este necesara specificarea ultimului element.
print()

# Iterarea unei liste

culori: list[str] = ["rosu", "verde", "albastru", "galben", "mov", "roz", "portocaliu",
                     "negru", "turcoaz", "alb", "magenta", "gri"]

# for obiect in grup_obiecte:

for culoare in culori:
    print(culoare)

print()

numere: list[int] = [1, 2, 3, 4, 5]
print(numere)

# afisarea inversa
# -> cu functie: apel al functiei reverse()
numere.reverse()
print(numere)
numere.reverse()
print(numere)

# -> algoritmic
numere_inversate:list[int] = [] # lista goala

for element in range(len(numere) - 1, -1, -1):
    numere_inversate.append(numere[element])

print(numere_inversate)

print()

obiecte: list[str] = [] # lista goala

n = int (input("Introdu numarul de obiecte: "))

for i in range (n):
    obiect = input(f"{i + 1}: ")
    obiecte.append(obiect)

print("Lista de obiecte: ")
print(obiecte)

