'''
Elenca proprietà e metodi della classe Prodotto.
Definisci il metodo assegna prezzo alla classe Prodotto 
'''
class Product:
    def __init__(self, name, colour, material, use):
        self.name = name
        self.colour = colour
        self.material = material
        self.use = use

    def assign_price(self, price):
        self.price = price

    def info(self):
        print("L'oggetto",self.name,",di colore",self.colour,",di",self.material,",che serve a",self.use,",")
        print("costa",self.price,"euro.")

p1 =  Product("sedia","marrone","legno","sedersi")
p1.assign_price(10)
p1.info()
p2 =  Product("pentola","grigia","metallo","cuocere")
p2.assign_price(15)
p2.info()