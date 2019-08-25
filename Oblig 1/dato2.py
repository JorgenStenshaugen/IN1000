# Simplifisert fra "dato.py"
# Her henter vi datoen i en dag.mnd format og splitter verdien vekk fra punktummet.
dato1 = input("Skriv inn første dato (eks. 7.10): ").split(".")
dato2 = input("Skriv inn ny dato (eks. 24.12): ").split(".")

# Vi henter verdiene gjennom et array og utfør samme funksjon som i "dato.py"
# Bruker funskjonen int() for å sikkre at verdiene blir tatt inn som heltall.
dag1 = int(dato1[0])
dag2 = int(dato2[0])
maaned1 = int(dato1[1])
maaned2 = int(dato2[1])

if dag1 < dag2 and maaned1 <= maaned2 :
    # Sjekker om dag1 er før dag2 og om maaned1 er før eller den samme.
    # Deretter skriver vi ut at datoen er i riktig rekkefølge
    print("Riktig rekkefølge")
elif dag1 == dag2 and maaned1 == maaned2 :
    # Her sjekker vi om datoene er helt like og skriver ut en melding.
    print("Samme dato!")
else :
    # Dersom dag1 og maaned1 er etter dag2 og maaned2 skriver vi ut en feilmelding
    print("feil rekkefølge")
