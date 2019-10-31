import re
import sys
import time
from color import Color
from crawlText import crawlText
from item import Item
from player import Player
from room import Room
from textwrap import wrap
from quitGame import quitGame

items = {
    'key': Item('Key', 'This Key is unusally large, and feels warm to the touch.'),

    'dogtoy': Item('Rubber Duck', 'It is bright yellow, dripping with dog slobber, and somewhat ripped apart.'),

    'flashlight': Item('Flashlight', 'MagLite Brand: A sturdy piece of metal filled with D cell batteries. You could light up a dark room or beat down a door with this american classic.', useRooms={'Gravel Pathway': 'You see a large dog, he starts to growl so you shine the flashlight directly into his eyes. The dog seems confused and runs away.', 'Front Lawn of the Mansion': f'You shine the light around the muddy holes in the lawn. A flash of yellow catches your eye. You {Color.PURPLE}look{Color.RED} again.{Color.END}'}),

    'napkinMap': Item('Napkin', 'It is some kind of map, hastily drawn on a used napkin.. is that red ink, or ketchup There are a few letters written in pencil, "wnwne"')
}

room = {
    'outside': Room("Outer Gate", f"To the {Color.PURPLE}north{Color.END} lies a long, unlit, gravel pathway lined with trees. The iron gate to the south is locked, and topped with several layers of razor wire. Somebody is serious about home security.", holding=[items['key'],items['flashlight']]),

    'gravel': Room("Gravel Pathway", f"It is [{Color.RED}dark{Color.END}]. Lawns stretch out to either side, but you cannot see much of anything past the large oak trees lining the pathway. To the {Color.PURPLE}north{Color.END} you can see the shape of a building. As you walk further down the noisy gravel path the shape comes into focus, a decrepit looking white mansion in the colonial style. You can hear something rustling around nearby."),

    'frontLawn': Room("Front Lawn of the Mansion", f"{Color.PURPLE}North{Color.END} of you, the door to the mansion is wide open.  What happened here? It is [{Color.RED}dark{Color.END}], but you can see several large holes dug into the lawn. You can hear something rustling around nearby."),
    
    'foyer': Room("Foyer", f"This room is mostly empty space surrounding a grand staircase, a few steps are missing but you could climb {Color.PURPLE}up{Color.END}. Dusty passages run {Color.PURPLE}east{Color.END} and {Color.PURPLE}west{Color.END}. "),

    'ballroom': Room("Grand Ballroom", f"You admire the polished hardwood floors. One of the chandeliers has fallen and radiates crystal shrapnel from the far end of the room. The only exit is {Color.PURPLE}down{Color.END}."),

    'library': Room("Library", f"You stand among thousands of years of collected thoughts. Bookshelves line every wall, and the carpeted floor is barely visible beneath piles of mangled books. Someone has recently searched this room. The only exit is {Color.PURPLE}east{Color.END}."),

    'narrow': Room("Narrow Passage", f"The narrow passage bends here from {Color.PURPLE}west{Color.END} to {Color.PURPLE}north{Color.END}. The smell of lavender permeates the air."),

    'treasure': Room("Treasure Chamber", f"You see a large door, engraved with mysterious symbols. It seems to be made from solid gold, and feels warm to the touch. There is a large [{Color.RED}keyhole{Color.END}] in the center. The only exit is to the {Color.PURPLE}south{Color.END}."),
}

# Link rooms together
room['outside'].n_to = room['gravel']
room['gravel'].s_to = room['outside']

room['gravel'].s_to = room['outside']
room['gravel'].n_to = room['frontLawn']

room['frontLawn'].s_to = room['gravel']
room['frontLawn'].n_to = room['foyer']

room['foyer'].s_to = room['frontLawn']
room['foyer'].u_to = room['ballroom']
room['ballroom'].d_to = room['foyer']

room['foyer'].w_to = room['library']
room['library'].e_to = room['foyer']

room['foyer'].e_to = room['narrow']
room['narrow'].w_to = room['foyer']

