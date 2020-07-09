from room import Room
from player import Player
#import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside",
                     """You find yourself in a garden with high walls of thorns and roses. 
                     Ahead of you, to the North, a door stands slightly ajar."""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """Dark shadows make parts of the room impossible to see.
    You can't tell if you're alone. """),
}


# Link rooms together

room['outside'].connections['n'] = room['foyer']
room['foyer'].connections['s']= room['outside']
room['foyer'].connections['n']= room['overlook']
room['foyer'].connections['e']= room['narrow']
room['overlook'].connections['s'] = room['foyer']
room['narrow'].connections['w'] = room['foyer']
room['narrow'].connections['n']= room['treasure']
room['treasure'].connections['s']= room['narrow']

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

# for line in textwrap.wrap(my_player.current_room.description):
#     print(line)

player_name = input('WELCOME TO THE CAVE OF HORRORS\n\nWhat is your name, brave adventurer?\n\n')
player = Player("Bob", room['outside'])

#at the beginning of every step, we need to state the room the player is in

#Logic for Movement
#while True:
#print(room.name)
#if input = "q" then:
#    halt completely 
#    user quits
#    #print a statement about quitting
#elif:
#    player_input='n':
#    player.current_room
#    player.move
#    move to n 
#    #should move them to foyer
#elif:
#    player_input='e':
#    move to e 
#    #from outside this will cause error message
#elif:
#    player_input='s':
#    move to s
#elif: 
#    player_input='w':
#    move to w 
#else:
#    commands=(player_input.split())
#    if:
#        commands[0]='take':
#        run player.take(item_name)
#    elif:
#        commands[0] ='drop':
#        run player.drop(item_name)

