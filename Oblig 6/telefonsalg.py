# Oppretter funksjon innlesing med filnavn som parameter
def innlesing(filnavn):
    # Åpner fil med filnavn som argument
    fil = open(filnavn)
    # Oppretter en tom ordbok
    ordbok = {}
    # For hver linje
    for person in fil:
        # legger til navnet fra første elementet fra split funksjonen
        navn = person.split(" ")[0]
        # legger til antallSalg fra andre elementet fra split funksjonen
        antallSalg = int(person.split(" ")[1])
        # Legger til nytt element i ordboken
        ordbok[navn] = antallSalg

    # Lukker filen
    fil.close()
    # Returnerer ordboken
    return ordbok

# Oppretter prosedyre med ordbok som parameter
def maanedensSalgsperson(ordbok):
    # Lager to variabler som skal brukes til å finne den som har solgt mest
    solgtMest = 0
    salg = 0
    # for løkke som går gjennom hvert elemnt i ordboken
    for person in ordbok:
        # Dersom salget er høyere enn verdien i salg variabelen
        if ordbok[person] > salg:
            # Erstatt salg variabelen med salg verdien i ordboken
            salg = ordbok[person]
            # legg navnet på denne personen i solgtMest verdien slik at vi kan hente navnet senere.
            solgtMest = person
    # Skriv ut den som har solgt mest ved bruk av solgtMest og salg variablene.
    print("Månedens ansatte er:", solgtMest, "med", salg, "salg")

# Oppretter funksjon med ordbok som parameter
def totaltAntallSalg(ordbok):
    # Setter antallSalg til 0
    antallSalg = 0
    # En for løkke som går gjennom hvert element i ordboken og legger sammen verdien som er i antallSalg med salget til personen.
    for person in ordbok:
        antallSalg += ordbok[person]
    # Returnerer den samlende verdien
    return antallSalg

# Oppretter funksjonen med ordbok som parameter og returnerer gjennomsnittet ved å kalle på totaltAntallSalg funksjonen og deler det på lengden til ordboken
def gjennomsnittSalg(ordbok):
    return totaltAntallSalg(ordbok)/len(ordbok)


# hovedprogram prosedyre
def hovedprogram():
    # Henter ordboken ved filnavn som argument
    ordbok = innlesing("salgstall.txt")
    # Kaller på på prosedyren som skriver ut månedens ansatt
    maanedensSalgsperson(ordbok)
    # Printer ut statistikk
    print("Antall selgere denne måneden:", len(ordbok))
    print("Totalt antall salg:", totaltAntallSalg(ordbok))
    print("Gjennomsnitt salg:", gjennomsnittSalg(ordbok))

# Kaller på hovedprogrammet
hovedprogram()
