from color import Color

def showHelp():
    print(f'{Color.RED}go{Color.END} [{Color.PURPLE}north, east, west, south{Color.END}] {Color.GREEN}$ Move in that direction (ex. go north){Color.END}')
    print(f'{Color.RED}get{Color.END} [{Color.RED}item{Color.END}] {Color.GREEN}$ Pick up an item you see (ex. get Rubber Duck){Color.END}')
    print(f'{Color.RED}drop{Color.END} [{Color.RED}item{Color.END}] {Color.GREEN}$ Drop an item you are holding (ex. drop Flashlight){Color.END}')
    print(f'{Color.RED}use{Color.END} [{Color.RED}item{Color.END}] {Color.GREEN}$ Use an item you are holding (ex. use Flashlight){Color.END}')
    print(f'{Color.RED}look{Color.END} {Color.GREEN}$ Observe your surroundings{Color.END}')
    print(f'{Color.RED}q{Color.END} {Color.GREEN}$ Quit{Color.END}')