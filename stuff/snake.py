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

def lagBrett():
    radOpsett.clear()
    brett.clear()
    for opsett in range(antallRader):
        radOpsett.append("x")
    for brettHentRader in range(antallKolonner):
        brett.append(["x", "x", "x", "x", "x", "x", "x", "x", "x"])
            #print(rader)
    for rad in brett:
        opsett = '| {0} | {1} | {2} |'.format(rad[0], rad[1], rad[2])
        #print(opsett)


def move(screen):
    global x
    global y
    #print("------")
    #print("_")
    #print("------")

    #print()
    oppsett = "0#"
    screen.timeout(0)
    while (True):
        for rad in range(len(brett)):
            #for a in range(3):
            brett[y][x] = "\033[1;32;47m"+"O"+"\033[1;32;40m"
                #brett[y][x-1] = "x"

            #print(oppsett+"\n")
            screen.addstr(0,0, oppsett)
        if x < antallRader:
            x+=1
            brett[y][x-1] = "x"
        if x==antallRader:
            x=0
            #y+=1
        if y < antallKolonner:
            brett[y-1][2] = "x"
        else:
            x = 0
            y = 0

        screen.refresh()
        time.sleep(0.3)



lagBrett()
curses.wrapper(move)
#intervaler(move, 0.0005)
