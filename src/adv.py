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

# set up variables
wants_to_quit = False
player = Player(room['outside'])

# Move command, will handle move attempts
def go(dir):
    """
    dir values:
    0: north
    1: east
    2: south
    3: west
    """
    # print('Moving in direction',dir)

    # grab current room connections
    conns = [
        player.cur_room.n_to,
        player.cur_room.e_to,
        player.cur_room.s_to,
        player.cur_room.w_to
    ]

    if conns[dir] is not None:
        player.cur_room = conns[dir]
    else:
        print("You can't go that way.")

def ph():
    print(
        """n, e, s, w: travel north, east, south, and west respectively.
q: quit the game
?: prints the controls. (you are here)"""
    )

# action table, deals with 
def act(command):
    if   command == 'n': # go north
        go(0)
    elif command == 'e': # go east
        go(1)
    elif command == 's': # go south
        go(2)
    elif command == 'w': # go west
        go(3)
    elif command == '?': # get help
        ph()
    elif command == 'q': # quit game
        global wants_to_quit
        wants_to_quit = True
    else:
        print("You don't know how to do that.")


# Initial printing
ph()
print()

# REPL game loop
while not wants_to_quit:
    # print("quitting:",~wants_to_quit)
    print(player.cur_room.name)
    print(player.cur_room.desc)

    comm = input("Command: ")

    act(comm)

    # spacing
    print()
