from random import randint
from celle import Celle
#importerer rammeverket os for å tømme terminalen
import os

class Spillebrett:
    def __init__(self, rader, kolonner):
        # Setter instansvariabelene
        self._rader = rader
        self._kolonner = kolonner
        self._brett = []
        self._gen = 0
        # For loop som går lager en nøstet liste
        for k in range(self._kolonner):
            # Legger til en liste i brett listen.
            self._brett.append([])
            for r in range(self._rader):
                # Legger til celle objektet i den opprettet listen.
                self._brett[k].append(Celle())

        # Kaller på "_generer" metoden for å sette noen i live
        self._generer()


    def tegnBrett(self):
        # Tømmer terminalen og legger til en ny linje
        os.system('clear')
        print("\n")
        # For løkke som går gjennom brettet og printer ut cellens statustegn
        for k in self._brett:
            for r in k:
                # Legger til mellomrom mellom for ordens skyld og gjør at den ikke gjør linjeskift
                print("", r.hentStatusTegn(), "", end="")
            # Printer ny linje til neste kolonner.
            print("\n")

    def oppdatering(self):
        # Oppretter to lister som skal inneholde levende og døde celler.
        doed = []
        levende = []

        # Løkke som går gjennom cellene i brettet
        for k in range(self._kolonner):
            for r in range(self._rader):
                # Setter antall levende naboer til 0
                levendeNaboer = 0
                # Sjekker naboen til cellen
                naboer = self.finnNabo(r, k)

                # Løkke som går gjennom naboene og legger dem til antall levende naboer.
                for nabo in naboer:
                    if nabo.erLevende():
                        levendeNaboer +=1

                # Spill reglene skjer her
                # Sjekker om cellen vi er på er levende.
                if self._brett[k][r].erLevende():
                    # Dersom den er levende så skal den dø dersom den har mindre enn 2 naboer eller mer enn 3.
                    # Hvis ikke så gjør vi ikke noe mer med den, siden den skal leve hvis den har 2 eller 3 naboer.
                    if levendeNaboer < 2 or levendeNaboer > 3:
                        # Legger til cellen i død listen
                        doed.append(self._brett[k][r])
                else:
                    # Dersom cellen vi er på er død og har totalt 3 levende naboer så legges cellen i levende listen.
                    if levendeNaboer == 3:
                        levende.append(self._brett[k][r])

        # Går gjennom alle cellene i "doed" listen og setter cellen død.
        for celle in doed:
            celle.settDoed()

        # Går gjennom alle cellene i "levende" listen og setter cellen til levende.
        for celle in levende:
            celle.settLevende()

        # Tegner brettet og oppdaterer generasjonsnummeret.
        self.tegnBrett()
        self._gen += 1

    def finnAntallLevende(self):
        # Setter antalllevende til 0
        antallLevende = 0
        # Går gjennom alle cellene i brettet
        for x in self._brett:
            for y in x:
                # Legger til dersom cellen er levende.
                if y.erLevende():
                    antallLevende += 1
        # Returnerer antall levende i brettet.
        return antallLevende

    def _generer(self) :
        # Går gjennom brettet
        for k in range(self._kolonner):
            for r in range(self._rader):
                # Dersom randomint gir oss 1 så setter vi cellen til levende, dette gir 1/3 sjanse for å være levende
                if (randint(0, 2) == 1):
                    self._brett[k][r].settLevende()

    def finnNabo(self, rad, kolonne):
        # Lager liste for naboen.
        naboer = []
        # Går gjennom cellene som ligger 3 rundt fra rad og kolonnene som er blitt oppgitt
        for k in range(kolonne-1, kolonne+2):
            for r in range(rad-1, rad+2):
                # Sjekker om cellen ikke er den cellen vi har valgt.
                if (r != rad) or (k != kolonne):
                    # Passer på at naboen er innenfor brettet
                    if (r >= 0 and k >= 0) and (r < self._kolonner) and (k < self._rader):
                        # Dersom den går gjennom alle sjekkene så legger vi naboene vi fant i listen
                        naboer.append(self._brett[k][r])
                        
        # Returnerer nabolisten.
        return naboer
