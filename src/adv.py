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
print('Welcome to the game! Enter a name for your player...')
name = input('>>>')
player = Player(name, room['outside'])

playerInput = ''
while playerInput != 'Q' or 'q':
    print(player1)
    print('Choose your next move: [N] North [S] South [E] East [W] West [Q] Quit')
    playerInput = input('>>').upper()

    if playerInput == 'N' or playerInput == 'S' or playerInput == 'E' or playerInput == 'W':
        if playerInput == "N" and player.room.n_to != None:
            player.room = player.room.n_to
        elif playerInput == "E" and player.room.e_to != None:
            player.room = player.room.e_to
        elif playerInput == "S" and player.room.s_to != None:
            player.room = player.room.s_to
        elif playerInput == "W" and player.room.w_to != None:
            player.room = player.room.w_to
        else:
            print("You can't move in that direction")
    elif playerInput == "Q":
        print('You ended the game')
        break
    else:
        print('That is not a valid input')

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
