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
user_name = input("Join the fight against the Horde, enter your name: ")
player = Player(user_name, room['outside'])

print("player test:", player)

# REPL should accept 'r', 'p', 's' commands
# 'q' to quit

choices = ['n', 'e', 's', 'w']
# Write a loop that:
while True:

    cmd = input("choose your Path -> ")

    print(f"You Have Moved  {cmd} ")

    if cmd == 'n':
        if player.current_location.n_to != None:
            player.current_location = player.current_location.n_to
        else:
            print(f"The Horde is blocking your route North turn back.")
        # print(f"You Gentley Step North")
    elif cmd == 'e':
        if player.current_location.e_to != None:
            player.current_location = player.current_location.e_to
        else:
            print(f"The Horde is blocking your route East turn back.")
        # print(f"You Silently Slide East")
    elif cmd == 's':
        if player.current_location.s_to != None:
            player.current_location = player.current_location.s_to
        else:
            print(f"The Horde is blocking your route South turn back.")
        # print(f"You Cautiously Move South")
    elif cmd == 'w':
        if player.current_location.w_to != None:
            player.current_location = player.current_location.w_to
        else:
            print(f"The Horde is blocking your route West turn back.")
        # print(f"You Sneak to the West")
    elif cmd == 'q':
        print('Goodbye!')
        break
    else:
        print(f"invalid entry, n, e, s, w, q are only valid inputs")

    # * Prints the current room name

    print(
        f"you are currently situated in the {player.current_location.name}")

    # * Prints the current description (the textwrap module might be useful here).
    print(textwrap.wrap(player.current_location.description))

    # * Waits for user input and decides what to do.

    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
