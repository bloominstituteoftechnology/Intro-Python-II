import re
import sys
import time
from color import Color
from item import Item
from player import Player
from room import Room
from textwrap import wrap

items = {
    'key': Item('Key', 'This Key is unusally large, and feels warm to the touch.'),

    'dogtoy': Item('Rubber Duck', 'It is covered in slobber, and somewhat ripped apart.'),

    'flashlight': Item('Flashlight', 'MagLite Brand: A sturdy piece of metal filled with D cell batteries. You could light up a dark room or beat down a door with this american classic.', useRooms={'Gravel Pathway': 'You see a large dog, he starts to growl so you shine the flashlight directly into his eyes. The dog seems confused and runs away.', 'Front Lawn of the Mansion': f'You shine the light around the muddy holes in the lawn. A flash of yellow catches your eye. You {Color.PURPLE}look{Color.RED} again.{Color.END}'}),

    'napkinMap': Item('Napkin', 'It is some kind of map, hastily drawn on a used napkin.. is that red ink, or ketchup There are a few letters written in pencil, "wnwne"')
}

room = {
    'outside': Room("Outer Gate", f"To the {Color.GREEN}north{Color.END} lies a long, unlit, gravel pathway that leads to the main house. The iron gate behind you is locked, and topped with several layers of razor wire. Somebody is serious about home security.", holding=[items['key'],items['flashlight']]),

    'gravel': Room("Gravel Pathway", f"It is [{Color.RED}dark{Color.END}], and lawns seem stretch out to either side. To the {Color.GREEN}north{Color.END} you can see the main house, a large white mansion in the colonial style. You can hear something rustling around quietly."),

    'frontLawn': Room("Front Lawn of the Mansion", f"{Color.GREEN}North{Color.END} of you, the door to the mansion is wide open.  Something happened here, there are several large holes dug into the lawn. It is [{Color.RED}dark{Color.END}]. You can hear something rustling around quietly."),
    
    'foyer': Room("Foyer", f"Dim light filters in from the south. Dusty passages run {Color.GREEN}east{Color.END} and {Color.GREEN}west{Color.END}, a grand staircase leads {Color.GREEN}north{Color.END}. "),

    'ballroom': Room("Grand Ballroom", f"You admire the polished hardwood floors. One of the chandeliers has fallen and radiates crystal shrapnel from the far end of the room. The only exit is {Color.GREEN}south{Color.END}."),

    'library': Room("Library", f"You stand among thousands of years of collected thoughts. Bookshelves line every wall, and the carpeted floor is barely visible beneath piles of mangled books. Someone has recently searched this room. The only exit is {Color.GREEN}east{Color.END}."),

    'narrow': Room("Narrow Passage", f"The narrow passage bends here from {Color.GREEN}west{Color.END} to {Color.GREEN}north{Color.END}. The smell of lavender permeates the air."),

    'treasure': Room("Treasure Chamber", f"You see a large door, engraved with mysterious symbols. It seems to be made from solid gold, and feels warm to the touch. There is a large [{Color.RED}keyhole{Color.END}] in the center. The only exit is to the {Color.GREEN}south{Color.END}."),
}

# Link rooms together
room['outside'].n_to = room['gravel']
room['gravel'].s_to = room['outside']

room['gravel'].s_to = room['outside']
room['gravel'].n_to = room['frontLawn']

room['frontLawn'].s_to = room['gravel']
room['frontLawn'].n_to = room['foyer']

room['foyer'].s_to = room['frontLawn']
room['foyer'].n_to = room['ballroom']
room['ballroom'].s_to = room['foyer']

room['foyer'].w_to = room['library']
room['library'].e_to = room['foyer']

room['foyer'].e_to = room['narrow']
room['narrow'].w_to = room['foyer']

room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# GAMEPLAY & DISPLAY FUNCTIONS
def showHelp():
    print(f'{Color.RED}go{Color.END} [{Color.PURPLE}north, east, west, south{Color.END}] $ Move in that direction (ex. go north)')
    print(f'{Color.RED}get{Color.END} [{Color.PURPLE}item{Color.END}] $ Pick up an item you see (ex. get Rubber Duck)')
    print(f'{Color.RED}use{Color.END} [{Color.PURPLE}item{Color.END}] $ Use an item you are holding (ex. use Flashlight)')
    print(f'{Color.RED}look{Color.END} $ Observe your surroundings')
    print(f'{Color.RED}q{Color.END} $ Quit\n')
    
