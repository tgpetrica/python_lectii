parola: str = input("introdu parola: ")

if (len(parola) > 7 and "!" in parola) or ("@" in parola and not "123" in parola):
    print("parola este valida.")
else:
    print("parola este invalida.")