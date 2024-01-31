import math

def area_triangel(base, height):
    area = 0.5 * base * height
    return area

def area_parallellogram(base, height):
    area = base * height
    return area

def area_parallelltrapets(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

def area_cirkel(radius):
    area = math.pi * radius ** 2
    return area

def area_cirkelsektor(radius, angle):
    area = (angle / 360) * math.pi * radius ** 2
    return area
#här är alla olika area uträkningarna listade 
bas = 5
höjd = 8
triangel_område = area_triangel(bas, höjd)
print("Triangelns område:", triangel_område)

bas = 1
höjd = 4
parallellogram_område = area_parallellogram(bas, höjd)
print("Parallellogrammets område:", parallellogram_område)

bas1 = 2
bas2 = 5
höjd = 5
parallelltrapets_område = area_parallelltrapets(bas1, bas2, höjd)
print("Parallelltrapets område:", parallelltrapets_område)

radie = 3
cirkel_område = area_cirkel(radie)
print("Cirkelns område:", cirkel_område)

radie = 5
vinkel = 60
cirkelsektor_område = area_cirkelsektor(radie, vinkel)
print("Cirkelsektorns område:", cirkelsektor_område)
#här tillkallar vi exempel på mått på olika objekt där kan vi då ända och få fram olika area 