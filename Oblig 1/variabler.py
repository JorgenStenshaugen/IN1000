# Spør brukeren om et navn
print("Skriv inn ditt navn")
# Legger verdien i variablen og skriver den ut
navn = input()
print("Hei " + navn)

# Definerer og skriver ut heltallene
tall1 = 6
tall2 = 4
print(tall1)
print(tall2)
# Tar differansen mellom tallene og skriver dem ut
differanse = tall1 - tall2
print("Differanse: ", differanse)

# Spør etter et nytt navn og skriver det ut sammen med det første navnet.
print("Oppgi et nytt navn:")
sammen = navn + input()

# Legger inn et "og" mellom det tidligere navnet og det nye navnet og skriver det ut.
sammen = sammen.replace(navn, navn + " og ")
print(sammen)
