def är_palindrom():
    mening = input("Ange ett ord eller mening: ")
    ren_mening = ''.join(mening.lower().split())
    omvänd_mening = omvänd_ordning(ren_mening)
    
    return ren_mening == omvänd_mening
def omvänd_ordning(text):
    return text[::-1]

if är_palindrom():
    print("Dert är ett palindrom.")
else:
    print("Det är inte ett palindrom.")