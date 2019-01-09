from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     ["Sword", "Shield"]),

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
    print_user_info(player.room)

    # user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))

    while True:
        input = get_input()

        if len(input) == 1:
            if input[0] == "q":
                print("Saionara my friend")
                break

            elif input[0] == "n":
                try:
                    player.room = player.room.n_to
                    print_user_info(player.room)
                except AttributeError:
                    print_direction_error(input)

            elif input[0] == "e":
                try:
                    player.room = player.room.e_to
                    print_user_info(player.room)
                except AttributeError:
                    print_direction_error(input)

            elif input[0] == "s":
                try:
                    player.room = player.room.s_to
                    print_user_info(player.room)
                except AttributeError:
                    print_direction_error(input)

            elif input[0] == "w":
                try:
                    player.room = player.room.w_to
                    print_user_info(player.room)
                except AttributeError:
                    print_direction_error(input)
            else:
                print("Cannot parse your input. Please try again.\n")
        elif len(input) == 2:
            action = input[0]
            item = input[1]

            if item not in player.room.items:
                print("Item doesn't exist. Choose an item in the room: " + player.room.get_all_items() + "\n")
                pass

            if action == "take":
                player.add_item(item)
                player.room.remove_item(item)
                print(f"Your current items: {player.get_all_items()}\n")
            elif action == "drop":
                player.remove_item(item)
                player.room.add_item(item)
                print(f"Your current items: {player.get_all_items()}\n")
            else:
                print("Cannot parse your input. Please try again.\n")
        else:
            print("Cannot parse your input. Please try again.\n")

def print_user_info(room):
    print(f"You are currently in the {room.name}.")
    for line in textwrap.wrap(room.description):
        print(line)
    print(room.get_all_items() + "\n")

def get_input():
    return input("What shall we do?\nGo to [n] north, [e] east, [s] south, [w] west, \n[take] or [drop] [items]: ").split()

def print_direction_error(direction):
    print(f"You cannot move {direction} from here.")

if __name__ == '__main__':
    initiate_game()