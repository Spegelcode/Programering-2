import math
#importerar math
def beräkna_area_kvadrat(sida):
    area = sida * sida
    return area

def beräkna_area_rektangel(bredd, höjd):
    area = bredd * höjd
    return area

def beräkna_area_triangel(bas, höjd):
    area = 0.5 * bas * höjd
    return area

def beräkna_area_cirkel(radie):
    area = math.pi * radie**2
    return area

def beräkna_area_hexagon(sida):
    area = (3 * math.sqrt(3) * sida**2) / 2
    return area
#olika uträkningar för arean för olika former 
# Exempelanvändning:
sida_kvadrat = 5
bredd_rektangel = 4
höjd_rektangel = 6
bas_triangel = 8
höjd_triangel = 3
radie_cirkel = 2.5
sida_hexagon = 7
#här definierar vi de måtten vi vill ha
area_kvadrat = beräkna_area_kvadrat(sida_kvadrat)
area_rektangel = beräkna_area_rektangel(bredd_rektangel, höjd_rektangel)
area_triangel = beräkna_area_triangel(bas_triangel, höjd_triangel)
area_cirkel = beräkna_area_cirkel(radie_cirkel)
area_hexagon = beräkna_area_hexagon(sida_hexagon)
#Här tillkallar vi den tidigar funktionerna för att räkna ut arean för de olia formerna
print(f"Area för kvadraten: {area_kvadrat:.2f}")
print(f"Area för rektangeln: {area_rektangel:.2f}")
print(f"Area för triangeln: {area_triangel:.2f}")
print(f"Area för cirkeln: {area_cirkel:.2f}")
print(f"Area för hexagonen: {area_hexagon:.2f}")
#sen skriver bi ut allt med 2 decimaler 