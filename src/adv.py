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
# Main
#
def try_direction(player, direction):

    attribute = direction + '_to'

    # python has a handy method called hasattr
    # which allows us to check if a class has an attribute
    if hasattr(player.location, attribute):
        # this is valid direction
        # use getattr to fetch the value associated with 
        player.location = getattr(player.location)
    else:
        print("There's nothing in that direction")
# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside '])
# Write a loop that:
while True:
    print(player.location)

    command = input("\nCommand: ").strip().lower().split()
    print(command)
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
if command == 'quit':
    print('you have quit the game')

first_comm = command[0]
first_char = first_comm[0]

if first_char == 'n':
    #move to the north
    try_direction(player, command)

elif first_char == 's':
    try_direction(player, command)
    #move to the south 
elif first_char == 'e':
    try_direction(player, command)
    #move to the east 
elif first_char == 'w':
    try_direction(player, command)
