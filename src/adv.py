from room import Room
from player import Player

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
"""
|---------------------|
|overlook -  treasure |
|  |            |     |
|foyer    -   narrow  |
|  |                  |
|outside              |
|---------------------|

"""


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


# print(room['outside'].n_to)

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

current_room = room['outside']
player = Player('student', current_room)
user = ''
i = 0
print('\n==== WELCOME TO THE ADVENTURE ====', '\n'*3)

while not user == 'q':
    print(f'\nPlayer currently in \n{player.current_room}\n')
    # print(player)
    print(f'Keyboard Hit#: {i}\n')
    i += 1

    user = input("[n] north  [e] east   [s] south [w] west  [q] Quit\n")

    if(user == 'q'):
        break
    print('\n   ...Loading\n   Please Wait\n')
    player.move(user)

print('\n'*3, '==== END OF THE ADVENTURE ====\n')
print('Thanks for enjoying the adventure!\nSee you next time!\n')