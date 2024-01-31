def skriv_till_fil(filnamn, text): #Deklarerar en dunktion med namnet skriv till fil och tilldelar filnamn och text
    try:
        with open(filnamn, 'a') as fil: #Öppnar filen i a och gör så att den läggs i slutet och inte skrivs över
            fil.write(text + '\n')#skriver en text till filen följt av \n för att lägga till en ny rad
    except IOError as e: # ifall det blir en oväntad error tex texten inte öppnas el skrivs till 
        print("Kunde inte skriva till filen:", str(e)) #felmedelande

def läs_från_fil(filnamn): #namnet på filen vi ska läsa 
    try:
        with open(filnamn, 'r') as fil: #öppnar fien filnamn i r och tilldelar den "fil" så vi kan läsa från filen
            innehåll = fil.read() #läser av inehållet i filen å gör den till innehåll
            print("Innehåll i filen:") 
            print(innehåll) # skriver ut filens inehåll
    except IOError as e: # ifall filen inte går att läsa från pga iofel 
        print("Kunde inte läsa från filen:", str(e))#skriver ut felmedelandet å varför

def main():
    filnamn = "textfil.txt" #tilldelar namnet på filen vi skriver och läser till

    while True: #loop som bryts av break
        rad = input("Skriv en rad text (eller lämna tom för att avsluta): ") #informerar om hur vi bryter loopen
        if rad == "":
            break # här bryter vi loopen

        skriv_till_fil(filnamn, rad)#för att lägga till på en rad 

    läs_från_fil(filnamn) #för att läsa från filnamn och skriva ut 

if __name__ == "__main__":
    main()#så vi kör main funktionen direkt och inte som modul