room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# GAMEPLAY & DISPLAY FUNCTIONS
def showHelp():
    print(f'{Color.RED}go{Color.END} [{Color.PURPLE}north, east, west, south{Color.END}] {Color.GREEN}$ Move in that direction (ex. go north){Color.END}')
    print(f'{Color.RED}get{Color.END} [{Color.RED}item{Color.END}] {Color.GREEN}$ Pick up an item you see (ex. get Rubber Duck){Color.END}')
    print(f'{Color.RED}drop{Color.END} [{Color.RED}item{Color.END}] {Color.GREEN}$ Drop an item you are holding (ex. drop Flashlight){Color.END}')
    print(f'{Color.RED}use{Color.END} [{Color.RED}item{Color.END}] {Color.GREEN}$ Use an item you are holding (ex. use Flashlight){Color.END}')
    print(f'{Color.RED}look{Color.END} {Color.GREEN}$ Observe your surroundings{Color.END}')
    print(f'{Color.RED}q{Color.END} {Color.GREEN}$ Quit{Color.END}')
    
def handleGoDir(dir):
    if dir not in ['north','east','west','south','up','down']:
        print(f'{Color.PURPLE}{dir}{Color.RED} is not an option{Color.END}')
    else:
        moveTo = dir[0] + '_to'
        newRoom = getattr(player.loc, moveTo)
        if newRoom != None:
            player.loc = newRoom
            if player.loc.seen == False: 
                player.loc.seen = True
                print('\n')
                crawlText(f'{Color.PURPLE}{player.loc.name}{Color.END}',0.03)
                crawlText(player.loc.desc,0.02)
            else:
                print('\n')
                crawlText(f'{Color.PURPLE}You have been here before{Color.END}',0.03)
                print(player.loc)
        else:
            print(f'{Color.RED}You cannot go {Color.PURPLE}{dir}{Color.RED} from here{Color.END}')

def handleDropItem(thisItem):
    index = None
    for i, item in enumerate(player.holding):
        if item.name.lower() == thisItem.lower():
            index = i
    if index != None:
        thisItem = player.holding.pop(index)
        player.loc.holding.append(thisItem)
        crawlText(f'You dropped the {Color.RED}{thisItem.name}{Color.END}')
    else:
        print(f'You cannot see a {Color.RED}{thisItem}{Color.END}')

def handleUseItem(thisItem):
    index = None
    for i, item in enumerate(player.holding):
        if item.name.lower() == thisItem.lower():
            index = i
    if index != None:
        thisItem = player.holding[index]
        thisHappened = thisItem.useItem(room=player.loc.name)
        print('\n')
        crawlText(f'{Color.RED}{thisHappened}{Color.END}')
        if thisItem.name == 'Flashlight' and player.loc.name == 'Front Lawn of the Mansion':
            player.loc.holding = [items['dogtoy']]
    else:
        print(f'You are not holding {Color.RED}{thisItem}{Color.END}')

def startNewGame(name):
    # DRAMATIC INTRO
    # INIT PLAYER and GET flashlight
    print('\n')
    intro = f'You awaken suddenly. Your body is aching and your clothes are stained with mud. You {Color.PURPLE}look{Color.END} around to see a locked iron gate behind you, and a gravel pathway before you. How did you get here? You touch your head and feel a lump, it is wet, and sticky. You can see a {Color.RED}Flashlight{Color.END} on the gravel nearby. It\'s YOUR flashlight.'
    # crawlText(intro, delay=0.03)
    player.loc.getItem('flashlight', player)
    # crawlText(f'{Color.PURPLE}It is wet with blood. Did someone knock you out with your own flashlight?{Color.END}', 0.02)
    # crawlText(f'{Color.PURPLE}You can see your name engraved on the handle: {Color.RED}{player.name.upper()}{Color.END}', 0.02)
    crawlText(player.loc.desc, 0.02)

# START GAME
player = Player('Ricky', room['outside'])
startNewGame(player.name)
# GAMEPLAY LOOP
while True:
    player.loc.seen = True
    location = player.loc.name
    print(f'You are at the {Color.PURPLE}{location}{Color.END}')
    youSee = player.loc.showItems()
    print(youSee)
    myItems = player.showItems()
    print(myItems)
    act = input(f'{Color.GREEN}$ action: {Color.END}')

    DropItem = re.match(r"^drop\s([a-z]*\s?[a-z]*)", act, flags=re.I)
    if DropItem != None:
        thisItem = DropItem.group(1)
        handleDropItem(thisItem)
        continue

    useItem = re.match(r"^use\s([a-z]*\s?[a-z]*)", act, flags=re.I)
    if useItem != None:
        thisItem = useItem.group(1)
        handleUseItem(thisItem)
        continue

    getItem = re.match(r"^get\s([a-z]*\s?[a-z]*)", act, flags=re.I)
    if getItem != None:
        thisItem = getItem.group(1)
        player.loc.getItem(thisItem, player)
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
        print('\n')
        continue
