import random

numar: int = random.randint(1, 20) 

if numar % 2 == 0: 
    print(f"Numarul generat este {numar} si este par.") 
else: 
    print(f"Numarul generat este {numar} si este impar.")