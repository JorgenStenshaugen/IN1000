# Lager en variabel og åpner filen temperatur.txt
temperaturfil = open("temperatur.txt")
# Oppretter en liste temperaturer
temperaturer = []

# Tar en for løkke som legger alle verdiene i hver linje i listen
for temperatur in temperaturfil:
     temperaturer.append(int(temperatur))

# Lukker temperaturfilen siden vi ikke trenger den lenger
temperaturfil.close()

# Oppretter funksjonen gjennomsnitt med en parameter
def gjennomsnitt(liste):
    # Setter opp variabel forrigeTall
    forrigeTall = 0
    # Summerer alle verdiene fra listen
    for tall in liste:
        forrigeTall += tall

    # Returnerer summen av alle tallene og deler det på størrelsen
    # til listen for å få gjennomsnittet.
    return forrigeTall/len(liste)

# Skriver ut gjennomsnittet ved å bruke funksjonen gjennomsnitt med
# temperatur listen som argument.
print("Gjennomsnitt: ", gjennomsnitt(temperaturer))
