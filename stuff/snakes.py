import threading
import os
import getch

import curses
import time
import sys

os.system('cls' if os.name == 'nt' else 'clear')

antallRader = 9
antallKolonner = 9

radOpsett = []
brett = []

x = 0
y = 0

def intervaler(funksjon, tid):
    event = threading.Event()
    while not event.wait(tid):
        funksjon()

class Brett:
    """docstring for Brett."""

    def __init__(self, l, h):
        self.brikker = [" . ", " o ", " O ", "[]"]
        self.lengde = l
        self.hoyde = h
        self.settOpp()
        self.s_posisjon = []

    def settOpp(self):
        self.brett = [[0 for j in range(self.lengde)] for i in range(self.hoyde)]

    def _clear_field(self):
        self.field = [[j if j!= 1 and j!= 2 else 0 for j in i] for i in self.brett]


    def oppdater(self, screen):
        lengde = self.lengde
        hoyde = self.hoyde
        self._clear_field()

        for i, j in self.s_posisjon:
            self.brett[i][j] = 0

        #spiller
        playerPos = self.s_posisjon[-1]
        self.brett[playerPos[0]][playerPos[1]] = 2

        for i in range(hoyde):
            rad = ""
            for j in range(lengde):
                rad += self.brikker[self.brett[i][j]]
            screen.addstr(i, 0, rad)

class Player:

    def __init__(self, navn):
        self.navn = navn
        self.retning = curses.KEY_RIGHT

        self.posisjon = [[0, 0], [0, 1], [0, 2], [5, 3]]

    def registrerBevegelse(self, key):

        self.retning = key
        self.beveg()

    def _check_limit(self, point):
        # Check brett limit
        if point[0] > self.brett.lengde-1:
            point[0] = point[0]-1
        elif point[0] < 0:
            point[0] = 0
        elif point[1] < 0:
            point[1] = 0
        elif point[1] > self.brett.hoyde-1:
            point[1] = point[1]-1
        return point

    def beveg(self):
        # Determine head posisjon
        head = self.posisjon[-1][:]

        if self.retning == curses.KEY_UP:
            head[0] -=1
        elif self.retning == curses.KEY_DOWN:
            head[0] +=1
        elif self.retning == curses.KEY_RIGHT:
            head[1] +=1
        else:
            head[1] -=1

        # Check brett limit
        head = self._check_limit(head)

        del(self.posisjon[0])
        self.posisjon.append(head)
        self.brett.s_posisjon = self.posisjon

    def sett_brett(self, brett):
        self.brett = brett



def move(screen):
    global x
    global y
    #print("------")
    #print("_")
    #print("------")

    #print()
    oppsett = "0#"
    screen.timeout(0)
    brett = Brett(10,10)
    slange = Player("Jay")
    slange.sett_brett(brett)
    slange.beveg()
    while (True):
        key = screen.getch()
        if key != -1:
            # If some arrows did pressed - change direction
            slange.registrerBevegelse(key)


        brett.oppdater(screen)

        screen.refresh()
        time.sleep(0.3)


curses.wrapper(move)
#intervaler(move, 0.0005)
