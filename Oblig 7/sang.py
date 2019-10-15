class Sang:

    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist

    def spill(self):
        print("Spiller av", self._tittel, "-", self._artist)

    def sjekkArtist(self, navn):
        for ord in navn.split():
            for artistOrd in self._artist.split():
                if ord == artistOrd:
                    return True
        return False


    def sjekkTittel(self, tittel):
        for ord in tittel.split():
            for tittelOrd in self._tittel.split():
                if ord.lower() == tittelOrd.lower():
                    return True
        return False

    def sjekkArtistogTittel(self, artist, tittel):
        if self.sjekkArtist(artist) and self.sjekkTittel(tittel):
            return True
