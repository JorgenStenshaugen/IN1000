# Importerer Motorsykkel klassen
from motorsykkel import Motorsykkel

# hovedprogram prosedyren
def hovedprogram():
    # Oppretter 3 objekter med ulike argumenter
    sykkel1 = Motorsykkel("Yamaha", "AB12345", 20)
    sykkel2 = Motorsykkel("Honda", "AB54321", 0)
    sykkel3 = Motorsykkel("Harley Davidson", "AB12453", 300)

    # Skriver ut alle objektene
    sykkel1.skrivUt()
    sykkel2.skrivUt()
    sykkel3.skrivUt()

    # kaller på kjor metoden til det siste objektet og skriver ut motosykkelens kilometerstand
    sykkel3.kjor(10)
    print("Antall km for sykkel nr3: ", sykkel3.hentKilometerstand())

# Kaller på hovedprogrammet
hovedprogram()
