# Du skal lage en quiz som henter spørsmål, alternativer og svar gjennom et array
# Deretter skal du sjekke om svaret er riktig eller feil gjennom en if/else funskjon
# Du skal også samle poengsummen og printe den ut til slutt med antall mulige poeng. f.eks 4/10

# Quiz array med spørsmål, alternativer og svar
quiz = [["Hva er hovedstaden i Norge?", "Hva heter Asias største øy?", "I hvilken amerikansk delstat ligger Grand Canyon"], #Spørsmål
        ["A: Stockholm\nB: Oslo\nC: Berlin\n", # Alternativ til spørsmål 1
         "A: Borneo\nB: Bali\nC: Java\n", # Alternativ til spørsmål 2
         "A: Arizona\nB: Florida\nC: Georgia\n"], # Alternativ til spørsmål 3
         ["b", "a", "a"]] # Riktige svar
# sett opp poengsum variabelen
poeng = 0

# Lag et for loop som går gjennom alle spørsmålene.
for antall_spm in range(len(quiz[0])):
    #Printer ut spørsmål og alternativer fra arrayet
    print(quiz[0][antall_spm], "\n")
    print(quiz[1][antall_spm])

    # Henter svar fra brukeren
    svar = input("Svaret ditt:\n> ")

    # Sjekker om svaret er riktig eller galt gjennom en if/else funksjon og printer ut om det er riktig eller feil
    if (svar.lower() == quiz[2][antall_spm]):
        print("Riktig svar!")
        # Legg til poeng
        poeng +=1
    else:
        print("Feil svar!")

    #Ny linje til neste spørsmål
    print("\n")

# Printer ut poengsummen helt til slutt
print("Din poengsum ble:", poeng, "/", len(quiz[0]))
