# Declare all the rooms
from game import Game
import os, sys, termios, fcntl

def getch(): # Credit to https://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user for this solution!
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

    try:
        while True:
            try:
                c = sys.stdin.read(1)
                break
            except IOError: pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
    return c

game = Game()
gameActions = ["w", "a", "s", "d", " "]

def doAction(action):
    print()
    if action == "w":
        game.moveUp()
    elif action == "a":
        game.moveLeft()
    elif action == "s":
        game.moveDown()
    elif action == "d":
        game.moveRight()

while(True):
    action = getch()
    
    if action == "x":
        print("Ending game")
        break

    if action in gameActions:
        doAction(action)
    elif action == '':
        continue
    else:
        print()
        game.updateMap(False)