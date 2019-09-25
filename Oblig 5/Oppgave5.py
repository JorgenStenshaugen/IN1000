

def registrer(navn, frokost, lunsj, middag):
    matplanFil = open("matplanfil.txt", "a")
    matplanFil.write(navn + "," + frokost + "," + lunsj + "," + middag + "\n")
    matplanFil.close()
    print(navn, "er registrert i systemet")

def hentData():
    data = open("matplanfil.txt")
    ordbok = {}
    for person in data.read().split():
        navn = person.split(",")[0]
        frokost = person.split(",")[1]
        lunsj = person.split(",")[2]
        middag = person.split(",")[3]
        ordbok[navn] = {"Frokost":frokost, "Lunsj": lunsj, "Middag": middag}

    data.close()

    return ordbok

def hentMatplan(navn):
    matplan = hentData()
    if navn in matplan:
        print(navn, matplan[navn])
    else:
        print("Personen finnes ikke i registre")

def skrivUt(plan_ordbok):
    for person in plan_ordbok:
        print(person, plan_ordbok[person])

def hoved():
    print("## Matplan")
    print("## Kommandoer:")
    print("## 0 = avslutt")
    print("## 1 = Registerer matplan")
    print("## 2 = Finn matplan til person")
    print("## 3 = skriv ut alle sin matplan")

    kommando = int(input("\n> "))

    while kommando != 0:
        if kommando == 1:
            registrer(input("Navn: "), input("Frokost: "), input("Lunsj: "), input("Middag: "))
        elif kommando == 2:
            hentMatplan(input("Navn: "))
        elif kommando == 3:
            skrivUt(hentData())
        else:
            print("Kommandoen eksisterer ikke")
        kommando = int(input("\n> "))


hoved()
