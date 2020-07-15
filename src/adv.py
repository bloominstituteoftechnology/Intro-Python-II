from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

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


name_input = input('Please select a name for your character.')

player1 = Player(room['outside'].room, room['outside'].description, name_input)
print(player1)

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

user_input = input(
    'Which direction would you like to move? \n\
    [n] North  [e] East  [s] South  [w] West  [q] Quit'
    )

user_input = user_input.lower()

while not user_input == 'q' or user_input == 'quit':
    # Player is 'outside'
    if player1 == room['outside']:
        if user_input == 'north' or user_input == 'n':
            player1 = room['outside'].n_to
            print(player1)
        elif user_input == 'south' or user_input == 's':
            print('That would mean you leave. Don\'t do that')
        else:
            print('You cannot go that direction, sorry.')

    elif player1 == room['foyer']:
        # Player is in the 'foyer'
        if user_input == 'north' or user_input == 'n':
            player1 = room['foyer'].n_to
            print(player1)
        if user_input == 'east' or user_input == 'e':
            player1 = room['foyer'].e_to
            print(player1)
        if user_input == 'south' or user_input == 's':
            player1 = room['foyer'].s_to
            print(player1)
        else:
            print('You cannot go that direction, sorry.')

    elif player1 == room['overlook']:
        # Player is on the 'overlook'
        if user_input == 'south' or user_input == 's':
            player1 = room['overlook'].s_to
            print(player1)
        else:
            print('You cannot go that direction, sorry.')

    elif player1 == room['narrow']:
        # Player is in 'narrow' passage
        if user_input == 'north' or user_input == 'n':
            player1 = room['narrow'].n_to
            print(player1)
        if user_input == 'east' or user_input == 'e':
            player1 = room['narrow'].e_to
            print(player1)
        if user_input == 'south' or user_input == 's':
            player1 = room['narrow'].s_to
            print(player1)
        else:
            print('You cannot go that direction, sorry.')
    
    else:
        if user_input == 'south' or user_input == 's':
            player1 = room['treasure'].s_to
            print(player1)
        else:
            print('You cannot go that direction, sorry.')