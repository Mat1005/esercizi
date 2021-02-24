'''
Crea una classe Quadrato con l'attributo lato e i metodi per calcolare il perimetro e l'area.
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


q = Quadrato(int(input("Quanto vale il lato del quadrato?")))
q.perimetro()
q.area()