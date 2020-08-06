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
#Main

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.
# Make a new player object that is currently in the 'outside' room.

player = Player(name=input("Welcome to the Adventure Game! What is your name? "), location=room['outside'])

print(player.name, player.location)
commands = ["N", "S", "E", "W"]
# Write a loop that:
while True:
    userInput = input(f"Great! Now enter which direction you will choose to go. Here are your options: {commands}. Enter Q if you would like to quit.")

    command = input("> ").split(',')

#    if command[0] == 'q':
#        break
#        elif command[0] == 'n':
#        # check if the player can move to the north
#        # if there is, set that north room as the player's location
#        elif command[0] == 's':
#
#        elif command[0] == 'e':
#
#        elif command[0] == 'w':
