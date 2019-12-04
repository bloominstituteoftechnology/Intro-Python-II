import sys

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

player = Player(room['outside'])

# Functions
def move():
    # Get user input
    user_move = input("Which direction? (N, E, S, W):  ")
    user_move = user_move.lower()

    # Check if move is a valid direction
    valid_dirs = ["n", "e", "s", "w", "q"]
    if user_move not in valid_dirs:
        print("Sorry, that's not a valid direction. Please enter: 'N', 'E', 'S' or 'W'")
        move()
    else:
        # Quit if "q"
        if user_move=="q":
            print("Bye!")
            sys.exit(0)
        
        global player
        # Check if there's a room in each direction

        # North
        try:
            if user_move=="n":
                if player.room.n_to == "nothing":
                    print("Sorry, there's nothing there.")
                    move()
                else:
                    new_location = player.room.n_to
                    player = Player(new_location)
                    print(player.room)
                    move()

            # South
            if user_move=="s":
                if player.room.s_to == "nothing":
                    print("Sorry, there's nothing there.")
                    move()
                else:
                    new_location = player.room.s_to
                    player = Player(new_location)
                    print(player.room)
                    move()

            # East
            if user_move=="e":
                if player.room.e_to == "nothing":
                    print("Sorry, there's nothing there.")
                    move()
                else:
                    new_location = player.room.e_to
                    player = Player(new_location)
                    print(player.room)
                    move()

            # West
            if user_move=="w":
                if player.room.w_to == "nothing":
                    print("Sorry, there's nothing there.")
                    move()
                else:
                    new_location = player.room.w_to
                    player = Player(new_location)
                    print(player.room)
                    move()
        except AttributeError:
            print("Sorry, there's nothing there.")
            move()

    

#
# Main
#

def Main():
    print(player.room)
    move()

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

Main()