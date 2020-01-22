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
player = Player("Me", room['outside'])

# Write a loop that:
#
while True:
    current_room = player.current_room
    # * Prints the current room name
    print(f"Your current location --> {current_room.area}")
    # * Prints the current description (the textwrap module might be useful here).
    print(f"*** {current_room.description} ***")
    # * Waits for user input and decides what to do.
    move = input("Make a move > ")
    if move == "n":
        if current_room.n_to is not None:
            player.current_room = current_room.n_to
        else:
            print("YOU MAY NOT ENTER! Try a different move.")
    elif move == "s":
        if current_room.s_to is not None:
            player.current_room = current_room.s_to
        else:
            print("YOU MAY NOT ENTER! Try a different move.")
    elif move == "e":
        if current_room.e_to is not None:
            player.current_room = current_room.e_to
        else:
            print("YOU MAY NOT ENTER! Try a different move.")
    elif move == "w":
        if current_room.w_to is not None:
            player.current_room = current_room.w_to
        else:
            print("YOU MAY NOT ENTER! Try a different move.")
        # If the user enters "q", quit the game.
    elif move == "q":
        print("Thank you for playing! Farewell!")
        exit()
    else:
        # Print an error message if the movement isn't allowed.
        print("Not a valid move. Please enter: n, s, e, w or q")
        # If the user enters a cardinal direction, attempt to move to the room there.