def crawlText(text, delay=0.01):
    text = wrap(text, 50)
    text = '\n\r'.join(text)
    for ln in text:
        sys.stdout.write(ln)
        sys.stdout.flush()
        time.sleep(delay)
    print('\n')

def quitGame():
    quitMsg = f'{Color.RED}Your mind feels electric, the taste of copper fills your mouth, and you wonder:{Color.PURPLE} "Is this real? Am I dreaming this moment?"\n\f\t\t{Color.END}'
    crawlText(quitMsg)
    sys.exit('x')

def handleGoDir(dir):
    if dir not in ['north','east','west','south']:
        print(f'\t{dir} is not a recognized direction')
    else:
        moveTo = dir[0] + '_to'
        newRoom = getattr(player.loc, moveTo)
        if newRoom != None:
            player.loc = newRoom
            print('\n')
            print(player.loc)
        else:
            print(f'\t{Color.RED}You cannot go {dir} from here{Color.END}')

def handleGetItem(getItem):
    index = -1
    for i, item in enumerate(player.loc.holding):
        if item.name == getItem:
            index = i
    if index != -1:
        thisItem = player.loc.holding.pop(index)
        player.holding.append(thisItem)
        print(f'You pick up the {thisItem}')
        if thisItem.name == 'Rubber Duck':
            youDied = f'{Color.RED}You hear a faint growl growing louder, as you turn you can see death in the eye of the beast. A sharp bark is the last thing you hear before you fall to the ground, the weight of a giant dog pressing you into the mud. The pain is terrible, and you faintly remember two words from a past life: King Corso.{Color.END}'
            crawlText(youDied, 0.03)
            print('\n')
            quitGame()
    else:
        print(f'\t{Color.RED}{getItem} not found (Case Sensitive){Color.END}')

def handleUseItem(thisItem):
    index = -1
    for i, item in enumerate(player.holding):
        if item.name == thisItem:
            index = i
    if index != -1:
        thisItem = player.holding[index]
        thisHappened = thisItem.useItem(room=player.loc.name)
        thisHappened = f'{Color.RED}{thisHappened}{Color.END}'
        crawlText(thisHappened)
        if thisItem.name == 'Flashlight' and player.loc.name == 'Front Lawn of the Mansion':
            player.loc.holding = [items['dogtoy']]
            youSee = player.loc.printItems()
            print(f'{youSee}')
    else:
        print(f'\t{thisItem} {Color.RED}not found (Case Sensitive){Color.END}')

# DRAMATIC INTRO
print('\n')
intro = f'You awaken suddenly, your head is aching and your clothes are stained with mud. You {Color.RED}look{Color.END} around to see a locked iron gate behind you, and a gravel pathway before you. How did you get here? Why does this all seem so familiar?'
crawlText(intro, delay=0.05)

# INIT PLAYER and PRINT CURRENT LOCATION
# player = Player('steve', room['frontLawn'], holding=[items['flashlight']])
player = Player('steve', room['outside'])
print('\n')
print(player.loc)

# START GAME LOOP
while True:
    myItems = player.myItems()
    print(myItems)
    act = input('$ do what now: ')

    useItem = re.match(r"^use\s([A-Z][a-z]*\s?[A-Z]*[a-z]*)", act)
    if useItem != None:
        thisItem = useItem.group(1)
        handleUseItem(thisItem)
        continue

    getItem = re.match(r"^get\s([A-Z][a-z]*\s?[A-Z]*[a-z]*)", act)
    if getItem != None:
        getItem = getItem.group(1)
        handleGetItem(getItem)
        continue

    goDir = re.match(r"^go\s([a-z]*)", act, flags=re.I)
    if goDir != None:
        dir = goDir.group(1).lower()
        handleGoDir(dir)
        continue

    if act == 'help':
        showHelp()
        continue
    if act == 'look':
        print(player.loc)
        continue
    if act == 'q':
        quitGame()
        break
    else:
        print('\n')
        print(f'{act} {Color.RED}command not recognized{Color.END}\ntype {Color.PURPLE}help{Color.END} to see a list of commands')
        continue
