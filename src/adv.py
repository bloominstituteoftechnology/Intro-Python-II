from room import Room
from player import Player
from item import Item

# Textwrap module
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
print('Hello there!')
new_player = input('What is your name?')
if len(new_player) == 0:
    print('Please enter your name.\n')
player = Player(new_player, room['outside'])
print(f'Welcome to the game, {player.name}!')
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
    # * Prints the current room name
    print(f'\nCurrent Location: {player.current_room.name[0]}')

    # * Prints the current description (the textwrap module might be useful here).
    print(f'\nLocation Description: {player.current_room.description}')

    # commands
    print('''
        Explore the map by entering one of the following: 
        "n" for North
        "s" for South
        "w" for West
        "e" for East
        ''')

    print('Enter "q" to quit the game.')

    # * Waits for user input and decides what to do.
    current_room = player.current_room.name
    choice = input('What would you like to do?')
    if len(choice) != 1:
        print('Invalid input, please try again.')
    if choice == 'q':
        print(f'Goodbye, {player.name}!')
        break
    if choice == 'n':
        player.move(choice)
    if choice == 's':
        player.move(choice)
    if choice == 'w':
        player.move(choice)
    if choice == 'e':
        player.move(choice)
    else:
        print('Not a valid choice, please choose again.')

