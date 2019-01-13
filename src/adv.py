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
    'foyer':    Room("Foyer",
                     """Dim light filters in from the south. Dusty
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

# Main

name_bypass = 1
game_state = 1
player = ""

dingus = Item("Dingus", "This really dings.")

room["outside"].add_item(dingus)
# Method to attempt to changes rooms


def try_direction(direction, current_room):
        # appends direction attr to direction to be readable by the map
    direction_attribute = direction + "_to"
    # Check if direction has valid direction_attribute
    if hasattr(current_room, direction_attribute):
        # fetch the new room
        return getattr(current_room, direction_attribute)
    else:
        cls()
        print("-" * 40 + f'\n{direction} is an invalid direction.')
        return current_room


# When game_state is 1, game will begin, 0 to stop the game
while game_state is 1:
    # Allows to bypass the name for testing
    if player == "":
        player = Player("Test Name", room['outside'])
        cls()
        if name_bypass == 0:
            player_name = input("Insert name: ")
            player.name = player_name.capitalize()
            name_bypass = 1

    # TEST PRINTS
    print(f"{player.current_room}")
    print(player)
    print("-" * 40)
    # accepts input from user and converts to lowercase
    player_input = input(f'Enter a direction > ').lower()
    cls()
    # Split player_input into two arguments
    if len(player_input.split(' ', 1)) > 2:
        player_input_option1 = player_input.split(' ', 1)[0]
        player_input_option2 = player_input.split(' ', 1)[1]
    else:
        player_input_option1 = player_input.split(' ', 1)[0]

    # Check if input was q, exit, or quit, then terminates the program
    if player_input_option1 == 'q' or player_input_option1 == 'exit' or player_input_option1 == 'quit':
        cls()
        game_state = 0

    # Travel check
    elif player_input_option1 in ("n", "s", "e", "w"):
        cls()
        player.current_room = try_direction(
            player_input_option1, player.current_room)

    elif player_input == "l":
        cls()
        print(player.look())
    else:
        cls()
        print("Command not found.")
