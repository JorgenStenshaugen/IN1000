# Oppretter klassen
class Motorsykkel:
    # Oppretter konstruktøren med merke, registreringsnummer og kilometerstand som parametere og putter dem i instansvariablene.
    def __init__(self, merke, registreringsnummer, kilometerstand):
        self.merke = merke
        self.registreringsnummer = registreringsnummer
        self.kilometerstand = kilometerstand

    # Oppretter instansmetode med km som parameter og øker kilometerstand med seg selv + km argumentet.
    def kjor(self, km):
        self.kilometerstand += km

    # Oppretter instansmetode og returnerer kilometerstand
    def hentKilometerstand(self):
        return self.kilometerstand

    # Oppretter instansmetode som printer ut merke, registreringsnummer og kilometerstand
    def skrivUt(self):
        print(self.merke, self.registreringsnummer, self.kilometerstand)
