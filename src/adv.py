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

player = Player('', '')

# Link rooms together

room['outside'].w_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].w_to = room['overlook']
room['foyer'].d_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].a_to = room['foyer']
room['narrow'].w_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

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
start_game = input("Would you like to play a game? (y,n) ")
if start_game == "y":
    user_name = input("What would you like to be called? ")
    player = Player(user_name, room['outside'])
    while True:
            print(f"{player.name} you are at {player.location.name} and {player.location.description} \n")
            user = input(f"{player.name} where would you like to go? [w] north [s] south [a] west [d] east [q] quit: ")
            if user in ["w", "s", "a", "d"]:
                player.move(user)
            elif user == "q":
                print("Ending Simulation")
                break
            else:
                print("Please try another input.")
else: 
    print("Maybe next time")