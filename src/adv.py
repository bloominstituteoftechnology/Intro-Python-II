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
player = Player(room['outside'])

'''
direction is the direction the user input
current is the current room the player is in

returns the new room that the player moves to if the
move was successful, or returns the current room if the move was
not successful
'''


def try_direction(direction, current):
    attribute = direction + '_to'

    # See if the inputted direction is one that we can move to
    if hasattr(current, attribute):
        # fetch the new room
        return getattr(current, attribute)
    else:
        print("There is nothing in that direction")
        return current


# Write a loop that:
#
while True:
    # * Prints the current room name
    print(player.curr_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print(player.curr_room.desc)
    # * Waits for user input and decides what to do.
    s = input("\n>").lower().split()

    # check to see if the user input a one or two word command
    if len(s) == 1:
        # the user passed us a direction

        # grab the first character of the first word
        s = s[0][0]
        pass
        if s == 'q':
            print('Thank you for playing')
            break

        player.curr_room = try_direction(s, player.curr_room)
    elif len(s) == 2:
        # the user passed us a two-word command
        first_word = s[0]  # verb
        second_word = s[1]  # noun

        if first_word in ['get', 'drop']:
            break
    else:
        print("I don't understand that command")
        continue

    # none dynamic way
    # if s == 'n':
    #     player.curr_room = player.curr_room.n_to
    # elif s == 's':
    #     player.curr_room = player.curr_room.s_to
    # elif s == 'e':
    #     player.curr_room = player.curr_room.e_to
    # elif s == 'w':
    #     player.curr_room = player.curr_room.w_to
    # else:
    #     print("not a valid direction")

    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
