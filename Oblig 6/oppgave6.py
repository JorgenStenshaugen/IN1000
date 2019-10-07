# Skriv en klasse Person med en konstruktør som tar imot navn og alder. I tillegg skal
# konstruktøren ha en tom liste hobbyer. Skriv en metode leggTilHobby som tar imot
# en tekststreng og legger den til i hobbyer-listen. Skriv også en metode skrivHobbyer.
# Denne metoden skal skrive alle hobbyene etter hverandre på en linje. Gi deretter
# Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og alder kaller på
# metoden skrivHobbyer. La brukeren skrive inn navn og alder, og lag et Person-objekt
# med informasjonen du får. Deretter skal brukeren ved hjelp av en løkke få legge til så
# mange hobbyer de vil. Når brukeren ikke lenger ønsker å oppgi hobbyer skal
# statistikk om brukeren skrives ut.

# Oppretter klassen
class Person:
    # Oppretter konstruktøren med navn og alder som parametere og setter de i instansvariablene navn og alder
    # Oppretter en til instansvariabel som er en tom liste
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder
        self.hobbyer = []

    # Opprettter instansmetode med en parameter som blir lagt inn i listen
    def leggTilHobby(self, hobby):
        self.hobbyer.append(hobby)

    # Oppretter instansmetode som printer ut hobbyene
    def skrivHobbyer(self):
        print("Hobbyer:", self.hobbyer)

    # Oppretter instansmetode som skriver ut navn, alder og kaller på skrivHobbyer()
    def skrivUt(self):
        print("Navn:", self.navn)
        print("Alder:", self.alder)
        self.skrivHobbyer()

# Oppretter et hovedprogram
def hovedprogram():
    # Oppretter et objekt som tar input som argumenter.
    person = Person(input("Navn: "), int(input("Alder: ")))

    # Henter hobby fra bruker input
    hobbyInput = input("Legg til hobby(0 for når man er ferdig): ")

    # En while løkke som går mens brukeren ikke skriver 0
    while hobbyInput != "0":
        # Legger til hobbyen i objektes leggTilHobby metode.
        person.leggTilHobby(hobbyInput)
        hobbyInput = input("Hobby: ")
    # skriver ut statistikk fra objektet.
    person.skrivUt()

# Kaller på hovedprogrammet
hovedprogram()
