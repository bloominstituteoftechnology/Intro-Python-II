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

# Make a new player object that is currently in the 'outside' room.

player = Player(room["outside"])


def try_direction(direction, location):
    attribute = direction + "_to"

    if hasattr(location, attribute):

        return getattr(location, attribute)

    else:
        print(
            "\x1b[1;37;41m\n - You can't head in that direction - \x1b[0m" + "\n")
        return player.location

# Write a loop that:


while True:

    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    print(
        "\n " + f"Your Location: {player.location.title} \n \n     {player.location.description}")

    # * Waits for user input and decides what to do.
    inp = input(
        "\n Enter a direction or pick up an item from the current room > ").lower().split()
    # If the user enters a cardinal direction, attempt to move to the room there.

    if len(inp) == 1:

        inp = inp[0][0]

        if inp == "q":
            break

        player.location = try_direction(inp, player.location)

    elif len(inp) == 2:
        first_word = inp[0]
