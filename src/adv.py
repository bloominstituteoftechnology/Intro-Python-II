from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north, east and west."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'passage1':   Room("Narrow Passage", """A narrow passage bends here from west
to north."""),

    'chamber': Room("Treasure Chamber", """You've found a small room with musty old chest in it. The only exit is to the south."""),

    'passage2':   Room("Wide Passage", """A wide passage stretches out before you.  You can't see the end of it. You think you see some faint light in the east."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['overlook'].s_to = room['foyer']
room['passage1'].n_to = room['chamber']
room['chamber'].s_to = room['passage1']
room['foyer'].e_to = room['passage1']
room['passage1'].w_to = room['foyer']
room['passage2'].e_to = room['foyer']
room['foyer'].w_to = room['passage2']
room['passage2'].w_to = room['passage2']


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

player_name = "Calli"
starting_room = room["outside"]
player = Player(player_name, starting_room)

while True:
    current_room = player.current_room

    print(f'You are now at the {current_room.name}\n')
    print(current_room.description)
    print("\nWhich direction would you like to move?")
    
    cmd = input("Enter 'n', 's', 'e', or 'w' ('q' to quit): ")

    if cmd == 'q':
        print("\nSee you again soon!\n")
        break
    
    if cmd == 'n':
        if hasattr(current_room, 'n_to'):
            print("\nWalking north...\n")
            player.current_room = current_room.n_to
        else:
            print("You cannot walk north from here. Please try another direction.")
    elif cmd == 's':
        if hasattr(current_room, 's_to'):
            print("\nWalking south...\n")
            player.current_room = current_room.s_to
        else:
            print("You cannot walk south from here. Please try another direction.")
    elif cmd == 'e':
        if hasattr(current_room, 'e_to'):
            print("\nWalking east...\n")
            player.current_room = current_room.e_to
        else:
            print("You cannot walk east from here. Please try another direction.")
    elif cmd == 'w':
        if hasattr(current_room, 'w_to'):
            print("\nWalking west...\n")
            player.current_room = current_room.w_to
        else:
            print("\nYou cannot walk west from here. Please try another direction.\n")
    else:
        print('\nInvalid input, please try again.\n')