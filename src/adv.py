# Global Imports
import os
import textwrap

# Local Imports
from room import Room
from player import Player
from item import Item

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

# Declare Player
player = Player('Chosen One', room['outside'])

# Centers Header Text

#
# Intro
#

# Clear Screen
clear = lambda: os.system('cls')
clear()


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

player_name = input('Please enter your name: ')
player.name = player_name

print(chr(27) + "[2J") # Scroll screen down so that the next loop begins at the top of the screen.

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

while True:

    # Room Name
    print(f'Location: {player.location.name} \n')

    # Room Description
    print(f'Description: {player.location.description}')
    

    # Main Input - Convert to Lowercase
    print('________________________________________________________________________________')
    command = input("Enter Command Here: ")
    command = command.lower()

    #
    # Commands --------------------------------------------------------------------------------
    #

    #
    # System Commands
    #

    # Commands to Quit Game
    if command in ["q", "quit", "esc", "end"]:
        break
    
    #
    # Movement Commands
    #     

    print(chr(27) + "[2J") # Scroll screen down so that the next loop begins at the top of the screen.