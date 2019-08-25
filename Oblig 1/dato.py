# Spør brukren etter dato gjennom tal og setter dem i variabler
dag1 = int(input("Skriv inn dag: "))
maaned1 = int(input("skriv inn måned: "))
dag2 = int(input("Skriv inn ny dag: "))
maaned2 = int(input("skriv inn ny måned: "))



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
