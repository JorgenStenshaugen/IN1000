
liste = []
tall = int(input("Tall: "))
while tall != 0:
    liste.append(tall)
    tall = int(input("Tall: "))

for x in liste:
    print(x)

minSum = 0
for plus in liste:
    minSum += plus
print("Sum: ", minSum)

minst = liste[0]
for nummer in liste:
    if minst > nummer:
        minst = nummer
        
storst = liste[0]
for nummer in liste:
    if storst < nummer:
        storst = nummer

print("Minst:", minst)
print("Størst:", storst)
