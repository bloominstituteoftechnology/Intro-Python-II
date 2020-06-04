from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room('Outside Cave Entrance',
                     'North of you, the cave mount beckons'),

    'foyer':    Room('Foyer', """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room('Grand Overlook', """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room('Narrow Passage', """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room('Treasure Chamber', """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = {
    'coins': Item('coins', 'Shiny currency'),
    'sword': Item('sword', 'Steel blade'),
    'shield': Item('shield', 'It protect')
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

# Add items to rooms

room['foyer'].items = items['coins']
room['overlook'].items = items['sword']
room['narrow'].items = items['shield']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print('Welcome foolish mortal, please state your name.')
player_name_input = input('> ')
player1 = Player(f'{player_name_input}', room['outside'])

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
    if player1.current_room.items != []:
        print(player1.current_room.items)
    else:
        print('No items in this room.')
    print(f'{player1.name}, what would you like to do? Move N, S, E, W, or take/drop item, or Quit?')
    user_input = input('> ')
    input_args = user_input.split(" ")
    if len(input_args) == 1:
        if input_args[0] == 'N' or 'n':
            if player1.current_room.n_to != None:
                print('Moving North')
                player1.current_room = player1.current_room.n_to
            else:
                print('Invalid move')
        elif input_args[0] == 'S' or 's':
            if player1.current_room.s_to != None:
                print('Moving South')
                player1.current_room = player1.current_room.s_to
            else:
                print('Invalid move')
        elif input_args[0] == 'E' or 'e':
            if player1.current_room.e_to != None:
                print('Moving East')
                player1.current_room = player1.current_room.e_to
            else:
                print('Invalid move')
        elif input_args[0] == 'W' or 'w':
            if player1.current_room.w_to != None:
                print('Moving West')
                player1.current_room = player1.current_room.w_to
            else:
                print('Invalid move')
        elif input_args[0] == 'Q':
            print('You have decided to end your quest. Game Over.')
    elif len(input_args) == 2:
        if input_args[0] == 'take' or 'Take':
            print('Taking item.')
            # take item
        elif input_args[0] == 'drop' or "Drop":
            print('Dropping item.')
            # drop item
    else:
        print('Input not recognized.')