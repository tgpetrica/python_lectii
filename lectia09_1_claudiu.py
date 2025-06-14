# Exercițiul 1: Gestionarea unei liste de cumpărături
# Scrie un program care permite utilizatorului să gestioneze o listă de cumpărături.
# Cerințe:
#  Afișează un meniu cu următoarele opțiuni:
# 1. Adaugă un produs
# 2. Afișează lista de cumpărături
# 3. Șterge un produs
# 4. Iese din program
#  Permite utilizatorului să adauge, să șteargă și să vizualizeze lista de cumpărături.
#  Programul trebuie să continue să ruleze până când utilizatorul alege opțiunea 4.


lista_cumparaturi = []

while True:
    print("== Meniu lista de cumparaturi ==")
    print("1. Adauga un produs")
    print("2. Afiseaza lista de cumparaturi")
    print("3. Sterge un produs")
    print("4. Iese din program")

    optiune = input ("Alege o optiune (1-4): ")

    if optiune == "1":
        produs = input("Introdu numele unui produs: ")
        lista_cumparaturi.append(produs)
        print (f"Produsul '{produs}' a fost adaugat.")
    
    elif optiune == "2":
        if not lista_cumparaturi:
            print("Lista de cumparaturi este goala")
        else:
            print ("Produsele din lista de cumparaturi: ")
            for i in range(len(lista_cumparaturi)):
                print(f"{i + 1}. {lista_cumparaturi[i]}")

    elif optiune == "3":
        produs = input("Introdu produsul pe care vrei sa il stergi: ")
        if produs in lista_cumparaturi:
            lista_cumparaturi.remove(produs)
        else:
            print(f"Produsul '{produs}' nu exista in lista de cumparaturi.")
    
    elif optiune == "4":
        print ("La revedere!")
        break
    
    else:
        print("Optiune invalida. Alege optiunea (1-4). ")


