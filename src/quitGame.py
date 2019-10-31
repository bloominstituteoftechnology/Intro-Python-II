import sys
from color import Color
from crawlText import crawlText

def quitGame():
    print('\n')
    crawlText(f'{Color.RED}Your mind feels electric, the taste of copper fills your mouth, and you wonder:')
    crawlText(f'{Color.PURPLE} "Is this real? Am I dreaming this moment?"\n\f\t\t{Color.END}')
    sys.exit()