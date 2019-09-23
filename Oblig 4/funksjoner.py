def adder(tall1, tall2):
    return int(tall1) + int(tall2)


print("Legger sammen 3 og 4 som blir:", adder(3,4))
print("Legger sammen 5 og 9 som blir:", adder(5,9))

def tellForekomst(minTekst, minBokstav):
    return minTekst.count(minBokstav)

tekst = input("Skriv inn en tekststreng: ")
bokstav = input("Skriv inn en bokstav: ")

print(tellForekomst(tekst, bokstav))
