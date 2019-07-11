from room import Room
from player import Player
import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100


#Title Screen
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

player = Player("Jason", room['outside'])

directions = ["n", "s", "e", "w"]
actions = ["look", "help", "quit"]

def room_move(cmd, current_room):
    if cmd == 'n':
        return current_room.n_to
    if cmd == 's':
        return current_room.s_to
    if cmd == 'e':
        return current_room.e_to
    if cmd == 'w':
        return current_room.w_to


def help_menu():
     print("'N', 'E', 'S', 'W' to move")
     print("'Look' will examine your surroundings.")
     print("'Quit' will exit the game")


# Write a loop that:
while True:
    # * Prints the current room name

    player_input = input("->")
    cmd = player_input.lower().split()

    if cmd[0] == "look":
        print(player.current_room.description)

    elif cmd[0] == "quit":
        print("Goodbye!")
        break
    elif cmd[0] == "help":
        help_menu()


    elif cmd[0] in directions:
        new_room = room_move(cmd[0], player.current_room)
        if new_room is not None:
            player.current_room = new_room
            print(f"You have entered the {player.current_room.name}")
        else:
            print("Can't move in that direction")
    elif cmd[0] not in directions + actions:
        print("Type 'help' for a list of commands.")
        


# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
