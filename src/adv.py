import re
from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside': Room("Outer Gate", "North of you, a long, unlit gravel pathway leads to the main house. The gate behind you is locked, and topped with several layers of razor wire. Somebody is serious about home security."),

    'gravel': Room("Gravel Pathway", "It is [dark], and lawns seem stretch out to either side. To the north you can see the main house, a large white mansion in the colonial style. You can hear something rustling around quietly."),

    'frontLawn': Room("Front Lawn of the Mansion", "North of you, the door to the mansion is wide open.  Something happened here, there are several large holes dug into the lawn. It is [dark]. You can hear something rustling around quietly."),
    
    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run east and west, a grand staircase leads north. "),

    'ballroom': Room("Grand Ballroom", "You admire the polished hardwood floors. One of the chandeliers has fallen and radiates crystal shrapnel from the far end of the room. The only exit is south."),

    'library': Room("Library", "You stand among thousands of years of collected thoughts. Bookshelves line every wall, and the floor is barely beneath piles of mangled books. Someone has recently searched this room, violently. The only exit is east."),

    'narrow': Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of lavender permeates the air."),

    'treasure': Room("Treasure Chamber", "You see a large door, engraved with mysterious symbols. It seems to be made from solid gold, and feels warm to the touch. There is a large [keyhole] in the center. The only exit is to the south."),
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

items = {
    'key': Item('Large Key', 'This Key is unusally large, and feels warm to the touch.'),
    'dogtoy': Item('Rubber Duck', 'It is covered in slobber, and somewhat ripped apart.'),
    'flashlight': Item('MagLite Brand Flashlight', 'A sturdy piece of metal filled with D cell batteries.\nYou could light up a dark room or beat down a door with this american classic.'),
    'map': Item('Hastily Drawn Map', 'It is drawn on a used napkin, is that red ink, or ketchup?\nThere are a few letters written in pencil, "wnwne"')
}

# Make a new player object that is currently in the 'outside' room.
player = Player('steve', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print('\n')
print(player.loc)
while True:
    act = input('$ do what now: ')

    goDir = re.match(r"^go\s?([a-z]*)", act)
    if goDir != None:
        dir = goDir.group(1)
        if dir not in ['north','east','west','south']:
            print(f'\t{dir} is not a recognized direction')
            continue
        else:
            moveTo = dir[0] + '_to'
            newRoom = getattr(player.loc, moveTo)
            if newRoom != None:
                player.loc = newRoom
                print('\n')
                print(player.loc)
                continue
            else:
                print(f'\tYou cannot go {dir} from here')
                continue
    if act == 'help':
        print('*** list of commands ***\n')
        print('go [north, east, west, south]\n>> Move in that direction (ex. go north)\n')
        print('look\n>> Observe your surroundings\n')
        print('q\n>> Quit\n\f')
        continue
    if act == 'look':
        print('\n')
        print(player.loc)
        continue
    if act == 'q':
        print('\n')
        print(' Your mind feels electric, ')
        print(' the taste of copper fills your mouth, ')
        print(' and you wonder: ')
        print(' "Is this real? Am I dreaming this moment?" ')
        break
    else:
        print('\f')
        print(f'{act} command not recognized, type help to see a list of commands')
        continue
