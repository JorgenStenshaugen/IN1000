import random
terninger = []
antall_kast = 3
behold = []

input("Trykk en enter for å kaste")

for kastnr in range(antall_kast):
    for kast in range(5-len(behold)):
        terninger.append(random.randint(1,6))
    print(terninger)

    behold = input("Velg hvilke terninger du vil beholde(separer dem med \",\"").split(",")
    if len(behold) > 0:
        behold = list(map(int, behold))
    else:
        behold = 0

    terninger = []
    for velg in behold:

    print(behold)
