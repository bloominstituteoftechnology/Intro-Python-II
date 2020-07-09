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


#
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])
possible_directions = ['n', 's', 'e', 'w']

# Write a loop that:
while True:

    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    print(f"{player.location}\n")

    # when input comes in, strip off whitespace, lowercase the input, and split it
    command = input("What would you like to do? ").strip().lower().split()[0]
    command = command[0]
    if command != ['n', 's', 's', 'w']:
        print("The given direction is not valid!")
        print()
    if command == 'q':
        break


    if command in possible_directions:
        # check to see if we can go in that direction
        # if we can, go there
        player.try_direction(command)

    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
