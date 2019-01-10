# Import classes from external files
from room import Room
from player import Player
from item import Item

# Import os for clear screen function
import os

# Clear screen function


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("the Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("the Treasure Chamber", """You've found the long-lost treasure
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

# Main

name_bypass = 1
game_state = 1

# Make a new player object that is currently in the 'outside' room.
player = Player("Test Name", room['outside'])

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

"""
direction is the direction of the user input
current_Room is the current room the player is in
returns the new room the player moves to if the
move was successful, or returns current room if
the move was unsuccessful.
"""


def try_direction(direction, current_room):
    direction_attribute = direction + "_to"

    # Check if direction has valid direction_attribute
    if hasattr(current_room, direction_attribute):
        # fetch the new room
        return getattr(current_room, direction_attribute)
    else:
        print('Invalid direction.' + '\n' + "-" * 40)
        return player.current_room


while game_state is 1:
    if name_bypass == 0:
        player_name = input("Insert name: ")
        player.name = player_name.capitalize()
        name_bypass = 1
    print(f'You are at the {player.current_room}')

    # accepts input from user and converts to lowercase
    player_input_option = input(
        f'Which direction would you like to go? ').lower()
    cls()
    # check if input was q, exit, or quit, then terminates the program
    if player_input_option == 'q' or player_input_option == 'exit' or player_input_option == 'quit':
        cls()
        break
    if player_input_option.split(' ', 1)[0] == "pickup":
        print('Tried to pickup')
    #
    elif player_input_option:
        player.current_room = try_direction(
            player_input_option, player.current_room)

    else:
        cls()
        print("Command not found.")
