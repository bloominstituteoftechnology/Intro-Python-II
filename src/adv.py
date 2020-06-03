from room import Room
from player import Player
import getpass

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
playerName = getpass.getuser().title()

print("\nAncient prophecies have fortold your arrival...\n\nWelcome {}!".format(playerName))
player = Player(playerName, room["outside"])

# Write a loop that:
#e
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

intro = """
The Forsaken Dungeon is full of terrors and treasure.
Search each room for the untold bounties of this realm 
using the four cardinal directions (n, s, w, e).

If you wish to return to safety, simply quit the game (q).
Your treasure will be lost as everything is temporary...even your inevitable suffering.

Beware the creatures and dark magic lurking around every corner."""

print(intro)

print("\nStarting location: " + player.location.name)

user_prompt = "\nMove or quit, the choice is yours... "

directions = ["n", "s", "e", "w"]

# Next part of game
response = ""
while response not in directions:
    
    response = input(user_prompt)

    if response == "n":
        player.move(response)
        print("Current location: " + player.location.name, "\nPrevious direction input: ", response)
        response = ""

    elif response == "s":
        player.move(response)
        print("Location: " + player.location.name, "\nPrevious direction input: ", response)
        response = ""

    elif response == "w":
        player.move(response)
        print("Location: " + player.location.name, "\nPrevious direction input: ", response)
        response = ""

    elif response == "e":
        player.move(response)
        print("Location: " + player.location.name, "\nPrevious direction input: ", response)
        response = ""

    elif response == "q":
        quit()

    else:
        print("I didn't understand that.\n")
