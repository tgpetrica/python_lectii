NUME_FISIER = "highscore.txt"

def citeste_highscore():
    try:
        f = open(NUME_FISIER, "r", encoding = "utf-8")
        linie = f.readline().strip()
        f.close()

        if linie.isdigit():
            return int(linie)
        
        return 0
    except:
        return 0
    
def scrie_highscore(val):
    try:
        f = open(NUME_FISIER, "w", encoding = "utf-8")
        f.write(str(val))
        f.close()
    except:
        pass