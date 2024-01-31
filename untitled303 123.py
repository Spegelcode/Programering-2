import csv
import random
import pandas as pd

# Klass Person
class Person:
    def __init__(self, namn, personnummer, adress):
        self.namn = namn
        self.personnummer = personnummer
        self.adress = adress

# Klass Kund (Ärv från Person och hantera CSV-fil för kunddata)
class Kund(Person):
    def __init__(self, namn, personnummer, adress):
        super().__init__(namn, personnummer, adress)

    def spara_till_csv(self):
        with open('kunddata.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.namn, self.personnummer, self.adress])

    @staticmethod
    def ladda_från_csv():
        try:
            df = pd.read_csv('kunddata.csv')
            kunder = []
            for _, row in df.iterrows():
                kund = Kund(row['namn'], row['personnummer'], row['adress'])
                kunder.append(kund)
            return kunder
        except FileNotFoundError:
            return []

# Klass Bankkonto
class Bankkonto:
    kontonummer_set = set()

    def __init__(self, kund, kontotyp):
        self.kontonummer = self.generera_kontonummer()
        self.kund = kund
        self.kontotyp = kontotyp
        self.saldo = 0

    def generera_kontonummer(self):
        kontonummer = f"{random.randint(1000, 9999)}-{random.randint(1000000, 9999999)}"
        while kontonummer in Bankkonto.kontonummer_set:
            kontonummer = f"{random.randint(1000, 9999)}-{random.randint(1000000, 9999999)}"
        Bankkonto.kontonummer_set.add(kontonummer)
        return kontonummer

    def blockera_kontonummer(self):
        Bankkonto.kontonummer_set.remove(self.kontonummer)

    def visa_saldo(self):
        return self.saldo

    def insättning(self, belopp):
        self.saldo += belopp

    def uttag(self, belopp):
        if belopp <= self.saldo:
            self.saldo -= belopp
        else:
            print("Otillräckligt saldo!")

# Testkod för att använda bankprogrammet
if __name__ == "__main__":
    # Skapa kunder och spara i CSV-fil
    kund1 = Kund("Anna", "19800101-1234", "Gatan 1")
    kund2 = Kund("Bengt", "19810202-5678", "Gatan 2")

    kund1.spara_till_csv()
    kund2.spara_till_csv()

    # Ladda kunder från CSV-fil
    kunder = Kund.ladda_från_csv()

    # Skapa bankkonton och blockera ett kontonummer
    bankkonto1 = Bankkonto(kunder[0], "Sparkonto")
    bankkonto2 = Bankkonto(kunder[1], "Lönekonto")

    bankkonto1.blockera_kontonummer()

    # Utföra transaktioner
    bankkonto1.insättning(1000)
    bankkonto1.uttag(500)

    # Visa saldo
    print(f"Saldo på {bankkonto1.kontonummer}: {bankkonto1.visa_saldo()}")