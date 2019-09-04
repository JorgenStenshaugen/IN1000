# Oprrett liste
liste = [3, 6, 9]
# Legg til et nytt tall i listen
liste.append(12)

# Printer ut første og tredje elementet
print(liste[0], liste[2])

# Lager en ny tom liste
nyListe = []

# Legger til et nytt navn 4 ganger i et for loop
for leggTilnavn in range(4):
    # Legger til det nye navnet i den nye listen.
    nyListe.append(input("Oppgi navn nr." + str(leggTilnavn+1) + "\n"))


if "Jørgen" in nyListe:
    # Hvis navnet "Jørgen" ligger i den nye listen.
    print("Du husket meg!")
else:
    # Hvis navnet "Jørgen" ikke ligger i den nye listen.
    print("Du glemte meg!")

# Legg sammen listene
listeSammen = liste + nyListe

# Print ut den sammenlagte listen.
print(listeSammen)
