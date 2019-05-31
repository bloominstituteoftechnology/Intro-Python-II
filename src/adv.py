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

import textwrap

# grabs user input
def grab_direction():
    direction = input("\nPlease enter a direction of travel: ").lower()
    if direction in ["n", "s", "e", "w", "q"]:
        return direction
    else:
        print("Invalid entry! Please use 'n', 's', 'e' or 'w' to navigate\nEnter 'q' to exit the game")
        grab_direction()

# checks to see if room has direction attribute
def try_direction(direction, current_room):
    attribute = direction + "_to"

    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
        print(direction_error(direction))
        return current_room

# error messages for invalid room directions
def direction_error(direction):
    if direction == "n":
        return "There is no room to the North\n"
    elif direction == "s":
        return "There is no room to the South\n"
    elif direction == "e":
        return "There is no room to the East\n"
    elif direction == "w":
        return "There is no room to the West\n"
    else:
        return "Goodbye!"

print("Welcome to the game!\n")
username = input("Please enter your players name: ")
print(f"\nHello {username}, within this game you can navigate rooms using n, s, w, or e")

# Make a new player object that is currently in the 'outside' room.
player = Player(username, room["outside"])

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
direction = None
while (direction != "q"):
    print("Current Position: " + 
        textwrap.fill(player.current_room.name + 
        ". " + player.current_room.description, width=50))
    direction = grab_direction()
    player.current_room = try_direction(direction, player.current_room)