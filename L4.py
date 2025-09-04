# Functii

# defineste un bloc de instructiuni care se pot repeta de mai multe ori.
# Acest bloc are un nume si se apeleaza de ori de cate ori avem nevoie de
# acele instructiuni.

# Tipuri de functii:

#   1. Functii fara parametru

def salutare():
    print("Salutare!")
    print("Numele meu este Teodor.")

salutare()

#   2. Functii cu parametru

def saluta_persoana(nume: str):
    print("Salut, " + nume + "!")
    # + realizeaza operatia de concatenare striguri 
    # (lipeste mai multe siruri de caractere)

saluta_persoana("Andrei")

def saluta_prieten(nume: str):
    print(f"Salut, {nume}!")

saluta_prieten("Mihai")

def saluta_coleg(nume: str):
    print("Salut, %s!" %nume)

saluta_coleg("Anastasia")

# Formatarea veche din Python folosea specificatori:
#   %s      - string (siruri de caractere)
#   %d      - numar intreg (decimal)
#   %f      - numar real (numar cu virgula)
#   %.2f    - numar real cu exact doua zecimale
#   %c      - caracter

#   3. Functii care returneaza valori

def inmultire(x: int, y: int) -> int:
    return x * y

print("Inmultire: ", inmultire(2, 5))

# Cum functioneaza?
# - Fisierul python (extensia .py) este citit/parcurs secvential 
#     (de sus in jos, linie cu linie).
# - Cand interpretorul intalneste definitia unei functii (ex. salutare), 
#     se creeaza in memorie un obiect cu acel nume.
# - Functia poate fi apelata mai tarziu in program, iar la apel, 
#     instructiunile din interiorul functiei sunt executate.
# - Dupa terminarea executiei functiei, se revine la codul principal

# Reguli pentru a denumi functii:
# - numele functiilor pot contine doar litere, cifre si caracterul underscore _
# - numele unei functii trebuie sa inceapa cu o litera sau cu caracterul underscore
# - numele unei functii NU poate incepe cu o cifra
# - NU sunt permise spatii in numele functiilor
# - NU sunt permise caractere speciale (@, !, #, $, %, <, >, ă, î, â, ș, ț)
# - recomandare: numele functiilor scrise cu minuscule (litere mici)
# - recomandare: intre cuvinte se pune caracterul underscore _

# Exemple:
# nume_functie()
# aceasta_este_o_functie()
# schimba_ora()
# transforma_baza_2()

