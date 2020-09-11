from room import (Room, valid_directions)
from player import Player
from item import Item

#Items
sword = Item('sword', 'a sharp two-edged sword')
coins = Item('coins', 'a bag of gold coins')
torch = Item('torch', 'a bright torch')
cloak = Item('cloak', 'a warm cloak')
helmet = Item('helmet', 'a helmet made of damascus steel')

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [cloak]), 

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [sword]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [helmet]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [torch]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [coins]),

    'pool': Room("Pool", """You've found a pool, grab a drink and chill out""",[]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].e_to = room['pool']
room['pool'].w_to = room['outside']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Pete', room['outside'])

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

valid_commands = ('get', 'drop')

def is_direction(str):
    """
    returns true from string if it is a valid
    """
    return str in valid_directions

def is_command(str):
    #checks if command is valid
    split_str = str.split(" ")
    if split_str.__len__() == 2:
        return split_str[0] in valid_commands
    else:
        return str

print(f'Welcome {player.name}, press q at any time to quit')
print(f'You are currently {player.current_room.name}')
print(player.current_room.description)
current_room = player.current_room

while True:
    if current_room != player.current_room:
        print(player.current_room)
        current_room = player.current_room
    current_room = player.current_room
    print(f'Items in room: {current_room.show_items()}')
    user_input = input('Where would you like to go? n, e, s or w?: ')
    if user_input == 'q':
        break
    elif is_direction(user_input):
        player.move(user_input)
    elif is_command(user_input):
        player.do(user_input)
    else:
        print('Sorry that is not a valid command, please try again!')

