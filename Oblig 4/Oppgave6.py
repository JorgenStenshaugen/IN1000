# Først lag en ordbok som skal holde alle verdiene
# Lag en prosedyre som tar inn navn og bursdag til vennen
# prosedyren skal legge verdiene inn i ordboken og skrive ut at vennen er lagt til

# Lag en ny prosedyre som skal finne bursdag basert på navn og skrive ut når vennen har bursdag

# Lag enda en prosedyre som printer ut alle vennene og når de har bursdag ved bruk av en for løkke

# Leg en prosedyre som finner venner som har bursdag i en oppgitt måned
# prosedyren skal gå gjennom alle vennene gjennom en for løkke og skal gå i en if sjekk
# sjekk om måneden er lik oppgitt måneden ved å splitte måned formatet

# Lag en siste prosedyre med kommandoer som sjekkes gjennom if/else
# Hver kommando skal bestemme hvilken prosedyre som skal brukes
# Det skal være en kommando for hver prosedyre
# På slutten av denne prosedyren så skal prosedyren kalle på seg selv en while løkke
# slik at brukeren kan skrive en ny kommando etter at forrige kommando er utført



# Lag en ordbok som holder alle vennene
bursdagTilVenner = {}

# Prosedyre som tar inn to argumenter, en for navn og en for bursdagen
def leggTilvenn(navn, bursdag):
    # Legg til vennen i orboken og print ut at vennen er lagt til i grønn farge.
    bursdagTilVenner[navn] = bursdag
    print("\033[92m" + navn, "har blitt lagt til og har bursdag", bursdag, "\n\033[0m")

# Prosedyre som tar inn et navn
def finnBursdag(navn):
    # Skriver ut navnet og finner bursdagen ved å hente det fra ordboken
    print("\033[92m" + navn, "har bursdag den", bursdagTilVenner[navn], "\n\033[0m")

# prosedyre som går i en for løkke og skriver ut alle vennene og bursdagene dems
def printAlle():
    for navn in bursdagTilVenner:
        print("\033[92m" + navn, "har bursdag den", bursdagTilVenner[navn], "\n\033[0m")

# Prosedyre som henter inn måned fra brukeren
def finnMaaned(maaned):
    # For løkke som går gjennom alle navnene i ordboken
    for navn in bursdagTilVenner:
        # Sjekker om brukerens måned er lik den siste indeksen i listen opprettet av split prosedyren
        # Vi splitter bursdagen mellom "." tegnet slik at vi får en liste med 2 indekser(0 og 1)
        # Vi trenger bare siste indeksen(1) siden bare måneden er nødvendig
        if maaned == bursdagTilVenner[navn].split(".")[1]:
            # Dersom den er lik så printer vi ut navene som har bursdag denne måneden.
            print("\033[92m" + navn, "har bursdag den", bursdagTilVenner[navn].split(".")[0], "denne måneden\n\033[0m")

# Prosedyre som tar inn kommandoer
def lesKommando():
    # Instrukser til hvordan kommandoene fungerer
    print("## Skriv inn kommando;")
    print("## 0 = stopper programmet")
    print("## 1 = Legg til en venn med bursdag.")
    print("## 2 = Finn bursdag til en venn.")
    print("## 3 = Finn alle som har bursdag i en spesifikk måned.")
    print("## 4 = Skriv ut alle bursdager venner.")

    # Setter opp en variabel som tar inn kommandoen fra brukeren
    kommando = int(input("> "))

    # Setter opp kommandoene opp mot prosedyrene som ble opprettet tidligere og utfører dem
    if kommando == 1:
        leggTilvenn(input("Navn: \n> "), input("Bursdag(format: dd.mm):\n> "))
    elif kommando == 2:
        finnBursdag(input("Navn:\n> "))
    elif kommando == 3:
        finnMaaned(input("Måned:\n> "))
    elif kommando == 4:
        printAlle()
    else:
        # Om brukeren skriver noe ugyldig og ikke 0
        if kommando != 0
            print("Kommandoen finnes ikke")

    # Kaller prosedyren på seg selv slik at programmet fortsetter i en while løkke
    # dersom brukeren skriver inn 0 så stopper programmet.
    while kommando != 0:
        lesKommando()

# Kaller på lesKommando for å starte programmet
lesKommando()
