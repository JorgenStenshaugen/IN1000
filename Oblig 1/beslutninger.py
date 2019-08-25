# Spør brukeren om den vil ha en brus
print("Vil du ha en brus? (\"Ja\" eller \"nei\")")
# Setter svaret i en variabel
svar = input()

if svar == "ja" :
    # Sjekker dersom verdien på svar variablen er lik "ja" og skriver ut en melding
    print("Her har du en brus!")
elif svar == "nei" :
    # Sjekker dersom svaret er nei vil en annen melding bli skrevet ut
    print("Den er grei.")
else :
    # Dersom svaret er noe annet enn "ja" eller "nei" så skriver vi ut en feilmelding.
    print("Det forstod jeg ikke helt.")
