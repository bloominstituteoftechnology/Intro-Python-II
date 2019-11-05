import sys
import time
from color import Color
from textwrap import wrap

class GameObj:
    def __init__(self, name, desc, holding=[], isDark=False):
        desc = wrap(desc, 50)
        self.name = name
        self.desc = '\n'.join(desc)
        self.holding = holding
        self.isDark = isDark
        self.seen = False

    def crawlText(self, text, delay=0.01):
        text = wrap(text, 50)
        text = '\n\r'.join(text)
        for ln in text:
            sys.stdout.write(ln)
            sys.stdout.flush()
            time.sleep(delay)
        print('\n')

    def showHelp(self):
        print(f'{Color.RED}go{Color.END} [{Color.PURPLE}north, east, west, south{Color.END}] {Color.GREEN}$ Move in that direction (ex. go north){Color.END}')
        print(f'{Color.RED}get{Color.END} [{Color.RED}item{Color.END}] {Color.GREEN}$ Pick up an item you see (ex. get Rubber Duck){Color.END}')
        print(f'{Color.RED}drop{Color.END} [{Color.RED}item{Color.END}] {Color.GREEN}$ Drop an item you are holding (ex. drop Flashlight){Color.END}')
        print(f'{Color.RED}use{Color.END} [{Color.RED}item{Color.END}] {Color.GREEN}$ Use an item you are holding (ex. use Flashlight){Color.END}')
        print(f'{Color.RED}look{Color.END} {Color.GREEN}$ Observe your surroundings{Color.END}')
        print(f'{Color.RED}q{Color.END} {Color.GREEN}$ Quit{Color.END}')

    def showItems(self):
        if self.isDark == True:
            return None
        items = [i.name for i in self.holding]
        itemString = ', '.join(items)
        if len(items) > 0:
            itemString = f'{Color.RED}{items}{Color.END}'
            return itemString
        else: return None

    def quitGame(self):
        print('\n')
        self.crawlText(f'{Color.RED}Your mind feels electric, the taste of copper fills your mouth, and you wonder:')
        self.crawlText(f'{Color.PURPLE} "Is this real? Am I dreaming this moment?"\n\f\t\t{Color.END}')
        sys.exit()

    def __str__(self):
        return f'++ {self.name}\n\f{self.desc} ++'