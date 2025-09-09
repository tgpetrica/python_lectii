import random
import unicodedata

def sterge_diacritice(text: str) -> str:
    if not text:
        return text
    clean = unicodedata.normalize("NFD", text)
    # NFD = normalization form decomposed: baza + diacritica
    return "".join(c for c in clean if unicodedata.category(c) != "Mn")

# https://www.unicode.org/reports/tr44/tr44-30.html#General_Category_Values

def curata(text: str) -> str:
    if not text:
        return ""
    text = text.strip()
    text = sterge_diacritice(text)
    text = text.lower()
    text = text.replace(" ", "_")
    return text

class UsernameGenerator:
    SUFIXE = ["123", "55", "_pro", "_dev", "demo", "_boss", "king", "queen" ]

    def __init__(self):
        print("Welcome to the Username generator!")
    
    def colecteaza_input(self):
        prenume_raw = input("Introdu-ti prenumele: ")   # first name
        nume_raw    = input("Introdu-ti numele: ")      # last name / surname
        culoare_raw = input("Care este culoarea ta preferata? ")
        hobby_raw   = input("Introdu hobby-ul tau: ")
        zi_raw      = input("Care este ziua ta preferata? (poti lasa gol daca nu ai)")
    
        prenume = curata(prenume_raw)
        nume    = curata(nume_raw)
        culoare = curata(culoare_raw)
        hobby   = curata(hobby_raw)
        zi      = curata(zi_raw)

        return prenume, nume, culoare, hobby, zi
    
    def alege_sufix(self) -> str:
        return random.choice(self.SUFIXE)
    
    def parti_candidat(self, prenume: str, nume: str, culoare: str, hobby: str, zi: str):
        parti = [
                    prenume,
                    nume, 
                    culoare,
                    hobby,
                    zi
            ]
        
        if prenume and nume:
            parti += [
                prenume[:3] + nume[:3], # primele 3 caractere din nume, prenume
                prenume[0] + nume,      # initiala prenumelui si numele complet
                nume[0] + prenume,      # initiala numelui si prenumele complet
                prenume + nume[:2],     # prenumele si primele 2 caractere din nume
                (prenume[::-1] + nume)  # prenumele scris invers si numele complet
            ]
        
        if culoare and hobby:
            parti += [
                culoare + hobby[:2],    # culoarea si primele 2 caractere din hobby
                hobby + culoare[:2]     # hobby-ul si primele 2 caractere din culoare
            ]
        
        if zi and prenume:
            parti += [
                zi + prenume[:2],       # ziua si primele 2 caractere din prenume
                prenume + zi[:2]        # prenumele si primele 2 caractere din zi        
            ]
        
        parti_unice = []
        for p in parti:
            if p and p not in parti_unice:
                parti_unice.append(p)
        
        return parti_unice
    
    def genereaza_username(self, x: int = 1):
        prenume, nume, culoare, hobby, zi = self.colecteaza_input()
        parti = self.parti_candidat(prenume, nume, culoare, hobby, zi)

        if not parti:
            parti = ["user", "player", "guest"]
        
        print("\nUsername generate:")
        for i in range(1, x + 1):
            baza = random.choice(parti)
            sufix = self.alege_sufix()
            username = baza + sufix
            print(f"    {i}. {username}")

if __name__ == "__main__":
    gen = UsernameGenerator()
    try:
        n = input("Cate username vrei sa generez?").strip()
        n = int(n) if n else 1
    except ValueError:
        n = 1
    
    gen.genereaza_username(n)
