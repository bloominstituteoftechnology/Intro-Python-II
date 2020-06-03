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
player1 = Player('Player 1', room['outside'])

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

# // print current state
# // need user input
# // while stuff is going on, do something
# // if user input is cardinal direction, move-if allowed (error state)
# // Else quit

user_input = ''
while user_input != 'Q':
    print(player1)
    prompt = f'{player1.player_name}, what would you like to do? Move N, S, E, W, or Quit?'
    print("\n".join(textwrap.wrap(prompt, 38)))
    user_input = input().capitalize()
    if user_input == 'N':
        if player1.in_room == room['outside']:
            print('Moving North')
            player1.in_room = room['foyer']
        elif player1.in_room == room['foyer']:
            print('Moving North')
            player1.in_room = room['overlook']
        elif player1.in_room == room['narrow']:
            print('Moving North')
            player1.in_room = room['treasure']
        else:
            print('Invalid move')
    elif user_input == 'S':
        if player1.in_room == room['foyer']:
            print('Moving South')
            player1.in_room = room['outside']
        elif player1.in_room == room['overlook']:
            print('Moving South')
            player1.in_room = room['foyer']
        elif player1.in_room == room['treasure']:
            print('Moving South')
            player1.in_room = room['narrow']
        else:
            print('Invalid move')
    elif user_input == 'E':
        if player1.in_room == room['foyer']:
            print('Moving East')
            player1.in_room = room['narrow']
        else:
            print('Invalid move')
    elif user_input == 'W':
        if player1.in_room == room['narrow']:
            print('Moving West')
            player1.in_room = room['foyer']
        else:
            print('Invalid move')
    elif user_input == 'Q':
        print('You have decided to end your quest. Game Over.')
    else:
        print('Input not recognized.')