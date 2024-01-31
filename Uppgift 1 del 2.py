def räkna_bokstäver():
    text = input("Ange en text: ")
    antal_små_bokstäver = 0
    antal_stora_bokstäver = 0
#överstående är för att få in mening från andvändaren och dela in i små och stora bokstäver 
    for tecken in text:
        if tecken.islower():
            antal_små_bokstäver += 1
        elif tecken.isupper():
            antal_stora_bokstäver += 1
#här kollar vi meningen och kollar hur många stor och små sen lägger in dem i rätt kategori
    return (antal_små_bokstäver, antal_stora_bokstäver)
resultat = räkna_bokstäver() 
print("Antal små bokstäver:", resultat[0])
print("Antal stora bokstäver:", resultat[1])
#skriver ut resultat 