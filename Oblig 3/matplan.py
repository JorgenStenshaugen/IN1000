matplan = {"Kari Nordmann":{"frokost":"brød","lunsj":"egg","middag":"pølser"}}

def sjekkMatPlan():
    beboer = input("Skriv inn navn på beboer: ")
    if beboer in matplan:
        print(matplan[beboer])
    else:
        print("Beboren er ikke registrert.")

sjekkMatPlan()

# Oppgave 3:
# a) Liste, Siden du trenger bare å hente en enkelverdi og har en rekkefølge du kan bruke for å hente spesifike brukere på
# b) Ordbok, siden du har flere verdier knyttet til en verdi.
# c og d) Mengde, siden du ikke har noen duplikater, det er ingen fast rekkefølge
# og det er raskere og hente, legge til og fjerne elementer
