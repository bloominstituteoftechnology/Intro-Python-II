from room import Room
from player import Player
import types

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

player = Player(room=room['outside'])

# Make a new player object that is currently in the 'outside' room.


def parse_command(command):
    split_list = command.lower().split()
    print(split_list)
    # split_list = list(map(lambda x: x.lower(), split_list))

    if 'north' in split_list:
        if player.room.n_to is None:
            print("That's not possible try again.")
        else:
            player.setRoom(player.room.n_to)
    if 'east' in split_list:
        if player.room.n_to is None:
            print("That's not possible try again.")
        else:
            player.setRoom(player.room.e_to)
    if 'south' in split_list:
        if player.room.n_to is None:
            print("That's not possible try again.")
        else:
            player.setRoom(player.room.s_to)
    if 'west' in split_list:
        if player.room.n_to is None:
            print("That's not possible try again.")
        else:
            player.setRoom(player.room.w_to)
    if 'quit' in split_list:
        confirmation = input('Are you sure you want to quit: ').lower()
        if confirmation == 'yes':
            global running
            running = False
        else:
            return


def list_items():
    if len(player.room.items) != 0:
        stringified_list = '\n'.join(player.room.items)
        print(f"In the room you see the following items: \n{stringified_list}")


def process_input():
    player_input = input('What do you wish to do?: ')
    parse_command(player_input)


def update():
    return


def draw():
    print(player.room.name)
    print(player.room.description)
    list_items()


running = True


def main_loop():
    while running:
        process_input()
        update()
        draw()


def start():
    draw()
    main_loop()


start()

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
