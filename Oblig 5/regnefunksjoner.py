# Oppretter funksjon addisjon med to parametere og returnerer summen.
def addisjon(tall1, tall2):
    return tall1 + tall2

# Kaller på og printer ut verdien returnert av funksjonen addisjon
print(addisjon(4, 6))

# Oppretter funksjonen subtraksjon med to parametere
def subtraksjon(tall1, tall2):
    return tall1 - tall2

# Oppretter funksjonen divisjon med to parametere
def divisjon(tall1, tall2):
    return tall1/tall2

# Tester funksjonen subtraksjon med assert.
assert subtraksjon(6, 4) == 2
assert subtraksjon(-3, -4) == 1
assert subtraksjon(4, -2) == 6

# Tester funksjonen divisjon med assert.
assert divisjon(6, 2) == 3
assert divisjon(-4, -4) == 1
assert divisjon(-15, 3) == -5

# Oppretter funksjonen tommerTilCm
# Tester om antallTommer variabelen er større enn 0 med assert
# Returnerer konverrtingen fra tommer til cm.
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer * 2.54

# Tester om tommerTilCm returnerer riktig verdi med hjelp av assert
assert tommerTilCm(5) == 12.7

# Oppretter funksjonen skrivBeregninger
def skrivBeregninger():
    # Tar inn 2 tall fra brukeren
    tall1 = float(input("Utregninger:\nSkriv inn tall 1: "))
    tall2 = float(input("Skriv inn tall2: "))
    # Printer ut resultat fra brukerens tall i funksjonene ovenfor
    print("\nResultat av addisjon: ", addisjon(tall1, tall2))
    print("Resultat av subtraksjon: ", subtraksjon(tall1, tall2))
    print("Resultat av divisjon: ", divisjon(tall1, tall2))

    # Tar inn ett nytt tall som brukes i tommerTilCm funksjonen og printer ut
    tall3 = float(input("\nKonverter tommer til cm\nTall: "))
    print("Resultat: ", tommerTilCm(tall3))

# Kaller på prosedyren skrivBeregninger
skrivBeregninger()
