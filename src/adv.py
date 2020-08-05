from room import Room
from player import Player
import argparse
import sys

# Argument Parser

# explore_parser = argparse.ArgumentParser()
# explore_parser.add_argument("n", "--north", help="Moves player north")
# explore_parser.add_argument("w", "--west", help="Moves player west")
# explore_parser.add_argument("s", "--south", help="Moves player south")
# explore_parser.add_argument("e", "--east", help="Moves player east")
# explore_parser.add_argument("q", "--quit", help="Quits the game")

# args = explore_parser.parse_args()

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

directions = ['n', 's', 'e', 'w']
done = False

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Chris', room["outside"])
# Write a loop that:
while not done:
# * Prints the current room name
    print(f'\n{player1.current_room}')
# * Prints the current description (the textwrap module might be useful here).
    print(f'\ntest room')
# * Waits for user input and decides what to do.
    commands = input('> ').split(',')
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    for command in commands:
# If the user enters "q", quit the game.
        if command == 'q':
            sys.exit(1)
        elif command == 'n':
            print('n pressed')
            #check if the player can move to the north
            # if there is, set that room to the player's location
        elif command == 's':
            print('s pressed')
        elif command == 'e':
            print('e pressed')
        elif command == 'w':
            print('w pressed')