import textwrap
import os
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
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
commands = {
    'n': 'You move north.',
    'e': 'You move east.',
    's': 'You move south.',
    'w': 'You move west.',
    'q': 'Are you sure you want to quit (Y/N)? '
}


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def validate_move(user_input):
    if user_input in commands:
        if user_input == 'q':
            yn = input(commands[user_input])
            clear()
            if yn.lower() == 'y':
                return False
            else:
                return True
        else:
            print(commands[user_input])
            return True
    else:
        print('--------------------')
        print('|' + 'Input invalid.'.center(18, ' ') + '|')
        print('|' + 'n - Move North'.center(18, ' ') + '|')
        print('|' + 's - Move South'.center(18, ' ') + '|')
        print('|' + 'e - Move East'.center(18, ' ') + '|')
        print('|' + 'w - Move West'.center(18, ' ') + '|')
        print('|' + 'q - Exit game'.center(18, ' ') + '|')
        print('--------------------')


while True:
    print(player.room.name)
    wrapper = textwrap.TextWrapper(width=50)
    word_list = textwrap.TextWrapper(
        width=50).wrap(text=player.room.description)
    # Print each line.
    for element in word_list:
        print(element)
    user_input = input('What will you do? ')
    clear()
    checked = validate_move(user_input)
    if not checked:
        break
    else:
        continue
