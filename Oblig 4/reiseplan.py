# Oppretter en tom liste steder
steder = []
# Spør brukeren om steder og legger dem til i listen 5 ganger gjennom en for løkke.
for reiser in range(5):
    steder.append(input("Sted: "))

# Lager 2 lister og for begge så tar vi inputen til brukeren og legger dem i listen 5 ganger for begge listene.
klesplagg = []
avreisedatoer = []
for elem in range(5):
    klesplagg.append(input("Klesplagg: "))
for elem in range(5):
    avreisedatoer.append(input("Avreisedatoer: "))

# Lager en ny liste som inneholder de tre forrige listene
reiseplan = []
reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedatoer)

# Printer ut alle listene i reiseplan listen ved hjelp av en for løkke
for element in reiseplan:
    print(element)

# Leser inn 2 indekser fra brukeren
i1 = int(input("Indeks: "))
i2 = int(input("Indeks nr2: "))

# Sjekker om i1 og i2 er større eller lik 0 og at den er mindre eller lik størrelsen på listen.
if i1 >= 0 and i1 <= len(reiseplan)-1 and i2 >= 0 and i2 <= len(reiseplan[i1])-1:
    # Skriver ut reiseplanen med indeksene
    print(reiseplan[i1][i2])
else:
    # Dersom i1 og i2 ikke møter kriterene så skriver vi ut en feilmelding.
    print("Ugyldig input!")
