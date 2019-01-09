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

def initiate_game():
    player = Player(room['outside'])
    print("Let's play a game")
    print_user_info(player.room.name, player.room.description)

    # user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))

    while True:
        direction = get_direction()

        if direction == "q":
            print("Saionara my friend")
            break

        elif direction == "n":
            try:
                player.room = player.room.n_to
                print_user_info(player.room.name, player.room.description)
            except AttributeError:
                print_direction_error(direction)

        elif direction == "e":
            try:
                player.room = player.room.e_to
                print_user_info(player.room.name, player.room.description)
            except AttributeError:
                print_direction_error(direction)

        elif direction == "s":
            try:
                player.room = player.room.s_to
                print_user_info(player.room.name, player.room.description)
            except AttributeError:
                print_direction_error(direction)

        elif direction == "w":
            try:
                player.room = player.room.w_to
                print_user_info(player.room.name, player.room.description)
            except AttributeError:
                print_direction_error(direction)
        else:
            print("Cannot parse your input. Please try again.")

def print_user_info(room, description):
    print(f"You are currently in the {room}.")
    for line in textwrap.wrap(description):
        print(line)

def get_direction():
    return input("In which direction shall we move? Go to [n] north, [e] east, [s] south, [w] west: ")

def print_direction_error(direction):
    print(f"You cannot move {direction} from here.")

if __name__ == '__main__':
    initiate_game()