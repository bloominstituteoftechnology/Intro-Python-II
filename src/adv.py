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

player = Player('Max',room['outside'])

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

while True:
    current_room = player.current_room
    print(f"Your location: {current_room.name_of_room}")
    print(f"{current_room.description}")
    move = input("Enter your next move (n, s, e, w, or q for quit): ")

    # A four-channel if tree (cardinal directions), with a fifth option out ("q")
    if move == "n":
        if current_room.n_to is not None:
            player.current_room = current_room.n_to
            print("You chose north!")
        else:
            print("\nThere is no room that way! Try again.")
    elif move == "s":
        if current_room.s_to is not None:
            player.current_room = current_room.s_to
            print("You chose south!")
        else:
            print("\nThere is no room that way! Try again.")
    elif move == "e":
        if current_room.e_to is not None:
            player.current_room = current_room.e_to
            print("You chose east!")
        else:
            print("\nThere is no room that way! Try again.")
    elif move == "w":
        if current_room.w_to is not None:
            player.current_room = current_room.w_to
            print("You chose west!")
        else:
            print("\nThere is no room that way! Try again.")
        # Quitting the game
    elif move == "q":
        print("Thank you for playing! Farewell!")
        exit()
    else:
        # Error message
        print("Please enter: n, s, e, w or q")
