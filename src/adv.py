from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you,
falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from
west to north. The smell of gold permeates the air."""),

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

player = Player('Nate', room['outside'])

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


def update_room(user_input):
    if user_input == 'n':
        if player.current_room.n_to is None:
            print('\nTHERE IS NO ROOM IN THAT DIRECTION!\nYou are still in...')
            return player.current_room
        else:
            return player.current_room.n_to
    if user_input == 's':
        if player.current_room.s_to is None:
            print('\nTHERE IS NO ROOM IN THAT DIRECTION!\nYou are still in...')
            return player.current_room
        else:
            return player.current_room.s_to
    if user_input == 'e':
        if player.current_room.e_to is None:
            print('\nTHERE IS NO ROOM IN THAT DIRECTION!\nYou are still in...')
            return player.current_room
        else:
            return player.current_room.e_to
    if user_input == 'w':
        if player.current_room.w_to is None:
            print('\nTHERE IS NO ROOM IN THAT DIRECTION!\nYou are still in...')
            return player.current_room
        else:
            return player.current_room.w_to
    elif user_input != 'q':
        print('\nNOT A CARDINAL DIRECTION!\nYou are still in...')
        return player.current_room


user_input = None
while user_input != 'q':
    print('\n' + player.current_room.name +
          '\n' + textwrap.fill(player.current_room.description, 50))
    user_input = input(
        "\nEnter a cardinal direction (n, s, e, w), or q to quit.\n")
    player.current_room = update_room(user_input)
