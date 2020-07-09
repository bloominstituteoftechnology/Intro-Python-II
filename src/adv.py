# Name of game is called Explore

from room import Room
from player import Player
import argparse
import time

# Argument Parser
explore_parser = argparse.ArgumentParser()
explore_parser.add_argument("-n", "--north", help="Moves player north")
explore_parser.add_argument("-w", "--west", help="Moves player west")
explore_parser.add_argument("-s", "--south", help="Moves player south")
explore_parser.add_argument("-e", "--east", help="Moves player east")
explore_parser.add_argument("-bp", "--backpack", help="Stores items for player")
explore_parser.add_argument("-q", "--quit", help="Quits the game")

args = explore_parser.parse_args()

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("at the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("at the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("at the Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("in the Treasure Chamber", """You've found the long-lost treasure
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
print("Welcome to Explore!")
print("What is your name explorer?")
player = input("> ")
new_player = Player(player, room["outside"])

user_input = ""
while user_input != "q":
    print("{}, you are {}, {}".format(new_player.name, new_player.room.name, new_player.room.description))
    print("What would you like to do? Enter n, s, e, or w to move or q to quit.")
    user_input = input("> ")
    # North
    if user_input == 'n':
        if new_player.room.n_to != None:
            print("Moving. Heading North.")
            time.sleep(2)
            new_player.room = new_player.room.n_to
        else:
            print("You cannot go that way.")
    # South
    elif user_input == 's':
        if new_player.room.s_to != None:
            print("Moving. Heading South.")
            time.sleep(2)
            new_player.room = new_player.room.s_to
        else:
            print("You cannot go that way.")
    # East
    elif user_input == 'e':
        if new_player.room.e_to != None:
            print("Moving. Heading East.")
            time.sleep(2)
            new_player.room = new_player.room.e_to
        else:
            print("You cannot go that way.")
    # West
    elif user_input == 'w':
        if new_player.room.w_to != None:
            print("Moving. Heading West")
            time.sleep(2)
            new_player.room = new_player.room.w_to
        else:
            print("You cannot go that way.")
    # Quit
    elif user_input == 'q':
        print("Well...")
        time.sleep(2)
        print("You have decided to end your quest.")
        time.sleep(1)
        print("Farewell!")
        quit()
    else:
        print("Please enter a proper decision")

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
