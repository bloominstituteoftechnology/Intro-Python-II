from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("outside the Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("in a Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("on the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("in a Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("in the Treasure Chamber", """You've found the long-lost treasure
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


# Make a new player object that is currently in the 'outside' room.
name_input = input('Please select a name for your character.\n')
player = Player(room['outside'], name_input)
print(f'{player.name}! {player.room}.')

#------------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------

# Setting up cardinal directions and decision prompt
cardinals = ['n', 'e', 's', 'w']

input_text = 'Which direction would you like to move? \n\
    [n] North  [e] East  [s] South  [w] West  [q] Quit\n\n'

decision = input(input_text)

# Item initialization


# Main game loop
while not decision == 'q':
    if decision in cardinals:
        player.room = player.movement(decision)
        decision = input(input_text)
    else:
        print('Please select a valid direction. \n\
            [n] North  [e] East  [s] South  [w] West  [q] Quit\n\n')
        decision = input(input_text)

print('\nThe quest has been abandoned...')