# Problema 2
# Se citeste de la tastatura un numar natural n (n >= 1) si apoi n numere intregi:
# - sa se afiseze cel mai mare numar din lista
# - sa se afiseze cel mai mic numar din lista
# - sa se afiseze suma numerelor din lista
# - sa se afiseze media aritmetica a numerelor din lista (suma elementelor / numarul elementelor (tip float))

numere: list [int] = []

n: int = int (input ("Introdu numarul de elemente: "))

# citirea elementelor din lista
for i in range(n):
    nr: int = int (input(f"Numarul {i + 1}: "))
    numere.append(nr)

maxim : int = numere[0]
minim : int = numere[0]
suma : int = 0


for i in numere:
    if i > maxim:
        maxim = i
    
    if i < minim:
        minim = i

    suma += i       # suma = suma + i

medie : float = suma / len(numere)

print(f"Maxim: {maxim}")
print(f"Minim: {minim}")
print(f"Suma: {suma}")
print(f"Media: {medie}")

    