# Declare all the rooms
from game import Game
from location import TermColors, Direction
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

def doAction(action):
    if action == "w" or action == "A":
        game.move(Direction.UP)
    elif action == "a" or action == "D":
        game.move(Direction.LEFT)
    elif action == "s" or action == "B":
        game.move(Direction.DOWN)
    elif action == "d" or action == "C":
        game.move(Direction.RIGHT)
    elif action == " ":
        game.performAction()
    elif int(action) in range(1, 10):
        game.switchWeapon(int(action) - 1)

startScreen = ""
with open("lambda_ascii_shield.txt", "r") as shield:
    # Artwork is original, but text was generated from http://patorjk.com/software/taag/#p=display&f=Ogre&t=Sword%20and%20Shield
    for index, line in enumerate(shield.readlines()):
        if index >= 30:
            break
        startScreen += line
    startScreen += "\n" * 6
    startScreen += f"\n{TermColors.OKGREEN}Press 'Enter' start or 'x' to quit{TermColors.ENDC}"
    print(startScreen)

gameActions = ["w", "a", "s", "d", " ", "A", "B", "C", "D", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

play = True
while(True):
    action = getch()
    print(action)
    if action == '\n':
        break
    elif action == 'x':
        play = False
        break

if play:
    game = Game("map1.txt")
while(play):
    action = getch()
    
    if action == "":
        continue
    elif action == "x":
        print(f"{TermColors.HEADER}Ending game{TermColors.ENDC}")
        break
    elif action in gameActions:
        doAction(action)
    else:
        game.updateMap(False)