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

# Make a new player object that is currently in the 'outside' room.
player = Player("Jose", room["outside"])

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

user_is_playing = True
#user will then get a welcome message 
print("Welcome to the Adventure Game 2020")

#loop starts here
while user_is_palying:
    #print current room and description
    print(player.curret_room)
    for line in textwrap.wrap(player.current_room.description, width=200):
        print(line)
    #take user input
    user_cmd = input(
        "[n] North   [s] South  [e] East  [w] West  [q] Quit\n").lower()
    print(f"You chose {user_cmd}")
    
    #user choose a cardinal direction
    #if user inputs q, quit the game 
    if user_cmd == "q":
        print("Bye, come back again")
        exit()
        
    #if user inputs 4 directions 
    
    #if the direction is available/not none then got to that room
    
    #else the option is not available/none then throw error and back to use input 
    
    #any other input will throw error