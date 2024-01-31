import csv
import random
import string

# här skapar vi klass för person
class Person:
    def __init__(self, namn, personnummer, adress):
        self.namn = namn
        self.personnummer = personnummer
        self.adress = adress

# här skapar vi en klass för kund som ärver från Person

class Kund(Person):
    def __init__(self, namn, personnummer, adress):
        super().__init__(namn, personnummer, adress)
        self.konton = set()

    def spara_till_fil(self, filnamn):
        with open(filnamn, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.namn, self.personnummer, self.adress])
            for konto in self.konton:
                writer.writerow([konto])

# här skapar vi klass för bankkonto 
class Bankkonto:
    def __init__(self, typ_av_konto):
        self.kontonummer = self.generera_kontonummer()
        self.saldo = 0
        self.typ_av_konto = typ_av_konto

    def generera_kontonummer(self):
        kontonummer = ''.join(random.choices(string.digits, k=7))
        return f'9855-{kontonummer}'

    def visa_saldo(self):
        print(f"Saldo: {self.saldo}")

    def insattning(self, belopp):
        self.saldo += belopp

    def uttag(self, belopp):
        if self.saldo >= belopp:
            self.saldo -= belopp
        else:
            print("Otillräckligt saldo.")

def skapa_konto_kund(kund, typ_av_konto):
    konto = Bankkonto(typ_av_konto)
    kund.konton.add(konto.kontonummer)
    return konto

# Exempel på hur programmet kan användas:d
if __name__ == "__main__":
    # Skapa en kund
    kund1 = Kund("Anna Andersson", "19871212-1234", "vägen 1")

    # Skapa konto för kunden
    konto1 = skapa_konto_kund(kund1, "sparkonto")
    konto2 = skapa_konto_kund(kund1, "lönekonto")

    # Gör insättning och uttag på konto1
    konto1.insattning(1000)
    konto1.visa_saldo()
    konto1.uttag(500)
    konto1.visa_saldo()

    # Spara kundoch konton till CSV-fil
    kund1.spara_till_fil("kunder.csv")
    
    
    
    
  