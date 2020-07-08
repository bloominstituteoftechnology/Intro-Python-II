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


def input_parser():

    command = input(
        "Please type one of the following commands: n (to go north), s (to go south), e (to go east), w (to go west), or q (to exit the game)\n")

    return command
#
# Main
#

# Make a new player object that is currently in the 'outside' room.


new_player = Player("David", room['outside'])

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

while True:
    # print player name, current location, and location description
    print(f" hello {new_player.name}, ")
    print(f"You are currently located in the {new_player.current_room.name}")
    print(new_player.current_room.description)

    # call input parser for user command
    command = input_parser()

    # player movement based on user input

    # if player input == 'q'
    if command == 'q':
        exit()

    # player input == 'n'
    if command == 'n':
        try:
            new_player = Player(
                "David,", new_player.current_room.n_to)
            print(
                f"you have moved to the north and entered the {new_player.current_room.name}")
        except:
            print("you have run into a dead end. try selecting a different direction.")

    # player input == 's'
    if command == 's':
        try:
            new_player = Player("David", new_player.current_room.s_to)
            print(
                f"you have moved to the south and entered the {new_player.current_room.name}")
        except:
            print("you have run into a dead end. try selecting a different direction.")

    # player input == 'e'
    if command == 'e':
        try:
            new_player = Player("David", new_player.current_room.e_to)
            print(
                f"you have moved to the east and entered the {new_player.current_room.name}")
        except:
            print("you have run into a dead end. try selecting a different direction.")

    # player input == 'w'
    if command == 'w':
        try:
            new_player = Player("David", new_player.current_room.w_to)
            print(
                f"you have moved to the west and entered the {new_player.current_room.name}")
        except:
            print("You have run into a dead end. try selecting a different direction.")
