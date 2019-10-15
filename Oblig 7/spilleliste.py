from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        data = open(filnavn)

        for linje in data.read().split("\n"):
            tittel = linje.split(";")[0]
            artist = linje.split(";")[1]
            self._sanger.append(Sang(tittel, artist))

        data.close()


    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        self._sanger.remove(sang)

    def spillSang(self, sang):
        sang.spill()

    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()

    def finnSang(self, tittel):
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                return sang
        return None

    def hentArtistUtvalg(self, artistnavn):
        nyListe = []
        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn):
                nyListe.append(sang)

        return nyListe
