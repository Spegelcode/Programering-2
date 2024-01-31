import csv
import matplotlib.pyplot as plt
#här importerar vi csv och matpolt.lib för att hantera CVS filer
def ar_primtal(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
#Här kollar vi ifall siffran som matats in är prime eller inte och ger ut ett tru false 
def räkna_primtal():
    primtal_lista = []
    for num in range(2, 201):
        if ar_primtal(num):
            primtal_lista.append(num)
    return primtal_lista
#här genererar vi en lista med primenummer från 2-200 med hjälp av
def spara_till_csv(primtal_lista):
    try:
        with open("primtal.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Primtal"])
            writer.writerows([[primtal] for primtal in primtal_lista])
        print("Data har sparats i primtal.csv.")
    except IOError:
        print("Det uppstod ett fel vid sparandet av data till CSV-filen.")
#spara_till_csv sparar primtal_lista till primtal.cvs
#csv-writer skriver prime tall till cvs filen
#Första raden i filen skrivs som rubrik "Primtal" varje Primtal får en egen rad
#sen skriver vi ut ett medelande ifall filen sparats eller inte
def läs_från_csv_och_skapa_diagram():
    primtal_lista = []
    try:
        with open("primtal.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Hoppa över rubrikraden
            for row in reader:
                primtal = int(row[0])
                primtal_lista.append(primtal)
    except FileNotFoundError:
        print("CSV-filen hittades inte.")
        return
    except IOError:
        print("Det uppstod ett fel vid läsning av CSV-filen.")
        return

    x = range(2, len(primtal_lista) + 2)
    plt.plot(x, primtal_lista, marker="o")
    plt.xlabel("Nummer")
    plt.ylabel("Primtal")
    plt.title("Primtal från 2 till 200")
    plt.show()
#här läser vi prime nummret från csv filen primtal.cvs och skapar sen en grav med Matplotib
#csv.reader är för att läsa av Cvs filer vi skippar första raden som är rubriken med next(read)
#sen omvandlas allt till ett heltal ock läggs in i primtal_lista, variabel x skapar som en sekvens från 2 till längden av promtal_lista + 2 
#grafen skapas av plt.plot och x är x-axeln och primtal_lista är y axeln
#grafen märks och får en titel  sen visar vi den med plt.show()

# Exempelanvändning:
primtal_lista = räkna_primtal()
spara_till_csv(primtal_lista)
läs_från_csv_och_skapa_diagram()