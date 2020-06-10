import code

from room import Room
from player import Playerr

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

directions = ['n', 's', 'e', 'w']
p = Player("Ryan", room ['outside'])

print(f'Welcome {p.name}!\nExplore the map by moving North(n), South(s), East(e), or West(w)\nTo exit the game, enter q\n')
print(f'You are in the {p.current_room.name} - {p.current_room.description}\n')

while True:
    selection = input('Where to? ').lower().split(' ')
    
    if selection == 'q':
        print('Thanks for playing!') 
        break
    
    try:
        if selection in directions:
            try:
                p.move_room(selection)
                print(f'The current room is {p.current_room.name} - {p.current_room.description}')
            except AttributeError:
                print('No room there, try another direction')
        else:
            print('Movement not allowed! Please enter a direction (n, s, e, w) to move around the map')
    except KeyError:
        print('Unknown territory! Please enter a valid direction or quit the game')-4

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
