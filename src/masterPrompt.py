import random
import time

import world as wrd
import player as plyr
# from menu import *
from intro import *

class masterPrompt():
    """parent masterPrompt class"""
    def __init__(self, search=True, inspect=True, inventory=True, back=True):
        # self._north = plyr.Player()._location._north
        # self._south = plyr.Player()._location._south
        # self._east = plyr.Player()._location._east
        # self._west = plyr.Player()._location._west
        self._north = True
        self._south = True
        self._east = True
        self._west = True
        self._search = search
        self._inspect = inspect
        self._inventory = inventory
        self._back = back
        # self._world = world.name
    
    
    @property
    def north(self):
        return self._north
    @property
    def south(self):
        return self._south
    @property
    def east(self):
        return self._east
    @property
    def west(self):
        return self._west
    @property
    def search(self):
        return self._search
    @property
    def inspect(self):
        return self._inspect
    @property
    def inventory(self):
        return self._inventory
    @property
    def back(self):
        return self._back

    @north.setter
    def north(self, x):
        self._north = x
    @south.setter
    def south(self, x):
        self._south = x
    @east.setter
    def east(self, x):
        self._east = x
    @west.setter
    def west(self, x):
        self._west = x
    @search.setter
    def search(self, x):
        self._search = x
    @inspect.setter
    def inspect(self, x):
        self._inspect = x
    @inventory.setter
    def inventory(self, x):
        self._inventory = x
    @back.setter
    def back(self, x):
        self._back = x

# Cardinal
    def displayNorth(self):
        if self._north != None:
            return '{:^10}'.format('[1] North')
        else:
            return '{:^10}'.format('---')
    def displaySouth(self):
        if self._south != None:
            return '{:^10}'.format('[2] South')
        else:
            return '{:^10}'.format('---')
    def displayEast(self):
        if self._east != None:
            return '{:^10}'.format('[3] East')
        else:
            return '{:^10}'.format('---')
    def displayWest(self):
        if self._west != None:
            return '{:^10}'.format('[4] West')
        else:
            return '{:^10}'.format('---')

# Options
    def displaySearch(self):
        if self._search == True:
            return '{:^10}'.format('[5] Search')
        else:
            return '{:^10}'.format('---')
    def displayInspect(self):
        if self._inspect == True:
            return '{:^10}'.format('[6] Inspect')
        else:
            return '{:^10}'.format('---')
    def displayInventory(self):
        if self._inventory == True:
            return '{:^10}'.format('[7] Inventory')
        else:
            return '{:^10}'.format('---')
    
# Back
    def displayBack(self):
        if self._back == True:
            return '{:^10}'.format('[9] Back')
        else:
            return '{:^10}'.format('---')

    def displayPrompt(self):
        textFormat(f"                                                  ▓████████████████                                                     ")
        textFormat(f"▓█ {self.displayNorth()} {self.displaySouth()} {self.displayEast()} {self.displayWest()}  ▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ {self.displaySearch()} {self.displayInspect()} {self.displayInventory()} {self.displayBack()} ▓█")
        textFormat(f"▓█▓▓█▓███╣╣╣████████████████████▓▓████████▓█████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████╣╫▓▓╣▓███▓▓▓▓█████████████████████████╣████████")
        # print("{}{}{}{}{}{}{}{}".format(self.displayNorth(), self.displaySouth(), self.displayEast(), self.displayWest(), 
        #                                self.displaySearch(), self.displayInspect(), self.displayInventory(), self.displayBack()))
                                               


# textFormat(f"                                                    ▓██████████████                                                     ")
# textFormat(f"▓█                                                  ▓█▓▓▓▓▓▓▓▓▓▓▓▓█                                                   ▓█")
# textFormat(f"▓█▓▓█▓███╣╣╣████████████████████▓▓████████▓███████████▓▓▓▓▓▓▓▓▓▓▓▓███████╣╫▓▓╣▓███▓▓▓▓█████████████████████████╣████████")


# def prompt():
#     print("\n" + "========================")
#     print("<What would you like to do?>")
#     action = input("> ")
#     possible_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'look']
#     while action.lower() not in possible_actions:
#         print("Unkknown action, try again.\n")
#         action = input("> ")
#     if action.lower() == 'quit':
#         sys.exit()
#     elif action.lower() in ['move', 'go', 'travel']:
#         player_move(action.lower())
#     elif action.lower() in ['examine', 'inspect', 'look']:
#         player_examine(action.lower())

#     while num <= len(option):
#         print(f'[{num}] {option[n]}')
#         num += 1
#         n += 1

if __name__ == "__main__":
    print('check')
    
    
          # sys.stdout.write("\033[F"*1) 
          # print(' '*30)
          # sys.stdout.write("\033[%d;%dH" % (1, 1)) 
          
# Value countdown
# for n in range(10):
#     print('\r', n, end='')
#     time.sleep(1)
    
# ANSI cursor test
    masterPrompt().displayPrompt()

    print("This is a test.")
    time.sleep(1)
    sys.stdout.write("\033[2J")
    time.sleep(1)
    sys.stdout.write("\033[<10>A")
    time.sleep(1)
    print("This is a test.")
    time.sleep(1)
    sys.stdout.write("\033[<10>:<10>H")
    time.sleep(1)
    sys.stdout.write("\033[s")
    time.sleep(1)
    print("This is a test.")
    time.sleep(1)
    sys.stdout.write("\033[2J")
    time.sleep(1)
    sys.stdout.write("\033[u")
    time.sleep(1)
    print("This is another test.")
    time.sleep(1)