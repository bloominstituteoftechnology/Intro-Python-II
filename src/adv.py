from room import Room
from player import Player
import textwrap

# Declare all the rooms

rooms = {
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

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print("Welcome foolish mortal, please state your name.")
player_name_input = input("> ")
player1 = Player(f'{player_name_input}')

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

# ~~Day 1~~
# print current state
# need user input
# while stuff is going on, do something
# if user input is cardinal direction, move-if allowed (error state)
# Else quit

# ~~Day 2~~
# add items to game
# room needs to hold items
# player needs to hold items
# add get [ITEM_NAME] and drop [ITEM_NAME]

user_input = ''
while user_input != 'Q':
    #print(player1.current_room.items)
    print(f'{player1.name}, what would you like to do? Move N, S, E, W, or Quit?')
    user_input = input("> ").capitalize()
    if user_input == 'N' or 'S' or 'E' or 'W':
        player1.movement = user_input
        player1.move()
    elif user_input == 'Q':
        print('You have decided to end your quest. Game Over.')
    else:
        print('Input not recognized.')