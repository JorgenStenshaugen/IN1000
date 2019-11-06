class Celle:
    # Konstruktør
    def __init__(self):
        # Setter instansvariabelen "Status"
        self._status = "doed"

    # Endre status til død/levende
    def settDoed(self):
        self._status = "doed"

    def settLevende(self):
        self._status = "levende"

    # Hente status
    def erLevende(self):
        # Returnerer True om statusen er levende, hvis ikke så returnerer den false
        return True if self._status == "levende" else False

    def hentStatusTegn(self):
        # Returnerer tegnet "O" om metoden erLevende returnerer True, hvis ikke så returnerer vi tegnet "."
        return "O" if self.erLevende() else "."
