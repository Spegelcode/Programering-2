def �r_palindrom():
    mening = input("Ange ett ord eller mening: ")
    ren_mening = ''.join(mening.lower().split())
    omv�nd_mening = omv�nd_ordning(ren_mening)
    
    return ren_mening == omv�nd_mening
def omv�nd_ordning(text):
    return text[::-1]

if �r_palindrom():
    print("Dert �r ett palindrom.")
else:
    print("Det �r inte ett palindrom.")