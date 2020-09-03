import sys
from room import Room
from player import Player

# Declare all the rooms
 
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons..."),

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


######FORMATING#######
def spacing():
    print('\n', end=' ')
def divider():
    print('------------------------------------------------')
######################


#game intro
spacing()

print('Welcome!', end=' ')
playername = input('Please enter a name: ')

player = Player(playername, room['outside'])

spacing()

print(f'Hello {player.name}, are you ready for an adveture?')

spacing()

#game loop
while True:
    ##prints current location and description, prompts user for directions##
    divider()
    spacing()
    print(player)
    spacing()
    direction = input('Which way? ').lower()
    spacing()
    ########################################################################
    if len(direction) == 1:
        #quits loops with 'q'
        if direction[0] == 'q':
            sys.exit()
        #sets direction reseting loop
        elif direction[0] in ('n','s','e','w'):
            player.travel(direction[0])
        #corrects player resets loop
        else:
            print('That is not an option, try q to QUIT or n, s, e, or w to move around :)')
            spacing()
