# Fisiere
# - o structura definita in care pot sa stochez date 
# - poate contine text sau poate contine date binare
# - unul sau mai multe fisiere pot fi adunate/salvate intr-un folder (director)

# nume_fisier.extensie
# extensie arata in general ce fel de date si cum arata structura fisierului
# Exemple de extensii fisiere text: .txt, .csv, .json, .geojson, .py
# Exemple de extensii fisiere binare: .exe, .dng, .png, .jpeg, .mp3, .pdf

# Deschiderea unui fisier

with open("text.txt", "r") as fisier:
    for linie in fisier:
        print(linie)

# Flaguri:
# "r" - read: deschide fisier doar pentru citire. daca nu exista fisierul apare eroare.
# "w" - write: deschide fisierul pentru scriere. Daca fisierul exista, continutul se sterge.
# "x" - create: creeaza un fisier nou. Daca exista deja, apare eroare.
# "a" - append: deschide fisierul pentru scriere, dar nu sterge continutul, ci adauga la final.

# Moduri de tip;
# "t" - text mode: lucreaza cu fisierul ca text
# "b" - binary mode: lucreaza cu fisierul ca biti (folosit in imagini, PDF, ..)

# "+" - update: deschide pentru citire si scriere

# Scrierea intr-un fisier
with open("fisier.txt", "w") as fisier:
    fisier.write("Aceasta este prima mea linie scrisa intr-un fisier cu Python!\n")

# Scrierea prin actualizare a unui fisier
with open("fisier.txt", "a") as fisier:
    fisier.write("Am actualizat fisierul!")

with open("jurnal.txt", "w") as file:
    file.write("Astazi m-am trezit de dimineata si am fost sa imi repar bicicleta.\n")
    file.write("La pranz, am fost la cumparaturi.")
    file.write("Dupa amiaza am iesit cu cativa priteni in parc.")
    file.write("Am plecat din parc la ora 18 pentru a ajunge la timp la cursul de Python!")
    file.write("Acum sunt la cursul de Python si imi place!")

cuvant: str = input ("Introdu cuvantul de cautat: ")
with open("jurnal.txt", "r") as fisier:
    continut: str = fisier.read()
    if cuvant in continut:
        print("Cuvantul exista.")
    else:
        print("Cuvantul nu exista.")

