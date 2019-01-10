import sys
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

# Main
#
def movement(direction, current_room):
    attr = direction + '_to'

    if hasattr(current_room, attr):
        return getattr(current_room, attr)

def adv_game():
# Make a new player object that is currently in the 'outside' room.
    # get the player name from the sys arguments
    player_one = Player(sys.argv[1], room['outside'])
        
    # welcome message
    print(f'Welcome {player_one.name.capitalize()}')

# Write a loop that:
    while True:
    # * Prints the current room name
        print(f'\nYou are currently standing at the {player_one.room.area}')
    # * Prints the current description (the textwrap module might be useful here).
        print(f'{player_one.room.description}')
    # * Waits for user input and decides what to do.
        userS = input('\nWhat would you like to do?>>> ')
        
        player_one.room = movement(userS, player_one.room)
        if userS == '9':
            break

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
if len(sys.argv) != 2:
    print('usage: python adv.py [player name (no spaces)]')
else:
    adv_game()
