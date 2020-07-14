from room import Room
from player import Player
import random

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

print(player)

# Write a loop that:

while player.room != room["treasure"]:
    n = input("\nPress q to quit or choose North, East, South, West: ")
    if n == "q":
        break
    elif (player.room == room['foyer']) & (n.lower().title() == "East"):
        print(f"Enetering a new area ... \n")
        player.room = room['foyer'].e_to
        print(player.room)
    elif (player.room == room['narrow']) & (n.lower().title() == "West"):
        print(f"Enetering a new area ... \n")
        player.room = room['narrow'].w_to
        print(player.room)
    elif (player.room == room['foyer']) & (n.lower().title() == "North"):
        print(f"Enetering a new area ... \n")
        player.room = room['foyer'].n_to
        print(player.room)
    elif (player.room == room['foyer']) & (n.lower().title() == "South"):
        print(f"Enetering a new area ... \n")
        player.room = room['foyer'].s_to
        print(player.room)
    elif (player.room == room['overlook']) & (n.lower().title() == "South"):
        print(f"Enetering a new area ... \n")
        player.room = room['overlook'].s_to
        print(player.room)
    elif (player.room == room['outside']) & (n.lower().title() == "North"):
        print(f"Enetering a new area ... \n")
        player.room = room['outside'].n_to
        print(player.room)
    elif (player.room == room['narrow']) & (n.lower().title() == "North"):
        print(f"Enetering a new area ... \n")
        player.room = room['narrow'].n_to
        print(player.room)
    else:
        ls = ["The way is blocked..", "I wouldn't go that way...", "Try Again...", "You shall not pass.."]
        print(random.sample(ls, 1)[0])
        


#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
