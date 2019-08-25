
dag1 = int(input("Skriv inn dag: "))
maaned1 = int(input("skriv inn måned: "))
dag2 = int(input("Skriv inn ny dag: "))
maaned2 = int(input("skriv inn ny måned: "))



if dag1 < dag2 and maaned1 <= maaned2 :
    print("Riktig rekkefølge")
elif dag1 == dag2 and maaned1 == maaned2 :
    print("Samme dato!")
else :
    print("feil rekkefølge")
