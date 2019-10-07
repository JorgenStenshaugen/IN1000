# Oppretter klassen
class Hund:
    # Oppretter konstruktør og definerer instansvariabler
    def __init__(self, alder, vekt):
        self.alder = alder
        self.vekt = vekt
        self.metthet = 10

    # Oppretter instansmetode og returnerer vekten
    def hentVekt(self):
        return self.vekt

    # Oppretter instansmetode og returnerer alderen
    def hentAlder(self):
        return self.alder

    # Oppretter instansmetode
    def spring(self):
        # Trekker 1 fra mettheten.
        self.metthet -= 1
        # Dersom mettheten er under 5, så trekker vi 1 fra vekten.
        if self.metthet < 5:
            self.vekt -= 1

    # Oppretter instansmetode med mengde som en parameter
    def spis(self, mengde):
        # Legger til mengde sammen med mettheten
        self.metthet += mengde
        # Om mettheten er større enn 7 så øker vekten med 1
        if self.metthet > 7:
            self.vekt +=1
