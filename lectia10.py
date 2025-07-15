import tkinter as tk

fereastra: tk.Tk = tk.Tk() # fereastra = tk.Tk()
fereastra.title("O fereastra Tkinter")
fereastra.geometry("400x300")

eticheta = tk.Label(fereastra, text = "Aceasta este o eticheta.")
eticheta.pack()

def schimba_text():
    eticheta.config(text = "Ai apasat pe buton!")
    buton.config(text = "Buton apasat.", state = "disabled")
    fereastra.after(1000 * 5, reactivare) # 5 secunde = 5000 milisecunde

def reactivare():
    buton.config(text = "Buton activat", state = "normal")

buton = tk.Button(fereastra, text = "Apasa-ma!", command = schimba_text)
buton.pack()

inchidere = tk.Button(fereastra, 
                      text = "inchide", 
                      background = "red",
                      fg = "white", # foreground
                      command = fereastra.destroy)
inchidere.pack()

spatiu = tk.Label(fereastra, text = "")
spatiu.pack(pady = 30)

caseta = tk.Entry(fereastra, width = 20)
caseta.pack()

def afiseaza():
    text = caseta.get()
    rezultat.config(text = f"Ai scris: {text}")

buton_afisare = tk.Button(fereastra, text = "Afiseaza text!", command = afiseaza)
buton_afisare.pack()

rezultat = tk.Label(fereastra, text = "--")
rezultat.pack(pady = 10)

fereastra.mainloop()

