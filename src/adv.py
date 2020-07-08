from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount beckons""", ['foyer', None, None, None]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dustypassages run north and east.""", ['overlook', 'narrow', 'outside', None]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [None, None, 'foyer', None]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['treasure', None, None, 'foyer']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [None, None, 'narrow', None]),
}

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

new_player = Player('Dingus', room['outside'])
while True:
    print('Current room:', new_player.current_room.name, new_player.current_room.description)
    command = input('Choose a direction, n = north, e = east, s = south w = west, q for quit\n')
    if command == 'q':
        break
    if command in ['n', 's', 'e', 'w']:
        new_room = new_player.directions(command)
        if new_room != None:
            new_player.current_room = room[new_room]
        continue
"q\n"