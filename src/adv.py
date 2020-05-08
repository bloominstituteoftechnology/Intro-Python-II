import textwrap
from room import Room
from player import Player
from item import Item 
import sys 

# create all valid user inputs 
direction_commands = ['n', 's', 'e', 'w']
exit_commands = ['q', 'quit', 'exit']
help_commands = ['?', 'help']
item_commands = ['get', 'drop', 'i']

valid_commands = direction_commands + exit_commands + help_commands + item_commands
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

    'graveyard': Room("Graveyard", """A dark mist prevents you from seeing more 
    than a few feet in front of you. The floor is littered with tiny bones."""),

    'lava':      Room("Lava", """A room filled with lava that will be harmful to 
    the player when the developers find time to make it so soon(TM)""")
}

# Declare all items

item = {
    'ring':     Item("Ring", "This old rusty ring has what looks to be a dragon wrestling a lion."),

    'box':      Item("Blossom", "An immaculately preserved flower from another age."),

    'fang':     Item("Fang", "A massive tooth from an unknown predator." ),
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
room['graveyard'].e_to = room['foyer']
room['foyer'].w_to = room['graveyard']
room['lava'].e_to = room['graveyard']
room['graveyard'].w_to = room['lava']


# Make a new player object that is currently in the 'outside' room.
player = Player("Mike", room['outside'])

done = False

# helper function to skip invalid inputs
def skip_input():
    print("I don't understand that!\n")

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
        print_help_text()
        continue
    
    if command in direction_commands:
        player.location = player.move_to(command, player.location)
        continue
    #
    if command == 'i':
       player.show_inventory()
        
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
