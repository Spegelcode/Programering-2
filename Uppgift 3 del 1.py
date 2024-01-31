def pris_inkl_moms(pris_exkl_moms, momssats):
    moms = pris_exkl_moms * (momssats / 100)
    pris_inkl_moms = pris_exkl_moms + moms
    return pris_inkl_moms
#Här tar vi och räkanr ut mons inklusvie mons men en simpel ecvations kod 

def skapa_textfil(resultat):
    try:
        with open("output.txt", "w") as file:
            file.write(f"Pris inklusive moms: {resultat:.2f} kr")
        print("Textfilen har skapats och resultatet har skrivits till filen.")
    except IOError:
        print("Det uppstod ett fel vid skapandet av textfilen.")
#vi skapar en text fil som heter output.text sen skriver vi in det till resultat med whit så öppnar och stänger vi filen atomatiskt 
#vi öppnar filen med W så vi kan skriva över write gör så att vi kan forma en string 
#La in en funktion flr att skriva ut vi ska bli informerade om ifall filen sparats rätt
def las_från_textfil():
    try:
        with open("output.txt", "r") as file:
            innehall = file.read()
            print("Innehållet i textfilen:")
            print(innehall)
    except FileNotFoundError:
        print("Textfilen hittades inte.")
    except IOError:
        print("Det uppstod ett fel vid läsning av textfilen.")
#vi läser av output.txt med las_från_textfil med whit för aotu öppna
#vi öppnar den i r sen läser vi den med read och lagrar i inehall
#sen skriver vi ut resultat och error medelande ifall det blev nått fel.
# Exempelanvändning:
exempel_pris_exkl_moms = 10012351  # Ange det pris du vill testa
exempel_momssats = 25  # Ange  momssatsen i procent

pris_inkl_moms_resultat = pris_inkl_moms(exempel_pris_exkl_moms, exempel_momssats)

skapa_textfil(pris_inkl_moms_resultat)
las_från_textfil()