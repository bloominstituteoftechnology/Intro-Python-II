from room import Room
from player import Player
from item import Item

# Declare all the rooms
sword = Item("sword", "This sword has no function whatsoever")
compass = Item("compass", "You seriously need a compass?")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [sword, compass]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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
directions = ['n', 's', 'e', 'w']
player = Player(room['outside'], [])

while True:
    print("\n")
    print(player.current_room.name)
    print("\n")
    print(player.current_room.description)
    print("\n")
    
    user_input = input('Where would you like to go? >>>').strip().lower().split()
    num_words = len(user_input)

    if num_words == 1:
        user_input = user_input[0]
        if user_input == 'q':
            print('Thanks for playing!')
            break
        elif user_input in directions:
            player.move(user_input)
    elif num_words == 2:
        verb = user_input[0]
        verb_item = user_input[1]
        if verb == 'get' or verb == 'take':
            player.add_item(verb_item)
        elif verb == 'drop':
            player.drop_item(verb_item)
    else:
        print("Whoops, enter a valid command like: n, s, e, w")