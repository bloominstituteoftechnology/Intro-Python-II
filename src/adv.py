from room import Room
from player import Player

# Declare all the rooms

outside = Room("Outside", "Outside Cave Entrance North of you, the cave mount beckons")

foyer = Room("Foyer", 'Dim light filters in from the south. Dusty passages run north and east.')

overlook = Room("Grand Overlook", 'A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.')

narrow = Room("Narrow Passage", 'The narrow passage bends here from west to north. The smell of gold permeates the air.')

treasure = Room("Treasure Chamber", 'You ve found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.')

# Link rooms together

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(outside)

# Write a loop that:
#

done = False
while not done:
    current_room = player.current_room
    print(current_room)

    user_input = input('Enter a command: ')
    # exiting the program
    if user_input == 'q':
        done = True

    if user_input == 'w':
        if current_room.w_to:
            player.current_room = current_room.w_to
    elif user_input == 'e':
        if current_room.e_to:
            player.current_room = current_room.e_to
    elif user_input == 's':
        if current_room.s_to:
            player.current_room = current_room.s_to
    elif user_input == 'n':
        # move to new room
        # check if room exists to north
        if current_room.n_to:
            player.current_room = current_room.n_to

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.