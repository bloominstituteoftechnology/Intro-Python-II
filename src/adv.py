from room import Room
from player import Player

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

player_name = "David"
starting_room = room["outside"]
player = Player(player_name, starting_room)

while True:
    current_room = player.current_room

    print(f'You are now in room: {current_room.name}\n')
    print(current_room.description)
    print("\nWhich direction would you like to move?")
    
    cmd = input("Enter 'n', 's', 'e', or 'w' ('q' to quit): ")

    if cmd == 'q':
        print("\nThanks for playing! Goodbye.\n")
        break
    
    if cmd == 'n':
        if hasattr(current_room, 'n_to'):
            print("\nMoving North...\n")
            player.current_room = current_room.n_to
        else:
            print("You cannot move North from here. Please try another direction.")
    elif cmd == 's':
        if hasattr(current_room, 's_to'):
            print("\nMoving South...\n")
            player.current_room = current_room.s_to
        else:
            print("You cannot move South from here. Please try another direction.")
    elif cmd == 'e':
        if hasattr(current_room, 'e_to'):
            print("\nMoving East...\n")
            player.current_room = current_room.e_to
        else:
            print("You cannot move East from here. Please try another direction.")
    elif cmd == 'w':
        if hasattr(current_room, 'w_to'):
            print("\nMoving West...\n")
            player.current_room = current_room.w_to
        else:
            print("\nYou cannot move West from here. Please try another direction.\n")
    else:
        print('\nInvalid input, please try again.\n')