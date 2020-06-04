from room import Room
from player import Player
import textwrap

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
def try_direction(player, direction):
    attribute = direction + '_to'
    if hasattr(player.location, attribute):
        player.location = getattr(player.location, attribute)
    else:
        print("There's nothing in that direction!")

# Make a new player object that is currently in the 'outside' room.

player = Player('Pete', room['outside'])

# Write a loop that:
while True:
    print("\n")
    print(player.location)

    first_char = input("\nChoose direction: ").strip().lower().split()
    
    first_first_char = first_char[0]

    first_char = first_first_char[0]

    if first_char[0] =='q':
        break

    if first_char[0] == 'n':
        try_direction(player, first_char)
    elif first_char[0] == 's':
        try_direction(player, first_char)
    elif first_char[0] == 'w':
        try_direction(player, first_char)
    elif first_char[0] == 'e':
        try_direction(player, first_char) 



#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# player = Player('Pete', room['outside'])
# print(player)

# d = input("Where do you want to go (Only way is north):")

# while True:
#     # print(player)
#     print(f"{player.location}")
#     d = input("Where do you want to go (Only way is north):")
#     print(f"You go {d}")
#     if d == 'n':
#         player.location = room['foyer']
#         print(f"{player.location}")
#         d = input("Where do you want to go (Choose: north, south or east):")
#         print(f"You go {d}")
#         if d == 'n':
#             player.location = room['overlook']
#             print(f"{player.location}")
#             d = input("Where do you want to go (Only way is south):")
#             print(f"You go {d}")
#         elif d == 's':
#             player.location = room['outside']
#             print(f"{player.location}")
#             d = input("Where do you want to go (Only way is north):")
#             print(f"You go {d}")
#         elif d == 'e':
#             player.location = room['narrow']
#             print(f"{player.location}")
#             d = input("Where do you want to go (Choose: north or west):")
#             print(f"You go {d}")
#     else:
#         print('You can only go north')
#         d = input("Where do you want to go (n, s, e, w):")