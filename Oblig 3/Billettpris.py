# Lager en prosedyre som heter sjekkPris
def sjekkPris():
    # Dersom brukeren skriver inn noe annet enn heltall vil man få en syntaksfeil.

    # Hent alder og konvert inputet til heltall
    alder = int(input("Din alder: "))

    # Setter bilettprisen til 0
    bilettpris = 0

    # Dersom alderen er mindre eller lik 17 blir prisen 30
    if alder <= 17:
        bilettpris = 30
    # Dersom alderen er større eller lik 63 vil prisen være 35
    elif alder >= 63:
        bilettpris = 35
    # Dersom alderen er større enn 17 vil prisen være 50
    elif alder > 17:
        bilettpris = 50

    # Print ut pris
    print("Pris for bilett:", bilettpris, "\n")

# Kjør prosedyren sjekkAlder 4 ganger i et for loop
for i in range(4):
    sjekkPris()
