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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Josh', room['outside'])
print(player1)
# Write a loop that:
# # * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
answer = input("would you like to play an adventure game(y/n): ")

if answer.lower().strip() == 'y':
    print("--Welcome to Tresure Hunt! You are in the outside room,\n--to find your way to the treasure,\n--you need to go to the foyer.")
    north = input("Type 'up' to go to foyer: ")
    if north.lower().strip() == 'up':
        """
        I have to move my player from current room to the next room based on connections
        """
        player1.current_room = player1.current_room.n_to
        print(f'Welcome to {player1.current_room}')
        north_2 = input("Type 'up' to go to overlook: ")
        if
        

elif answer.lower().strip() == 'n':
    print('the game will now quit')
    exit(0)


