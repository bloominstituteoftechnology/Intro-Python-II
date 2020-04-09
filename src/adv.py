from room import Room
from player import Player
from colors import print_color
import time


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


player_name = input('\nWhat is your name? ')

player = Player(player_name, room['outside'])

print_color('cyan', f'\nWelcome {player.name}!\n\n')

time.sleep(1)


def location_print(color):
    print_color(color, f'\n\nYour location: {player.current_room.name}')
    time.sleep(1.5)
    print_color(color, f'{player.current_room.description} \n')
    time.sleep(1.5)


while True:
    if player.current_room == room['outside']:
        location_print('green')
    elif player.current_room == room['foyer']:
        location_print('purple')
    elif player.current_room == room['overlook']:
        location_print('light_purple')
    elif player.current_room == room['narrow']:
        location_print('light_grey')
    elif player.current_room == room['treasure']:
        location_print('yellow')

    player_move = input("Enter 'n', 's', 'e', or 'w' to move rooms. ").lower()

    if player_move in ['n', 's', 'e', 'w']:
        player.move(player_move)
    elif player_move == 'q':
        exit()
    else:
        print_color('red', '\n\n\nInvalid input. Please try again.\n\n')
