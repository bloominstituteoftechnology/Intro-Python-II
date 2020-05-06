from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons ..."),

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
new_player = Player(player_name = "Ryan", current_room = room["outside"])


print("\nWelcome player! You may enter a direction in which to travel with n, s, e, w, and q to quit the game.\n")
print(f"{new_player.player_name} is {new_player.current_room} \n")

# Write a loop that:
while True: 
# * Prints the current room name
    
# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
    selection = input("Enter a direction or Q to escape: ")
    if selection == "q": 
        print("Have a good day. Thanks for playing.")
        break
    elif selection == "n" or selection == "s" or selection == "e" or selection == "w":
        new_player.move(selection)
        print(f"\n{new_player.player_name} is {new_player.current_room.room_name} \n{new_player.current_room.description}\n\n")
    else:
        print("That is not a proper command.")
# If the user enters a cardinal direction, attempt to move to the room there.

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
