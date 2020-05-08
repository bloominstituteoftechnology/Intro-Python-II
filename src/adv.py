from room import Room
from player import Player

# Define the default prompt.

prompt = '> '

# Declare all the rooms

room = {
    'outside':  Room('Outside Cave Entrance',
                     'North of you, the cave mouth beckons.'),

    'foyer':    Room('Foyer',
                     ('Dim light filters in from the south. Dusty passages '
                      'run north and east.')),

    'overlook': Room('Grand Overlook',
                     ('A steep cliff appears before you, falling into the '
                      'darkness. Ahead to the north, a light flickers in the '
                      'distance, but there is no way across the chasm.')),

    'narrow':   Room('Narrow Passage',
                     ('The narrow passage bends here from west to north. The '
                      'smell of gold permeates the air.')),

    'treasure': Room('Treasure Chamber',
                     'You\'ve found the long-lost treasure chamber! Sadly, it '
                     'has already been completely emptied by earlier '
                     'adventurers. The only exit is to the south.'),
}


# Link rooms together

room['outside'].exits['n'] = room['foyer']
room['foyer'].exits['s'] = room['outside']
room['foyer'].exits['n'] = room['overlook']
room['foyer'].exits['e'] = room['narrow']
room['overlook'].exits['s'] = room['foyer']
room['narrow'].exits['w'] = room['foyer']
room['narrow'].exits['n'] = room['treasure']
room['treasure'].exits['s'] = room['narrow']

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
move = input(f'{player.room}\n\n{prompt}')
while move != 'q':
    try:
        player.room = player.room.exits[move]
        move = input(f'{player.room}\n\n{prompt}')
    except KeyError:
        move = input(f'There\'s no obvious way to do that.\n\n{prompt}')
