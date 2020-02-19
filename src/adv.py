from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),
    'foyer':Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook':Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure':Room("Treasure Chamber", """You've found the long-lost treasure
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
player_1 = Player("1", room['outside'])
wrappedDesc = textwrap.wrap(player_1.currentRoom.desc)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

def askUserInput(printArg1=f"Player's current room: {player_1.currentRoom.name}", 
                printArg2=f"Current room desc: {wrappedDesc}", 
                printArg3="Select one of the following direction to move the player. \nN (north), S (south), E (east), W (west):\n ---> "):
    print(printArg1)
    print(printArg2)
    userInput = input()
    return userInput.lower(printArg3)

lowUserInput = askUserInput()
while lowUserInput:
    if lowUserInput == "n" or lowUserInput == "s" or lowUserInput == "e" or lowUserInput == "w":
        lowUserInput = askUserInput()
    else:
        printArg1 = ""
        if len(lowUserInput) == 0:
            printArg1 = "Please enter a value from N, S, E, W"
        elif len(lowUserInput) > 1:
            printArg1 = "You can only select a value from N, S, E, W"
        else:
            printArg1 = "This movement is not allowed"
        lowUserInput = askUserInput(printArg1, "", "")


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
