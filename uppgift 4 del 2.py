import math
#imporerar math
class Form:
    def beräkna_area(self):
        pass
#form andvänds för att definerar en metod beräkna_area() som är tom å skapar subklasser 
class Rektangel(Form):
    def __init__(self, bredd, höjd):
        self.bredd = bredd
        self.höjd = höjd

    def beräkna_area(self):
        return self.bredd * self.höjd

class Kvadrat(Form):
    def __init__(self, sida):
        self.sida = sida

    def beräkna_area(self):
        return self.sida * self.sida

class Triangel(Form):
    def __init__(self, bas, höjd):
        self.bas = bas
        self.höjd = höjd

    def beräkna_area(self):
        return 0.5 * self.bas * self.höjd

class Cirkel(Form):
    def __init__(self, radie):
        self.radie = radie

    def beräkna_area(self):
        return math.pi * self.radie**2

class Hexagon(Form):
    def __init__(self, sida):
        self.sida = sida

    def beräkna_area(self):
        return (3 * math.sqrt(3) * self.sida**2) / 2
#här kallar vi på form förr att räkna ut olika area 

# Exempelanvändning:
rektangel = Rektangel(4, 6)
kvadrat = Kvadrat(5)
triangel = Triangel(8, 3)
cirkel = Cirkel(2.5)
hexagon = Hexagon(7)
#vi skapar rader som tilldelas klass och variabler
area_rektangel = rektangel.beräkna_area()
area_kvadrat = kvadrat.beräkna_area()
area_triangel = triangel.beräkna_area()
area_cirkel = cirkel.beräkna_area()
area_hexagon = hexagon.beräkna_area()
#vi anroppar beräkna_are() för att beräkna area 
print(f"Area för rektangeln: {area_rektangel:.2f}")
print(f"Area för kvadraten: {area_kvadrat:.2f}")
print(f"Area för triangeln: {area_triangel:.2f}")
print(f"Area för cirkeln: {area_cirkel:.2f}")
print(f"Area för hexagonen: {area_hexagon:.2f}")
#här skriver vi ut alla resultat 