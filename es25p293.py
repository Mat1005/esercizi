'''
Crea la classe Triangolo, la classe derivata TriangoloIsoscele e, da quest'ultima, la classe derivata TriangoloEquilatero.
'''
class Triangolo:
    def __init__(self, latoa, latob, latoc, altezza):
        self.latoa = latoa
        self.latob = latob
        self.latoc = latoc
        self.altezza = altezza
    def perimetro(self):
        print("Il perimetro del triangolo con i lati di lunghezza:", self.latoa,",",self.latob,",",self.latoc,";è uguale a",self.latoc + self.latob + self.latoa)
 
    def area(self):
        print("La sua area è ")
        area = self.latoa * self.latoc/2
class TriangoloIsoscele(Triangolo):
    def _init_(self, latoa, latoobliquo, altezza):
        super()._init_(latoa)
        super()._init_(altezza)
        self.latoobliquo = latoobliquo
        
    def perimetro_isoscele(self):
        print("Il perimetro del triangolo isoscele è uguale a",perimetro)
        perimetro = self.latoobliquo * 2 + self.latoa

    def area_isoscele(self):
        print("La sua area è ",area)
        area = self.latoa * self.altezza/2


class TriangoloEquilatero(TriangoloIsoscele):
    def _init_(self, latoa, altezza):
        super()._init_(latoa)
        super()._init_(altezza)

        
    def perimetro_equilatero(self):
        print("Il perimetro del triangolo equilatero è uguale a",perimetro)
        perimetro = self.latoa * 3

    def area_equilatero(self):
        print("La sua area è ",area)
        area = self.latoa * self.altezza/2



lato1 = int(input("Inserire lato"))
lato2 = int(input("Inserire lato"))
lato3 = int(input("Inserire lato"))
h =  int(input("Inserire altezza"))
t1 = Triangolo(lato1, lato2, lato3, h)
t1.perimetro()
t1.area()
base = int(input("Inserire base"))
lato_obliquo = int(input("Inserire lato"))
altezza = int(input("Inserire altezza"))
t2 = TriangoloIsoscele(base, lato_obliquo, altezza)
t2.perimetro_isoscele()
t2.area_isoscele()
lato = int(input("Inserire lato"))
altezza3 = int(input("Inserire altezza"))
t3 = TriangoloEquilatero(lato, altezza3)
t3.perimetro_equilatero()
t3.area_equilatero()