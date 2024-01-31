def pris_inkl_moms(pris_exkl_moms, momssats):
    moms = pris_exkl_moms * (momssats / 100)
    pris_inkl_moms = pris_exkl_moms + moms
    return pris_inkl_moms

# funktionen med exempelvärden
exempel_pris_exkl_moms = 10012351  # Ange det pris du vill testa
exempel_momssats = 25  # Ange  momssatsen i procent

pris_inkl_moms_resultat = pris_inkl_moms(exempel_pris_exkl_moms, exempel_momssats)
print(f"Pris inklusive moms: {pris_inkl_moms_resultat:.2f} kr")
