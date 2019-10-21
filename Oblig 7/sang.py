class Sang:
    # Instansmetode med 2 parametere, "tittel" og "artist".
    def __init__(self, tittel, artist):
        # Instansvariabelene
        self._tittel = tittel
        self._artist = artist

    # Metode som printer ut Instansvariabelene
    def spill(self):
        print("Spiller av", self._tittel, "-", self._artist)

    # Funksjonsmetode som tar inn parameteren "navn"
    def sjekkArtist(self, navn):
        # For loop som går gjennom "navn" splittet opp
        # Slik at den sjekker alle mellomnavn osv.
        for navnSplittet in navn.split():
            # For loop som går gjennom navnene på selve artisten splittet opp.
            for artistNavn in self._artist.split():
                # Dersom navnSplittet matcher en av en av "artistNavn"ene.
                # Så returnerer den True.
                if navnSplittet == artistNavn:
                    return True
        # Dersom for løkken ovenfor ikke returner True, så returnerer funksjonen False
        return False

    # Funksjonsmetode som tar in parameteren "tittel"
    def sjekkTittel(self, tittel):
        # For løkke som går gjennom ordene i "tittel".
        for ord in tittel.split():
            # For løkke som går gjennom alle ordene i tittelen til dette objektet.
            for tittelOrd in self._tittel.split():
                # Sjekker om ordet matcher objektets ord i tittelen.
                # Gjør begge til småbokstaver slik at stor og små bokstav ikke
                # påvirker sjekken. Dersom det matcher så returnerer vi True.
                if ord.lower() == tittelOrd.lower():
                    return True
        # Om ikke for løkken returnerer noe så returnerer vi False.
        return False

    # Funksjonsmetode som tar inn 2 parametere, "artist" og "tittel".
    def sjekkArtistogTittel(self, artist, tittel):
        # Bruker funksjonsmetodene sjekkArtist og "sjekkTittel"
        # Dersom begge metodene returnerer True, så returnerer denne metoden True.
        # Ellers så returnerer den False. (True and True = True, False and True = False)
        return self.sjekkArtist(artist) and self.sjekkTittel(tittel)
