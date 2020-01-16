# Declare all the rooms
from src.room import Room

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
currentRoom = room['outside']
player = str(input("[N] North  [S] South   [E] East   [W] West    [Q] Quit\n"))

# Write a loop that:
#
# * Prints the current room name
# gamplay loop
while not player == "Q":
    # player chooses North
    if player == "N":
        if currentRoom == room['outside']:
            print("You find yourself outside.")
        elif currentRoom == room['foyer']:
            print("You find yourself in the foyer.")
        elif currentRoom == room['narrow']:
            print("You find yourself in the foyer.")
        else:
            print("You found the treasure!!!")

    # player chooses South
    elif player == "S":
        if currentRoom == room['outside']:
            print("You find yourself outside.")
        elif currentRoom == room['foyer']:
            print("You find yourself in the foyer.")
        elif currentRoom == room['narrow']:
            print("You find yourself in the foyer.")
        else:
            print("You found the treasure!!!")


    # player chooses East
    elif player == "E":
        if currentRoom == room['outside']:
            print("You find yourself outside.")
        elif currentRoom == room['foyer']:
            print("You find yourself in the foyer.")
        elif currentRoom == room['narrow']:
            print("You find yourself in the foyer.")
        else:
            print("You found the treasure!!!")

    # player chooses West
    elif player == "W":
        if currentRoom == room['outside']:
            print("You find yourself outside.")
        elif currentRoom == room['foyer']:
            print("You find yourself in the foyer.")
        elif currentRoom == room['narrow']:
            print("You find yourself in the foyer.")
        else:
            print("You found the treasure!!!")
    else:
        print("Please choose a valid Cardinal Direction...")

    # prompt player to make another selection
    print("Please choose a Direction to continue...")

    # initialize player
    player = str(input("[N] North  [S] South   [E] East   [W] West    [Q] Quit\n"))

# Game over
print("Game Over. Thanks for playing!!")

# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
