from room import Room
from player import Player
import re

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
player = Player('Noob', room['outside'])

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


while True:
    print(player)
    advance = input(
        '''Please select direction that you would like to go in
        n - North
        e - East
        s - South
        w - West
        q - Quit
        ''')
    if advance.lower() == 'n' or advance.lower() == 'north':
        if player.current_room.n_to != None:
            player.current_room = player.current_room.n_to
        else:
            print('''
            ----------------------------------------------

            there is no available room to the north
            ----------------------------------------------
            ''')

    if advance.lower() == 'e' or advance.lower() == 'east':
        if player.current_room.e_to != None:
            player.current_room = player.current_room.e_to
        else:
            print('''
            ----------------------------------------------

            there is no available room to the east
            ----------------------------------------------
            ''')

    if advance.lower() == 's' or advance.lower() == 'south':
        if player.current_room.s_to != None:
            player.current_room = player.current_room.s_to
        else:
            print('''
            ----------------------------------------------

            there is no available room to the south
            ----------------------------------------------
            ''')

    if advance.lower() == 'w' or advance.lower() == 'west':
        if player.current_room.w_to != None:
            player.current_room = player.current_room.w_to
        else:
            print('''
            ----------------------------------------------

            there is no available room to the west
            ----------------------------------------------
            ''')

    if advance.lower() == 'q' or advance.lower() == 'quit':
        break

