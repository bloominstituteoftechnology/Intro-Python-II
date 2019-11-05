import re
import sys
import time
from color import Color
from item import Item
from player import Player
from room import Room
from textwrap import wrap

items = {
    'key': Item('Key', 'This Key is unusally large, and feels warm to the touch.', useRooms={'Treasure Chamber': f'You hesitate for a moment, contemplating the strange engravings on this golden door. You feel the warmth of the key in your hand as it turns with a satisfying {Color.PURPLE}*CLIK*{Color.END}'}),

    'dogtoy': Item('Rubber Duck', 'It is bright yellow, dripping with dog slobber, and somewhat ripped apart.'),

    'flashlight': Item('Flashlight', 'MagLite Brand. A sturdy piece of metal filled with D cell batteries.', useRooms={'Gravel Pathway': 'You can see a large dog moving beyond the trees. You shine the flashlight directly into his eyes, and he stops for a moment. Suddenly, he lets out a short bark and runs away.', 'Front Lawn of the Mansion': f'You shine the light around the muddy holes in the lawn. A flash of yellow catches your eye. It looks like some kind of dog toy.'}),

    'napkinMap': Item('Napkin', f'It is a map, hastily drawn on a used napkin. You don\'t recognize the symbols, but there are a few letters written in pencil: {Color.RED}W N W N E{Color.END}')
}

room = {
    'outside': Room("Outer Gate", f"To the {Color.PURPLE}north{Color.END} lies a long, unlit, gravel pathway lined with trees. The iron gate to the south is locked, and topped with several layers of razor wire. Somebody is serious about home security.", holding=[items['flashlight']]),

    'gravel': Room("Gravel Pathway", f"Lawns stretch out to either side, but you cannot see much of anything past the large oak trees lining the pathway. To the {Color.PURPLE}north{Color.END} you can see the shape of a building. As you walk further down the noisy gravel path the shape comes into focus, a decrepit looking white mansion in the colonial style. You can hear something rustling around nearby.", isDark=True),

    'frontLawn': Room("Front Lawn of the Mansion", f"{Color.PURPLE}North{Color.END} of you, the door to the mansion is wide open.  What happened here? It is {Color.RED}dark{Color.END}, but you can see several large holes dug into the lawn. You can hear something rustling around nearby.", holding=[items['dogtoy']], isDark=True),
    
    'foyer': Room("Foyer", f"This room is mostly empty space surrounding a grand staircase, a few steps are missing but you could climb {Color.PURPLE}up{Color.END}. Dusty passages run {Color.PURPLE}east{Color.END} and {Color.PURPLE}west{Color.END}. "),

    'ballroom': Room("Grand Ballroom", f"You admire the polished hardwood floors. One of the chandeliers has fallen and radiates crystal shrapnel from the far end of the room. The only exit is {Color.PURPLE}down{Color.END} the staircase.", holding=[items['napkinMap']] ),

    'library': Room("Library", f"You stand among thousands of years of collected thoughts. Bookshelves line every wall but they are all emptied. Someone has recently searched this room. Books and furniture lay tossed about in various piles. The only exit is {Color.PURPLE}east{Color.END}."),

    'narrow': Room("Narrow Passage", f"The narrow passage bends here from {Color.PURPLE}west{Color.END} to {Color.PURPLE}north{Color.END}. The smell of lavender permeates the air."),

    'treasure': Room("Treasure Chamber", f"You see a large door, engraved with mysterious symbols. It seems to be made from solid gold, and feels warm to the touch. There is a large [{Color.RED}keyhole{Color.END}] in the center. The only exit is to the {Color.PURPLE}south{Color.END}.", holding=[items['key']]),
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

# START GAME
player = Player('Ricky', room['outside'])
player.startGame()

# GAMEPLAY LOOP
while True:
    player.loc.seen = True
    location = player.loc.name
    print(f'You are at the {Color.PURPLE}{location}{Color.END}')
    
    youSee = player.loc.showItems()
    if youSee != None:
        print(f'You can see {Color.RED}{youSee}{Color.END}')
    elif player.loc.isDark:
        print(f'It is {Color.RED}[dark]{Color.END}')

    myItems = player.showItems()
    if myItems != None:
        print(f'You are holding {Color.RED}{myItems}{Color.END}')
    action = input(f'{Color.GREEN}$ action: {Color.END}')

    dropItem = re.match(r"^drop\s([a-z]*\s?[a-z]*)", action, flags=re.I)
    if dropItem != None:
        thisItem = dropItem.group(1)
        player.drop(thisItem)
        continue

    useItem = re.match(r"^use\s([a-z]*\s?[a-z]*)", action, flags=re.I)
    if useItem != None:
        thisItem = useItem.group(1)
        player.use(thisItem)
        continue

    getItem = re.match(r"^get\s([a-z]*\s?[a-z]*)", action, flags=re.I)
    if getItem != None:
        thisItem = getItem.group(1)
        player.loc.getItem(thisItem, player)
        continue

    goTo = re.match(r"^go\s([a-z]*)", action, flags=re.I)
    if goTo != None:
        there = goTo.group(1).lower()
        player.go(there)
        continue

    if action == 'help':
        player.showHelp()
        continue
    if action == 'look':
        print('\n')
        print(player.loc)
        continue
    if action == 'q':
        player.quitGame()
        break
    else:
        print('\n')
        print(f'{action} {Color.RED}action not recognized{Color.END}\ntype {Color.PURPLE}help{Color.END} to see a list of actions')
        print('\n')
        continue
