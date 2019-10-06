# Oppretter en ny liste mineOrd
mineOrd = []
# Oppretter funksjonen slaaSammen som tar inn 2 parametere
# og slår dem sammen og returnerer verdien.
def slaaSammen(str1, str2):
    return str(str1) + str(str2)

# Oppretter prosedyren skrivUt som tar inn en parameter
# og printer ut hvert element fra argumentet
def skrivUt(liste):
    for element in liste:
        print(element)

# Henter brukerinput og legger verdien i en variabelen
kommando = input("Kommando: > ")
# While løkke som går så lenge brukeren ikke skriver "s"
while kommando != "s":
    # Om brukeren skriver "i" så legger vi sammen to strenger fra
    # bruker input gjennom slaaSammen funksjonen
    # og legger resultatet fra funksjonen i mineOrd liste
    if kommando == "i":
        mineOrd.append(slaaSammen(input("Første strenge: "), input("Andre strenge: ")))
    elif kommando == "u":
        # Om brukeren skriver inn "U" så bruker vi skrivUt prosedyren
        # med listen mineOrd som et argument
        skrivUt(mineOrd)
    # Oppdater variabelen med nytt input fra brukeren.
    kommando = input("Kommando: > ")
