# Prosedyre med navn og bosted variabler som leser input og skriver ut.
def hilsen():
    navn = input("Skriv inn navn: ")
    bosted = input("Hvor kommer du fra? ")
    print("Hei, " + navn + "! Du er fra " + bosted + ".\n")

# Utføre prosedyren "hilsen()" 3 ganger i et for loop
for runder in range(3):
    hilsen()
