# Oppretter en funksjon som returnerer hvor mange bokstaver det er i oppgitte ordet.
def antallBokstaver(ord):
    return len(ord)

# Oppretter funksjon som tar inn en setning
def antallOrd(setning):
    # Gjør om alle ordene til små bokstaver
    # slik at om det er stor forbokstav så telles den og
    setning = setning.lower()

    # Finner antall ord ved å splitte setningen til en liste og skriver ut.
    print("Det er", len(setning.split()), "ord i setningen din.")

    #Oppretter en ordbok
    ordbok = {}
    # Tar inn alle ordene og gjør setningen til en mengde slik at vi ikke får duplikater
    for ord in set(setning.split()):
        # Deretter teller vi hvor mange ganger ordet oppstår i opprinnelige teksten
        # og legger det til i ordboken
        ordbok[ord] = setning.count(ord)

    # til slutt så returnerer vi ordboken
    return ordbok

# Tar inn returnert ordbok fra funksjonen med brukerens input.
returnertOrdbok = antallOrd(input("Skriv en setning:\n"))

# Går gjennom hvert ord i returnerte ordboken
for ord in returnertOrdbok:
    # Skriver ut ordet ved å hente opplysninger fra løkka og fra den returnerte ordboken
    # og teller hvor mange bokstaver det er i ordet ved hjelp av den første funksjonen vår
    print("Ordet", ord, "forekommer", returnertOrdbok[ord], "ganger, og har", antallBokstaver(ord), "bokstaver")
