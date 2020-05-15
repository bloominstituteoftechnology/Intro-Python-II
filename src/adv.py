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
name = input('Stay thy name adventurer!')
player = Player(name,room['outside'])

# Write a loop that:
#
# * Prints the current room name
print(f'###### Welcome {player.name}, your are at {player.room}')

def gameplay(player):
    direction = input('Which do want to do? (Press N for North, E for east , W for West , S for South. Q for quit game')

    while direction != 'Q':
        if direction == 'N':
            player.current_room = player.current_room.n_to
            print('The player is now in the', player.current_room.name)
        elif direction == 'S':
            player.current_room = player.current_room.s_to
            print('The player is now in the', player.current_room.name)
        elif direction == 'E':
            player.current_room = player.current_room.e_to
            print('The player is now in the', player.current_room.name)
        elif direction == 'W':
            player.current_room = player.current_room.w_to
            print('The player is now in the', player.current_room.name)
        elif direction == 'Q':
            break
        else:
            print("Invalid choice,choose again")

    print(f'Thanks for Playing!')







# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
