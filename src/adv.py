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


name = input('What is your name, Adventurer? ')
player = Player(name, room['outside'])

print(f'Welcome {name}. Begin your adventure from {player.current_room}')
# print(room['outside'].n_to)

while True:
    direction = input('Choose your next direction. (n for North, s for South, e for East, w for West, q to Quit) ')

    if direction == 'n' or direction == 'N':
        next_move = player.current_room.n_to
        if next_move == None:
            print("Can't go that way. Try a different direction.")
        else:
            player = Player(name, next_move)
            print(player)

    elif direction == 's' or direction == 'S':
        next_move = player.current_room.s_to
        if next_move == None:
            print("Can't go that way. Try a different direction.")
        else:
            player = Player(name, next_move)
            print(player)
    
    elif direction == 'e' or direction == 'E':
        next_move = player.current_room.e_to
        if next_move == None:
            print("Can't go that way. Try a different direction.")
        else:
            player = Player(name, next_move)
            print(player)
    
    elif direction == 'w' or direction == 'W':
        next_move = player.current_room.w_to
        if next_move == None:
            print("Can't go that way. Try a different direction.")
        else:
            player = Player(name, next_move)
            print(player)
    
    elif direction == 'q' or direction == 'Q':
        print('Goodbye Adventurer!')
        break
        



