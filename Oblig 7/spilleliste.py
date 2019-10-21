from sang import Sang

class Spilleliste:
    # Instansmetode som tar in parameteren "listenavn"
    def __init__(self, listenavn):
        # Setter instansvariabelen _sanger til en liste
        # og setter _navn til listenavn argumentet.
        self._sanger = []
        self._navn = listenavn

    # Metode som tar inn "filnavn" som parameter
    def lesFraFil(self, filnavn):
        # Åpner filen
        sangFil = open(filnavn)

        # For løkke som går gjennom hver linje og legger
        # sang objektet med tittel og artist i "_sanger" listen.
        for linje in sangFil.read().split("\n"):
            tittel = linje.split(";")[0]
            artist = linje.split(";")[1]
            self._sanger.append(Sang(tittel, artist))
        # Lukker filen.
        sangFil.close()


    # Metode som tar inn parameteren "nySang" og legger den i "_sanger" listen.
    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    # Metode som tar inn parameteren "sang" og fjerner den fra listen.
    def fjernSang(self, sang):
        self._sanger.remove(sang)

    # Metode som tar inn en parameter sang, som skal være et objekt og
    # kaller det objektets "spill()" metode.
    def spillSang(self, sang):
        sang.spill()

    # Metode som går gjennom alle sang objektene i "_sanger" listen og
    # kaller på objektets "spill()" metode.
    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()

    # Funksjonsmetode som tar inn parameteret "tittel"
    def finnSang(self, tittel):
        # Går gjennom for løkke som går gjennom alle objektene i "_sanger" lista.
        for sang in self._sanger:
            # Dersom objektets "sjekkTittel" metode returnerer True, så returnerer vi sang objektet.
            if sang.sjekkTittel(tittel):
                return sang
        # Dersom for løkken ikke returnerer noe så returnerer vi None.
        return None

    # Funksjonsmetode som tar inn parameteren "artistnavn"
    def hentArtistUtvalg(self, artistnavn):
        # Oppretter enn ny liste som skal ta inn nye Sang objekter.
        nyListe = []
        # For løkke som går gjennom "_sanger" listen.
        for sang in self._sanger:
            # Dersom objektets metode "SjekkArtist" returnerer True så legger vi
            # objektet i den nye listen.
            if sang.sjekkArtist(artistnavn):
                nyListe.append(sang)
        # Når løkken er ferdig så returnerer vi den nye listen.
        return nyListe
