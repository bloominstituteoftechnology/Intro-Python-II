from exceptions import MoveError
from room import Room
from player import Player
import textwrap

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

wrapper = textwrap.TextWrapper(width=70)

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Establish items in rooms
room['foyer'].items = ['Bronze Sword', 'Giraffe Statuette']

#
# Main
#

# Helper method to check whether a player can enter a new room
def verify_move(current_room, move_dir):
    if(current_room.__dict__['{}_to'.format(move_dir)] is None):
        raise MoveError(current_room, move_dir)

# Helper function to check current room's items and return a string 
# which can be printed based on what it finds
def check_items(current_room):
    items = current_room.items
    if(items is None):
        return 'No items in this room'
    else:
        return ', '.join(items)

# Make a new player object that is currently in the 'outside' room.
player_name = input('Enter a name for your character: ')
p1 = Player(player_name, room['outside'])

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
while(True):
    # Determine current room
    c_room = p1.current_room

    # Print Buffer space to make it easier to read
    print('')
    print('-'*70)

    # Print current Location and location description/items
    print('Current Room: {}'.format(c_room.name))
    [print(line) for line in wrapper.wrap(text=c_room.description)]
    item_str = 'Items in room:\t{}'.format(check_items(c_room))
    [print(line) for line in wrapper.wrap(text=item_str)]

    # Input from user
    inp = input('What would you like to do? ')

    # Print buffer to make it easier to read
    print('-'*70)

    # Process Input
    if(inp == 'q'):
        break
    elif(inp in ['n','e','s','w']):
        try:
            verify_move(c_room, inp)
            p1.current_room = c_room.__dict__['{}_to'.format(inp)]
        except MoveError as e:
            print('You cannot move in that direction!')
    else:
        print('Invalid Input')