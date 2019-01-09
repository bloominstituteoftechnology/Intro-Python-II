# Global Imports
import os
import textwrap

# Local Imports
from location import Location
from player import Player
from item import Item

# Declare all the locations

location = {
    'outside':  Location("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Location("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Location("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Location("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Location("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link locations together

location['outside'].n_to = location['foyer']
location['foyer'].s_to = location['outside']
location['foyer'].n_to = location['overlook']
location['foyer'].e_to = location['narrow']
location['overlook'].s_to = location['foyer']
location['narrow'].w_to = location['foyer']
location['narrow'].n_to = location['treasure']
location['treasure'].s_to = location['narrow']

# Declare Player
player = Player('Chosen One', location['outside'])

# Centers Header Text

#
# Intro
#

# Clear Screen
clear = lambda: os.system('cls')
clear()

# Enter to Continue
def enter_to_continue():
    input('--\nPress Enter to Continue...')

print(r'''   
             /\    
            /  \   
           / /\ \  
          / /  \ \ 
         /_/    \_\

Welcome to Lambda Adventure! 
============================
''')

player_name = input('Please enter your name: ')
player.name = player_name

print(chr(27) + "[2J") # Scroll screen down so that the next loop begins at the top of the screen.

print(r'''   
             /\    
            /  \   
           / /\ \  
          / /  \ \ 
         /_/    \_\

Welcome to Lambda Adventure! 
============================

Please enter your commands below. 

Enter 'q' to quit the game.
---
''')

#
# Main
#

# Make a new player object that is currently in the 'outside' location.

# Write a loop that:
#
# * Prints the current location name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the location there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:

    # Location Name
    print(f'Location: {player.location.name} \n')

    # Location Description
    print(f'Description: {player.location.description}')
    

    # Main Input + Convert to Lowercase and a List
    print('________________________________________________________________________________')
    command = input("Enter Command Here: ")
    command = command.lower().split(" ", 1)

    # Define Command Action
    command_action = command[0]

    if len(command) == 1:
        command_object = ""
    else:
        command_object = command[1]

    #
    # Commands --------------------------------------------------------------------------------
    #

    #
    # System Commands
    #

    # Commands to Quit Game
    if command_action in ("q", "quit", "esc", "end"):
        break
    
    #
    # Movement Commands
    #

    move_commands = ("walk", "go", "move", "travel", "venture", "proceed", "n", "s", "e", "w")
    move_directions = {
        'north': ("northward", "north", "n"),
        'south': ("southward", "south", "s"),
        'east': ("eastward", "east", "e"),
        'west': ("westward", "west", "w")
    }
    
    # Movement Error Message
    def invalid_direction():
        print(chr(27) + "[2J") # Scroll screen down so that the next loop begins at the top of the screen.
        print('You are unable to see a way to move in that direction!')
        enter_to_continue()

    # Check if Command Was a Movement Command
    if command_action in move_commands:
        
        # Check Movement Type and Whether Movement is Valid
        
        # North
        if command_action == "n" or command_object in move_directions['north']:
            if hasattr(player.location, 'n_to'):
                player.location = player.location.n_to
            else:
                invalid_direction()

        # South 
        elif command_action == "s" or command_object in move_directions['south']:
            if hasattr(player.location, 's_to'):
                player.location = player.location.s_to
            else:
                invalid_direction()

        # East
        elif command_action == "e" or command_object in move_directions['east']:
            if hasattr(player.location, 'e_to'):
                player.location = player.location.e_to
            else:
                invalid_direction()

        # West
        elif command_action == "w" or command_object in move_directions['west']:
            if hasattr(player.location, 'w_to'):
                player.location = player.location.w_to
            else:
                invalid_direction()
        
        else:
            invalid_direction()

    print(chr(27) + "[2J") # Scroll screen down so that the next loop begins at the top of the screen.