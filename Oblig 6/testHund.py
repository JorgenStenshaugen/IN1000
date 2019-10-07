# Importerer klassen
from hund import Hund

# Setter opp hovedprogram
def hovedprogram():
    # Oppretter ny objekt
    hund = Hund(4, 5)
    # Kaller på objektets spring og spis funksjon og printer ut vekten
    hund.spring()
    hund.spis(1)
    print(hund.hentVekt())
    # Kaller på objektets spring og spis funksjon og printer ut vekten
    hund.spring()
    hund.spis(7)
    print(hund.hentVekt())

# Kaller på hovedprogrammet
hovedprogram();
