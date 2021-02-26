'''
Deriva dalla classe Quadrato una nuova classe Rettangolo aggiungendo un secondo lato per l'altezza 
e riscrivine i metodi per il calcolo del perimetro e dell'area.
'''
class Quadrato:
    
    def __init__(self, lato):
        self.lato = lato

    def perimetro(self):
        perimetro = self.lato * 4
        print("Il perimetro del quadtrato è uguale a",perimetro)
    
    def area(self):
        area = self.lato * self.lato
        print("L'area è uguale a",area)
        
class Rettangolo(Quadrato):
    def _init_(self, lato, lato2):
        super()._init_(lato)
        self.lato2 = lato2
        
    def ottieni_perimetro(self):
        return (self.lato + self.lato2) * 2

    def ottieni_area(self):
        return self.lato * self.lato2


q = Quadrato(int(input("Quanto vale il lato del quadrato?")))
q.perimetro()
q.area()
b = int(input("Quanto vale la base del rettangolo?"))
h = int(input("Quanto vale l'altezza del rettangolo?"))
r = Rettangolo(b, h)
r.ottieni_perimetro()
r.ottieni_area()
