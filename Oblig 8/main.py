from spillebrett import Spillebrett

def main():
    # Oppretter spillebrett objekt. Spør om antall rader og kolonner fra brukeren.
    brett = Spillebrett(int(input("Oppgi rader: ")),int(input("Oppgi kolonner: ")))
    # Tegner brettet
    brett.tegnBrett()
    # Printer ut generasjonsnummeret og antall levende.
    print("Generasjon:", brett._gen)
    print("Antall levende", brett.finnAntallLevende())

    # Henter input fra brukeren og går i en while løkke som går så lenge brukeren ikke taster "q" eller om brukeren tastet "a"
    tast = input("Enter = neste Generasjon, q = avslutt, automatisk = a\n")
    while tast != "q" or tast == "a":
        if tast == "a":
            # Dersom brukeren skriver "a" så spør vi om hvor mange generasjoner den skal gå gjennom
            antallGens = int(input("Antall generasjoner: "))
            # While løkke som går dersom tallet brukeren har oppgitt er større enn brettets generasjoner
            while antallGens > brett._gen:
                brett.oppdatering()
                print("Generasjon:", brett._gen)
                print("Antall levende", brett.finnAntallLevende())
            # Når løkken er ferdig så spør vi om input igjen.
            tast = input("Enter = neste Generasjon, q = avslutt, automatisk = a\n")
        else:
            # Dersom man skal bare trykke enter for å oppdatere så gjør vi dette.
            brett.oppdatering()
            print("Generasjon:", brett._gen)
            print("Antall levende", brett.finnAntallLevende())
            tast = input("Enter = neste Generasjon, q = avslutt, automatisk = a\n")


# starte hovedprogrammet
main()
