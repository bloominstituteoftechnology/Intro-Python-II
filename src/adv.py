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
new_player = Player("Joe", room['outside'])

# Welcome message
print("Welcome to the Adventure Game!")
print("Please choose a direction to move.")

game_running = True

# Write a loop that:
while game_running:
    # * Prints the current room name
    print("Current room:", new_player.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print("Description:", new_player.current_room.description)
    # * Waits for user input and decides what to do.
    user = input("[n] north [s] south [e] east [w] west [q] quit\n")
    # If the user enters a cardinal direction, attempt to move to the room there.
    if user == "n":
        # rooms you can travel north from
        if new_player.current_room in (room['outside'], room['foyer'], room['narrow']):
            new_player.current_room = new_player.current_room.n_to
        else:
            print("Try a different direction!")
    elif user == "s":
        # rooms you can travel south from
        if new_player.current_room in (room['foyer'], room['overlook'], room['treasure']):
            new_player.current_room = new_player.current_room.s_to
        else:
            print("Try a different direction")
    elif user == "e":
        # rooms you can travel east from
        if new_player.current_room in (room['foyer']):
            new_player.current_room = new_player.current_room.e_to
        else:
            print("Try a different direction")
    elif user == "w":
        # rooms you can travel west from
        if new_player.current_room in (room['narrow']):
            new_player.current_room = new_player.current_room.w_to
        else:
            print("Try a different direction")
    # If the user enters "q", quit the game
    elif user == "q":
        print("Game Over!")
        break
    else:
        print("Not a valid input!")
