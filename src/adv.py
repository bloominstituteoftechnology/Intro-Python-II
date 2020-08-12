import sys
from room import Room
from player import Player
from player import player_info
from items import items

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

   'hall': Room("A hallway", """Dim light filters in from the south. Dusty
passages run north and east.""" ),

   'study': Room("A study", """Dim light filters in from the south. Dusty
passages run north and east.""" ),

   'stairs': Room("Some stairs, don't fall", """Dim light filters in from the south. Dusty
passages run north and east."""),

   'kitchen': Room("A kitchen", """Dim light filters in from the south. Dusty
passages run north and east.""" ),

   'bathroom': Room("A bathroom", """Dim light filters in from the south. Dusty
passages run north and east."""),

   'bedroom': Room("A bedroom", """Dim light filters in from the south. Dusty
passages run north and east."""),


}

# room['bathroom'].e_to = room['bedroom']
# room['bedroom'].w_to = room['bathroom']
# room['bedroom'].s_to = room['hall']
# room['hall'].n_to = room['bedroom']
# room['study'].n_to = room['hall']
# room['hall'].s_to = room['study']
# room['stairs'].e_to = room['hall']
# room['hall'].w_to = room['stairs']
# room['stairs'].s_to = room['foyer']
# room['foyer'].n_to = room['stairs']
# room['stairs'].w_to = room['foyer']
# room{'foyer'}.s_to = room['final_door']


# I guess I should number doors....?


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

Player("outside", player_info)

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

trapped = True

while trapped:

    movement = input("Enter n, s, w, e, or q to quit:")

    print(movement)
    
    def switch(movement) :
        if movement == 'n' or movement=='N':
            Room.n_to()
        elif movement =='s' or movement=='S':
            Room.s_to()
        elif movement == 'w' or movement=='W':
            Room.w_to()
        elif movement == 'e' or movement=='E':
            Room.e_to()
        elif movement == 'q' or movement=='Q':
            trapped = False
            sys.exit()
        else:
            print("Please be sure to enter n, s, e, w, or q")

    switch(movement)