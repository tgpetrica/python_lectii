# scrie un program care cere utilizatorului sa aleaga intre trei tipuri de meniuri:
# 1. vegetarian
# 2. vegan
# 3. carnivor

# Daca utilizatorul alege vegetarian, sa se afiseze "Ai ales un meniu fara carne."

# Daca utilizatorul alege vegan, sa se afiseze "Ai ales un meniu fara produse de origine animala."

# Daca utilizatorul alege carnivor, sa se afiseze "Ai ales un meniu pe baza de carne."

# Daca utilizatorul introduce altceva, sa se afiseze "Meniu invalid."

print ("Alege un meniu: \n1 - vegetarian\n2 - vegan\n3 - carnivor")

alegere :int = int(input("Introdu numarul optiunii: "))

if alegere == 1:
    print("Ai ales un meniu fara carne.")
elif alegere == 2:
    print("Ai ales un meniu fara produse de origine animala.")
elif alegere == 3:
    print("Ai ales un meniu pe baza de carne.")
else:
    print("Meniu invalid.")
