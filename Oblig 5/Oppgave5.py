# Lag en prosedyre "registrer" som skal registrere matplanen til en person med hjelp av parametere.
# Prosedyren skal først hente filen ved å lese den og putte verdiene i en egen variabel og lukke filen
# Deretter skal filen åpnes igjen for å skrives på
# Filen skal ta inn elementene som var der fra før av og legge det sammen med de nye verdiene på en ny linje
# Formatet skal være "Navn, Frokost, Lunsj, Middag"
# Så skal filen lukkes og printe ut at personen er lagt til

# Deretter skal du lage en funksjon "hentData" som henter dataen, den skal ikke ta inn noen parametere
# Hent matplanfil.txt, lag en variabel for ordboken
# Deretter skal du hente informasjonen for hver linje i en for løkke
# Og legge til personen i en ordboken
# Så skal filen lukkes og returnere ordboken.

# Lag en prosedyre "hentMatplan" som skal hente matplanen med navn som parameter.
# Prosedyren skal hente matplanen ved å bruke funksjonen som ble lagd tidligere
# Deretter skal du burke en if/else funskjon til å sjekke om persnen finnes i ordboken
# om personen er i ordboken så skal den printes ut, hvis ikke så skal den printe ut at den ikke er registrert.

# Lag en ny prosedyre som heter "skrivUt" som skal ta inn en parameter for ordbok.
# Prosedyren skal gå i en for løkke for ordboken oppgitt i parameteret.
# og skrive ut alle verdiene i ordboken

# Til slutt skal du lage en prosedyre som skal være hovedprogrammet.
# Hovedprogrammet skal ta inn input fra brukeren som Kommandoer
# Hovedprogrammet skal han en while løkke som går mens brukeren ikke har tastet 0
# Om brukeren skrives "1" skal brukeren skrive inn navn, frokost, lunsj og middag
# og legge det til i "registrer" prosedyren.
# Om brukeren skriver "2" skal brukeren skrive inn navn og putte inputet i hentMatplan Prosedyren
# Om brukeren skriver "3" skal du kalle på "skrivUt" prosedyren med "hentData" som parameter.
# Om brukeren skriver et tall som ikke eksisterer så skal den skrive ut at kommandoen ikke eksisterer.

# Til slutt kall på hovedprogrammet.


# Lager prosedyren registrer
def registrer(navn, frokost, lunsj, middag):
    # Henter matplanfilen og leser verdien i en egen variabel.
    # og lukker filen
    matplanFil = open("matplanfil.txt")
    matplan = matplanFil.read()
    matplanFil.close()

    # Henter matplanfilen igjen for å skrive på den
    matplanFil = open("matplanfil.txt", "w")
    # Skriver først verdiene som var i filen fra før av og legger til en \n for ny linje
    # Skriver deretter inn navn, frokost, lunsj og middag i med "," som skille.
    matplanFil.write(matplan + "\n" + navn + "," + frokost + "," + lunsj + "," + middag + "\n")
    matplanFil.close()
    # Lukker filen og skriver ut at personen er registrert.
    print(navn, "er registrert i systemet")

# Lager funksjonen hentData
def hentData():
    # Henter filen igjen.
    data = open("matplanfil.txt")
    # lagre en ny ordbok
    ordbok = {}

    # For løkke som går gjennom linjene ved å splitte dem opp.
    for person in data.read().split():
        # Henter verdiene ved å skille det på ","
        navn = person.split(",")[0]
        frokost = person.split(",")[1]
        lunsj = person.split(",")[2]
        middag = person.split(",")[3]
        # Legger alt i ordboken.
        ordbok[navn] = {"Frokost":frokost, "Lunsj": lunsj, "Middag": middag}

    # Lukker filen
    data.close()

    # Returnerer ordboken.
    return ordbok

# Lager prosedyren med navn som parameter.
def hentMatplan(navn):
    # Henter matplanen ved å kalle på hentData.
    matplan = hentData()

    # Om navnet oppgitt i parametere eksisterer i matplanen så skrives ut personen og matplanen.
    if navn in matplan:
        print(navn, matplan[navn])
    else:
        # Skriv ut at personen ikke finnes.
        print("Personen finnes ikke i registre")

# Lager prosedyren skriv ut med en parameter.
def skrivUt(plan_ordbok):
    # For løkke som skriver ut alle elementene i ordboken oppgitt i parameteret.
    for person in plan_ordbok:
        print(person, plan_ordbok[person])

# Hovedprogram prosedyre
def hoved():
    # Skriver ut instruksjoner
    print("## Matplan")
    print("## Kommandoer:")
    print("## 0 = avslutt")
    print("## 1 = Registerer matplan")
    print("## 2 = Finn matplan til person")
    print("## 3 = skriv ut alle sin matplan")

    # Hneter inn kommando fra bruker input.
    kommando = int(input("\n> "))

    # While løkke mens inputet ikke er 0
    while kommando != 0:
        # Om brukeren skriver "1", så henter vi input som spør etter navn, frokost, lunsj og middag og putter verdiene
        # i registrer prosedyren.
        if kommando == 1:
            registrer(input("Navn: "), input("Frokost: "), input("Lunsj: "), input("Middag: "))
        elif kommando == 2:
            # Om brukeren skriver "2" så henter vi input som spør etter navn og putter det i hentMatplan
            # prosedyren.
            hentMatplan(input("Navn: "))
        elif kommando == 3:
            # Om brukeren skriver "3" så kaller vi på skrivUt prosedyren med hentData funksjonen som paramter.
            skrivUt(hentData())
        else:
            # Om brukeren skriver ett tall som ikke er en kommando, så skrives ut en feilmelding.
            print("Kommandoen eksisterer ikke")

        # Spør etter kommando på nytt
        kommando = int(input("\n> "))

# Kaller på hovedprogrammet
hoved()
