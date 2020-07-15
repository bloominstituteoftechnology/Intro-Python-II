from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("outside cave entrance",
                     "North of you, the cave mouth beckons"),

    'entrance':    Room("entrance", """Dim light filters in from the south. Dusty
passages run north, east and west."""),

    'cliff': Room("steep cliff", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'passage1':   Room("narrow passage", """A narrow passage bends here from west
to north."""),

    'chamber': Room("empty chamber", """You've found a small room with musty old chest in it. The only exit is to the south."""),

    'passage2':   Room("wide passage", """A wide passage stretches out before you. You can't see the end of it. You think you see some faint light in the east."""),
}


# Link rooms together

room['outside'].n_to = room['entrance']
room['entrance'].s_to = room['outside']
room['entrance'].n_to = room['cliff']
room['cliff'].s_to = room['entrance']
room['passage1'].n_to = room['chamber']
room['chamber'].s_to = room['passage1']
room['entrance'].e_to = room['passage1']
room['passage1'].w_to = room['entrance']
room['passage2'].e_to = room['entrance']
room['entrance'].w_to = room['passage2']
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

player_name = input("\nPlease enter your name\n")
starting_room = room["outside"]
player = Player(player_name, starting_room)

while True:
    current_room = player.current_room

    print(f'You are now at the {current_room.name}.\n')
    print(current_room.description)
    print("\nWhich direction would you like to move?")
    
    cmd = input("Enter 'n', 's', 'e', or 'w' ('q' to quit): ")

    if cmd == 'q':
        print(f'\nThanks for playing, {player_name}. See you again soon!\n')
        break
    
    if cmd == 'n':
        if hasattr(current_room, 'n_to'):
            print("\nWalking north...\n")
            player.current_room = current_room.n_to
        else:
            print(f'\nSorry, {player_name}, you cannot walk north from here. Please try another direction.\n')
    elif cmd == 's':
        if hasattr(current_room, 's_to'):
            print("\nWalking south...\n")
            player.current_room = current_room.s_to
        else:
            print(f'\nSorry, {player_name}, you cannot walk south from here. Please try another direction.\n')
    elif cmd == 'e':
        if hasattr(current_room, 'e_to'):
            print("\nWalking east...\n")
            player.current_room = current_room.e_to
        else:
            print(f'\nSorry, {player_name}, you cannot walk east from here. Please try another direction.\n')
    elif cmd == 'w':
        if hasattr(current_room, 'w_to'):
            print("\nWalking west...\n")
            player.current_room = current_room.w_to
        else:
            print(f'\nSorry, {player_name}, you cannot walk west from here. Please try another direction.\n')
    else:
        print('\nInvalid input, please try again.\n')