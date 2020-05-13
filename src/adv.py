from room import Room

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
from player import Player
bash = Player("Bash", room['outside'])

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

selection =  ""

directions = """
The path splits ahead. Choose a direction:
    n. North
    e. East
    s. South
    w. West
"""

def move_player(player, room):
    player.move_to(room)

while selection != "q":
    currentroom = bash.currentroom
    print(currentroom)
    selection = input(directions)
    try:
        if selection == "n":
            move_player(bash, currentroom.n_to)
        elif selection == "e":
            move_player(bash, currentroom.e_to)
        elif selection == "s":
            move_player(bash, currentroom.s_to)
        elif selection == "w":
            move_player(bash, currentroom.w_to)
        else:
            print('Choose a valid direction.')
    except AttributeError:
        print('There is no path in that direction')

print("Thanks for playing!")