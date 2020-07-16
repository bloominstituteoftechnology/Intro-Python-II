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


# Main -----------------------------------------------------------


# Make a new player object that is currently in the 'outside' room.
name_input = input('Please select a name for your character.\n')
player = Player(room['outside'], name_input)
print(player.room)

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

cardinals = ['n', 'e', 's', 'w']

input_text = 'Which direction would you like to move? \n\
    [n] North  [e] East  [s] South  [w] West  [q] Quit\n\n'

decision = input(input_text)


# Main game loop

while not decision == 'q':
    if decision in cardinals:
        player = player.movement(decision)
        print(player, '\n')
        decision = input(input_text)

    else:
        print('Sorry, try a different direction...')

print('\nThe quest has been abandoned...')




# while not decision == 'q':

#     # Player is 'outside'
#     if player == room['outside']:
#         if decision == 'north' or decision == 'n':
#             player = room['outside'].n_to
#             print(player, '\n')
#             decision = input(input_text)
#         elif decision == 'south' or decision == 's':
#             print('That would mean you leave. Don\'t do that...\n')
#             decision = input(input_text)
#         else:
#             print('You cannot go that direction, sorry.')
#             decision = input(input_text)

#     # Player is in the 'foyer'
#     elif player == room['foyer']:
#         if decision == 'north' or decision == 'n':
#             player = room['foyer'].n_to
#             print(player, '\n')
#             decision = input(input_text)
#         if decision == 'east' or decision == 'e':
#             player = room['foyer'].e_to
#             print(player, '\n')
#             decision = input(input_text)
#         if decision == 'south' or decision == 's':
#             player = room['foyer'].s_to
#             print(player, '\n')
#             decision = input(input_text)
#         else:
#             print('You cannot go that direction, sorry...\n')
#             decision = input(input_text)

#     # Player is on the 'overlook'
#     elif player == room['overlook']:
#         if decision == 'south' or decision == 's':
#             player = room['overlook'].s_to
#             print(player, '\n')
#             decision = input(input_text)
#         else:
#             print('You cannot go that direction, sorry...\n')
#             decision = input(input_text)

#     # Player is in 'narrow' passage
#     elif player == room['narrow']:
#         if decision == 'north' or decision == 'n':
#             player = room['narrow'].n_to
#             print(player, '\n')
#             decision = input(input_text)
#         if decision == 'east' or decision == 'e':
#             player = room['narrow'].e_to
#             print(player, '\n')
#             decision = input(input_text)
#         if decision == 'south' or decision == 's':
#             player = room['narrow'].s_to
#             print(player, '\n')
#             decision = input(input_text)
#         else:
#             print('You cannot go that direction, sorry...\n')
#             decision = input(input_text)
    
#     # Player is in the 'treasure' room
#     elif player == room['treasure']:
#         if decision == 'south' or decision == 's':
#             player = room['treasure'].s_to
#             print(player1, '\n')
#             decision = input(input_text)
#         else:
#             print('You cannot go that direction, sorry...\n')
#             decision = input(input_text)
#     else:
#         if decision == 'q' or decision == 'quit':
#             print('The quest has been abandoned...')
#             break