from room import Room
from player import Player
from item import Gold
from item import Food

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Food('banana', 'is a bit bruised', 20), Gold(100)]),

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
room['outside'].north_to = room['foyer']
room['outside'].n_to = room['foyer']
room['foyer'].south_to = room['outside']
room['foyer'].s_to = room['outside']
room['foyer'].north_to = room['overlook']
room['foyer'].n_to = room['overlook']
room['foyer'].east_to = room['narrow']
room['foyer'].e_to = room['narrow']
room['overlook'].south_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].west_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].north_to = room['treasure']
room['narrow'].n_to = room['treasure']
room['treasure'].south_to = room['narrow']
room['treasure'].s_to = room['narrow']

#
# Main
#


def tryDirection(d, curRoom):

    attrib = d + '_to'

    # curRoom.s_to
    # hasattr(currRoom, 's_to) will return true
    if hasattr(curRoom, attrib):
        return getattr(curRoom, attrib)
    else:
        print("You cant go that way")

    return curRoom


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
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

done = False

while not done:
    print('\nWelcome to my adventure game! In this game you will choose which direction you want to go from room to room. In the terminal please type either n or north, s or south, w or west, or e or east. To exit type q or quit. Thank you!')
    print(f'\n{player.curRoom.name}\n')
    print(f'{player.curRoom.description}')

    # print room items
    for item in player.curRoom.items:
        print(item)
        print(item.inspect())

    user_input = input("\nType direction to go: ").strip().lower().split()

    if len(user_input) != 1:
        print('I dont understand that. Type n,s,w, or e')
        continue

    if user_input[0] == 'quit' or user_input[0] == 'q':
        done = True

    elif user_input[0] in ["n", "north", "s", "south", "w", "west", "e", "east"]:
        player.curRoom = tryDirection(user_input[0], player.curRoom)

    else:
        unknown_input = user_input[0]
        print('Unknown command: ', unknown_input)
