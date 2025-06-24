# Problema 1
# Se citeste de la tastatura un numar natural n (n >= 1) si apoi n obiecte:
# - se afiseaza obiectele in ordinea in care au fost introduse
# - se afiseaza obiectele in ordinea inversa in care au fost introduse
# - se citeste un obiect si se sterge acel obiect din lista (daca exista)

obiecte: list [str] = []

n: int = int (input("Introdu numarul de elemente: "))

# citirea elementelor din lista
for numar in range (n):
    element: str = input(f"Obiectul {numar + 1}: ")
    obiecte.append(element)

# afisare de la stanga la dreapta
for element in range(len(obiecte)):
    print(obiecte[element])

# afisare de la dreapta la stanga
for element in range(len(obiecte) - 1, -1, -1):
    print(obiecte[element])

sterge : str = input ("Introdu un element pentru a fi sters: ")

if sterge in obiecte:
    while sterge in obiecte:
        obiecte.remove(sterge)
    print(f"Elementul {sterge} a fost sters din lista.")
else:
    print("Elementul nu a fost gasit in lista.")

print ("\n La final lista arata astfel:")
for element in range(len(obiecte)):
    print(obiecte[element])