# Simplifisert fra "dato.py"
# Her henter vi datoen i en dag.mnd format og splitter verdien vekk fra punktummet.
dato1 = int(input("Skriv inn første dato (eks. 7.10): ").split("."))
dato2 = int(input("Skriv inn ny dato (eks. 24.12): ").split("."))

#Vi henter verdiene gjennom et array og utfør samme funksjon som i "dato.py"
if dato1[0] < dato2[0] and dato1[1] <= dato2[1] :
    print("Riktig rekkefølge")
elif dato1[0] == dato2[0] and dato1[1] == dato2[1] :
    print("Samme dato!")
else :
    print("feil rekkefølge")
