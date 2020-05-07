import textwrap
from room import Room
from player import Player
import sys 

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

direction_commands = ['n', 's', 'e', 'w']
exit_commands = ['q', 'quit', 'exit']
help_commands = ['?', 'help']

valid_commands = direction_commands + exit_commands + help_commands
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
player = Player("Sean", room['outside'])

done = False

# helper function to skip input we don't understand
def skip_input():
    print("I don't understand that\n")

def print_help_text():
    print("""
    Valid commands:
        -[n]: move north
        -[s]: move south
        -[e]: move east
        -[w]: move west
        -[q]: quit
        -[help]: help text
    """)

# Write a loop that:
while not done:
    # * Prints the current room name
    print(player.location)
    # * Prints the current description (the textwrap module might be useful here).
    for line in textwrap.wrap(player.location.print_description()):
        print(line)
    print("\n")
    # * Waits for user input and decides what to do.
    command = input("What do you want to do? ")

    # check that the command is properly formatted
    if command not in valid_commands:
        skip_input()
        continue
    
    if command in direction_commands:
        player.location = player.move_to(command, player.location)
        continue
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    if command in exit_commands:
        done = True
        print("Exiting game!")
        sys.exit(0)

    if command in help_commands:
        print_help_text()
        continue

    else:
        skip_input()
        continue 
