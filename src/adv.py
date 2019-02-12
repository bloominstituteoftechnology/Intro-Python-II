from room import Room
from item import Item
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ""),
}

# Declare all items

item = {
    'sword': Item("excalibur", "pretty cool sword"),

    "shield": Item("hylian shield", "pretty sturdy shield"),

    "boots": Item("leather boots", "a pair of pretty fashionable boots"),

    "armor": Item("tunic", "a pretty weird looking suit"),

    "helmet": Item("crown", "pretty regal looking headpiece")
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

player = Player(room["outside"])

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


for r in room:
    # print(f'room name: {room[r].name}, description: {room[r].description} \n')
    print(room[r])

# print(f'{room["outside"].name}')
print(player)
print(player.room.name)
print(player.room.description)

# print(room)
# print(room["outside"].print_room)
