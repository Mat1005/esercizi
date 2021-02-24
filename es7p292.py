'''
Elenca proprietà e metodi della classe Motociclo.
'''
class Motociclo:
    
    def __init__(self, modello, colore, velocita_massima, accelerazione_massima, prezzo):
        self.modello = modello
        self.colore = colore
        self.velocita_massima = velocita_massima
        self.accelerazione_massima = accelerazione_massima
        self.prezzo = prezzo
    
    def info(self):
        print("Il motociclo del modello",self.modello,"che costa",self.prezzo,"euro, è di colore",self.colore,".")
        print("Può raggiungere la velocita massima di",self.velocita_massima,"km/h e può raggiungere l'accelerazione massima di",self.accelerazione_massima,"m/s^2.")

modello = input("Quale è il modello del motociclo?")
colore = input("Quale è il suo colore?")
velocita_massima = int(input("Quale è la velocità massima che può ragiungere?(Esprimere la misura in km/h)"))
accelerazione_massima = int(input("Quale è l'accelerazione massima che può ragiungere?(Esprimere la misura in m/s^2)"))
prezzo = int(input("Quanto costa?"))
m1 = Motociclo(modello, colore, velocita_massima, accelerazione_massima, prezzo)
m1.info()