import random

def arunca_zarul() -> int:
    return random.randint(1, 6)

# https://docs.python.org/3/library/random.html#random.randint

rezultat: int = arunca_zarul()

print("Ai aruncat zarul si ai obtinut: ", rezultat)

def verifica_paritatea(numar: int):
    if numar % 2 == 0:
        print("par")
    else:
        print("impar")

verifica_paritatea(3)
verifica_paritatea(8)