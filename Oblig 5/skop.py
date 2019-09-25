# Først defineres funksjonen minFunksjon() som ikke skal ta inn noen parametere
# Deretter defineres prosedyren hovedprogram() som også ikke skal ta inn noen parametere
# Så kaller den på prosedyren hovedprogram()
# Inne i hovedprogram opprettes variabelen "a" med verdien "42"
# Så opprettes en til variabel "b" med verdien "0"
# Deretter skrives variabelen "b" ut som blir "0"
# Så endres variabelen "b" til å være lik variabelen "a"
# Videre endres variabelen "a" til å være lik minFunksjon()
# minFunksjon() blir kalt på og går gjennom en for løkke i en range(2) som vil si at den
# går gjennom 2 indekser(0 og 1).
# første runden i for løkken kjøres
# Variabelen "c" opprettes og får verdien "2"
# deretter skrives variabelen "c" ut og vi får ut "2"
# Så endres variabelen til å plusse seg selv med "1" slik at variabelen blir 3
# Så opprettes en variabel "b" i denne funksjonen som ikke er relatert med "b" i hovedprogram()
# "b" settes til verdien 10
# Så prøver programmet å endre variabelen "b" med å plusse seg selv med "a"
# Siden "a" ikke eksisterer i denne funksjonen vil vi få en programfeil siden a ikke
# er oprettet i denne funksjonen og finnes bare lokalt i prosedyren hovedprogram()
