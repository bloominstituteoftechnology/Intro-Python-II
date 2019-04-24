from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("torch", "Lights your way.")]),

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

player = Player(room['outside'])

while True:
    print(f'\nCurrently: {player.current_room.name}')
    print(player.current_room.description)
    command = input("What would you like to do? ")

    if command == "north" or command == "n":
        try:
            player.current_room = player.current_room.n_to
        except:
            print("\nYou can't move north from.")
    elif command == "south" or command == "s":
        try: 
            player.current_room = player.current_room.s_to
        except:
            print("\nYou can't move south from here.")
    elif command == "east" or command == "e":
        try:
            player.current_room = player.current_room.e_to
        except:
            print("\nYou can't move east from here.")
    elif command == "west" or command == "w":
        try:
            player.current_room = player.current_room.w_to
        except:
            print("\nYou can't move west from here.")
    elif command == "look":
        print(f'\nLooking around you see: {items}')
    elif command == "q":
        break
    else:
        print("\nThat isn't a valid command, try again.")