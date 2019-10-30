import re
from room import Room
from player import Player

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

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
    print('\n')
    act = input('$ do what now: ')

    m = re.match(r"^go\s?([a-z]*)", act)
    if m != None:
        dir = m.group(1)
        if dir not in ['north','east','west','south']:
            print('\n')
            print(f'{dir} is not a recognized direction')
            continue
        else:
            move = dir[0] + '_to'
            x = getattr(player.loc, move)
            if x != None:
                player.loc = x
                print('\n')
                print(player.loc)
                continue
            else:
                print('\n')
                print(f'You cannot move {dir} from here')
                continue
    if act == 'help':
        print('\n')
        print('??? HELP ???')
        print('go (direction): ex. go north >> move in that direction')
        print('look: observe your current situation')
        print('q: quit')
        print('\n')
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
        print('\n')
        print(f'{act} command not recognized, type help to see a list of commands')
        continue
