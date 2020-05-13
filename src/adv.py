import time
import sys
# from room import Room

# Declare all the rooms

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

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
intro = 'I was a young teen, in search to find a real demon!' + \
    ' I was told that this house was haunted by one!\n\n'
for char in intro:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.2)

name = input('\tWhat is your name, charmed one? \t')

for char in name:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.20

while True:

    direction=input(
        'What direction would you like to go: n(orth), s(outh), e(ast), w(est), q to quit!').lower()

    if direction == 'n:
        print('north')

    elif direction == 's':
        print('south')

    elif direction == 'e':
        print('east')

    elif direction == 'w':
        print('west')
