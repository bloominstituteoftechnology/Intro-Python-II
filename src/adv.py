from room import Room
from player import Player
import textwrap

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


def move_in_dir(direction):
    current_room = player.get_current_room()

    # Check if player can move in direction given
    if direction == 'n' and current_room.n_to:
        player.set_current_room(current_room.n_to)
        return True
    elif direction == 's' and current_room.s_to:
        player.set_current_room(current_room.s_to)
        return True
    elif direction == 'e' and current_room.e_to:
        player.set_current_room(current_room.e_to)
        return True
    elif direction == 'w' and current_room.w_to:
        player.set_current_room(current_room.w_to)
        return True

    return False


# Make a new player object that is currently in the 'outside' room.
player = Player('Shreyas')
player.set_current_room(room['outside'])

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

direction_cmd = ['n', 's', 'e', 'w']

while True:

    print(f'{player.current_room.name}\n')
    for text in textwrap.wrap(player.current_room.desc):
        print(text)

    cmd = input("Please provide your input: ")

    if cmd == 'q':
        print('Nice game. Visit again.')
        break
    elif cmd.lower() in direction_cmd:
        if not move_in_dir(cmd.lower()):
            print('Moving in this direction is not allowed.')
            continue
    else:
        print('Input invalid.')
        print('n - To move North')
        print('s - To move South')
        print('e - To move East')
        print('w - To move West')
        print('q - To quit')
