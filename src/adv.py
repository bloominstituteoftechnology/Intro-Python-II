from room import Room
from player import Player
import sys

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_1 = room['outside']

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

print(f'Hello, stranger. You are currently in the {player_1.room_name}. {player_1.room_description}.\n')

output = ('Choose a direction to travel in order to find the treasure.', 
f'But beware, there are many wrong paths to take:\n'
'[n] North  [s] South  [e] East  [w] West  [q] Quit\n')
direction = input('\n'.join(output))

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
if not direction == 'q': 
    if direction == 'n':
        player_1 = player_1.n_to
        print(f'You are now in the {player_1.room_name}. \n{player_1.room_description}.')
        direction = input('\n'.join(output))
    else: 
        error_message = ("Wow, you walked right into a wall.",
        f'You are still in the {player_1.room_name}. {player_1.room_description}.')
        print('\n'.join(error_message))
        direction = input('\n'.join(output))
else:
    print("Bye, then.")
    sys.exit()
        
# If the user enters "q", quit the game.