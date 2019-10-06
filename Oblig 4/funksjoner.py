# Oppretter en funksjon som tar inn to tall og returnerer summen av tallene
def adder(tall1, tall2):
    return int(tall1) + int(tall2)

# printer ut og bruker funksjonen
print("Legger sammen 3 og 4 som blir:", adder(3,4))
print("Legger sammen 5 og 9 som blir:", adder(5,9))

# Oppretter en funskjon som tar inn en tekst og en bokstav og returnerer
# hvor mange ganger den bokstaven forekommer i teksten
def tellForekomst(minTekst, minBokstav):
    return minTekst.count(minBokstav)

# Henter inn tekst fra brukeren
tekst = input("Skriv inn en tekststreng: ")
# Henter inn bokstav fra brukeren
bokstav = input("Skriv inn en bokstav: ")

# Skrivet ut hvor mange ganger bokstaven forekommer i brukerens tekst ved å
# bruke tellForekomst funksjonen.
print("Bokstaven", bokstav, "Forekommer", tellForekomst(tekst, bokstav), "ganger i teksten")
