from room import Room

from player import Player

import textwrap

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
player = Player("Blair", room["outside"])

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


def compass(player, direction):
    attr = direction + '_to'

    if hasattr(player.room, attr):
        player.room = getattr(player.room, attr)
    else:
        print("You can't go that direction")


player = Player("Blair", room["outside"])


user_playing = True

while user_playing:
    print(player.room.name)
    for desc in textwrap.wrap(player.room.description, width=150):
        print(desc)

    user_input = input(
        "(N) North | (S) South | (E) East | (W) West | (Q) Quit\n")
    print(f"You chose the following direction: {user_input}")

    if user_input.lower() == 'n':
        compass(player, user_input)
    elif user_input.lower() == 's':
        compass(player, user_input)
    elif user_input.lower() == 'e':
        compass(player, user_input)
    elif user_input.lower() == 'w':
        compass(player, user_input)

    #     if player.room.connect is not None:
    #         player.move(user_input)
    #         print("You're now in ", player.room.name)

    # else:
    #     print("Please choose one of the following options: (N) North | (S) South | (E) East | (W) West | (Q) Quit")
