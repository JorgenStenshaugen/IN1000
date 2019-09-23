# Oppretter en tom liste som skal inneholde tallet til brukeren
liste = []
# Tar inn første tall
tall = int(input("Tall: "))

# En while løkke som går helt til brukeren taster 0.
while tall != 0:
    # Legger tallet til brukeren i listen
    liste.append(tall)
    # Spør om neste tall.
    tall = int(input("Tall: "))

# Skriver ut alle tallene i listen ved bruk av en for løkke.
for tall in liste:
    print(tall)

# Setter opp variabel
minSum = 0
# En for løkke som legger sammen verdiene i minSum variabelen
for tall in liste:
    minSum += tall
print("Sum: ", minSum)

# En for løkke som går gjennom hvert tall i listen og sjekker om det er mindre enn forrige
# tall i minste variabelen, dersom den er det så oppdateres variabelen med minste verdi.
minst = liste[0]
for nummer in liste:
    if minst > nummer:
        minst = nummer

# Samme som forrige løkke bare at den sjekker om den er verdien er større
storst = liste[0]
for nummer in liste:
    if storst < nummer:
        storst = nummer

# printer ut begge variabelene
print("Minst:", minst)
print("Størst:", storst)
