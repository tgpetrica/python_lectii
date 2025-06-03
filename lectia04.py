# Functii

# descrie o serie de instructiuni care se pot repeta intr-un singur loc,
# urmand ca blocul de instructiuni sa fie apelat ca un alias in locul
# in care am nevoie de acel bloc de instructiuni

# Functiile pot fi de mai multe tipuri:

#   1. Functii fara parametru

def salut():
    print("Salutare!")
    print("Numele meu este Teodor.")

salut() # apelul functiei salut()

#   2. Functii cu parametru

def saluta_persoana(nume: str):
    # print("Salut, " + nume + "!") # + realizeaza operatia de concatenare stringuri (lipeste)
    print(f"Salut, {nume}!")
    # print("Salut, %s!" %nume)

saluta_persoana("Andrei")
saluta_persoana("Miruna")

#   3. Functii care returneaza valori
# Pentru a returna un rezultat folosim cuvantul rezervat return

def adunare(a: int, b: int) -> int:
    return a + b

print ("Suma este: ", adunare(23,30))


# Cum functioneaza?
# - Fisierul .py este citit/parcurs de sus in jos
# - se identifica definitia unei functii (ex. salut()) si se creaza
#   un obiect cu numele salut in memoria programului
# - obiectul nou creat poate fi apelat ulterior; cand se gaseste un apel
#   al obiectului, instructiunile aferente obiectului sunt executate.
# - in final, se intoarce la codul principal din fisierul .py

# Numele functiilor
# - regula: doar din litere, cifre si eventual _
# - numele functiei poate incepe cu caracter litera sau _ (NU poate incepe cu o cifra)
# - conventie care spune ca numele functiilor contin doar minuscule (litere mici) (v. PEP8)
# - numele functiilor NU poate contine caractere spatiu
# - numele functiilor NU poate contine caractere speciale (@, !, #, $, %, <, >, ă, î, â, ț, ș, ö, ä, ł, ą, ż, ń, etc.)

# Exemple de bune practici:
# nume_functie()
# functie()
# aceasta_este_alta_functie()
# schimba_baza_2