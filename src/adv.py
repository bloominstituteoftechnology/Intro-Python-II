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
player = Player('Pete', room['outside'])
# room1 = Room()
# print(room1)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#

current_room = player.current_room

def print_room(room):
    print(f"---------------------")
    print(f"\n{room.name}")
    print(f"\n  {room.description}\n")

while True:
    current_room = player.current_room
    userInput = input("Make a move: ")

    # print(current_room)

    if userInput == "n":
        if current_room.n_to is not None:
            player.current_room = current_room.n_to
            print_room(player.current_room)
        else:
            print("You can't go there")

    elif userInput == "s":
        if current_room.s_to is not None:
            player.current_room = current_room.s_to
            print_room(player.current_room)
        else:
            print("You can't go there")

    elif userInput == "w":
        if current_room.w_to is not None:
            player.current_room = current_room.w_to
            print_room(player.current_room)
        else:
            print("You can't go there")

    elif userInput == "e":
        if current_room.e_to is not None:
            player.current_room = current_room.e_to
            print_room(player.current_room)
        else:
            print("You can't go there")

    elif userInput == "q":
        print("Till next time!")
        exit()
    else:
        print("Move invalid")


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# while int(userInput) !== "treasure"
#     userInput = input("Select the direction")