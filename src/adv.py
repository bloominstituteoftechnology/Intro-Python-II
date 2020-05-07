from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "Dim light filters in from the south.\n"
                              "Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness.\n"
                                       "Ahead to the north, a light flickers in the distance,\n"
                                       "but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north.\n"
                                       "The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber!\n"
                                         "Sadly, it has already been completely emptied by earlier adventurers.\n"
                                         "The only exit is to the south."),
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
player = Player('Chad', room['outside'])

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

running = True

while running:
    print(f"\n{player.current_room.name}\n")
    print(player.current_room.description)

    command = input('\nWhere do you want to go? Enter (n, s, e, or w; q to quit): ')
    if command in ['q', 'quit', 'exit']:
        print("\nThanks for playing!\n")
        running = False
    elif command in ['?', 'help']:
        print("\nValid commands: ['n': North, 's': South, 'e': East,\n"
              "'w': West, 'q, quit, exit': Quit, '?, help': Help]\n")
    else:
        next_room = player.move_to(command)
        if next_room is None:
            print("\nNo room in this direction.\n")
        else:
            player.current_room = next_room
