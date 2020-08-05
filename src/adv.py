from room import Room
from player import Player
from game_controller import GameController
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
room['outside'].s_to = None
room['outside'].e_to = None
room['outside'].w_to = None

room['foyer'].n_to = room['overlook']
room['foyer'].s_to = room['outside']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = None

room['overlook'].n_to = None
room['overlook'].s_to = room['foyer']
room['overlook'].e_to = None
room['overlook'].w_to = None

room['narrow'].n_to = room['treasure']
room['narrow'].s_to = None
room['narrow'].e_to = None
room['narrow'].w_to = room['foyer']

room['treasure'].n_to = None
room['treasure'].s_to = room['narrow']
room['treasure'].e_to = None
room['treasure'].w_to = None

#
# Main
#

items = []
done = False
current_room = room['outside']
game_controller = GameController()

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Chris', current_room)
# Write a loop that:
while not done:
    current_room.isLit = False
    if current_room == room['outside']:
        current_room.isLit = True
    else:
        current_room.isLit = player1.light_source_on

    print(f'\n{player1}')

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
    print(f'\n{current_room}')

# * Waits for user input and decides what to do.
    commands = input('> ').split(',')
    print(f'verified commands: {commands} ... adv.py line 82')
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    for command in commands:
            game_controller.roomOperation(current_room, player1, command)
        # elif command == 'n' or 'north':
            
        # elif command == 's':
        #     print('s pressed')
        # elif command == 'e':
        #     print('e pressed')
        # elif command == 'w':
        #     print('w pressed')