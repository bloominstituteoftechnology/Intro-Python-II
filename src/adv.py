from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("in the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("in the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("in the Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("in the Treasure Chamber", """You've found the long-lost treasure
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
player = Player("Player 1", room['outside'])
# Write a loop that:
#
selection = 0
print(f"\n Welcome {player.name}! \n")
current_room = room['outside']
print(f'You are currently {player.current_room} \n')
while selection != "exit":
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
    selection = input("Enter direction to move >> ") # * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
    try: 
        if selection == "n" and current_room.n_to:
            current_room = current_room.n_to
            print(f'\n{current_room}')
        elif selection == "s" and current_room.s_to:
            current_room = current_room.s_to
            print(f'\n{current_room}')
        elif selection == 'w' and current_room.w_to:
            current_room = current_room.w_to
            print(f'\n{current_room}')
        elif selection == 'e' and current_room.e_to:
            current_room = current_room.e_to
            print(f'\n{current_room}')
        elif selection == 'c':
            print(f'\n{current_room}')

        else: 
            print("Please enter n, s, e, or w to move or enter c to see your current location")

    except: 
        print("That move isn't allowed please chose another direction. ") # Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.
