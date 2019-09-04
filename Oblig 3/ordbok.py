varer = {"brød":14.90, "brød":24.90, "yoghurt":12.90, "pizza":39.90}
print(varer)

for i in range(2):
    varenavn = input("Legg til varenavn: ")
    varepris = float(input("Legg til pris: "))
    varer[varenavn] = varepris
    print("\n")

print(varer)
