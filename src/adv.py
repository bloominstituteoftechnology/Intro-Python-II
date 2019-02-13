from room import Room
from item import Item
from player import Player
from data import room as room, item as item, player as player

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

# add items to rooms:
room["narrow"].items.append(item["sword"])
room["narrow"].items.append(item["shield"])
room["foyer"].items.append(item["armor"])
room["foyer"].items.append(item["helmet"])
room["overlook"].items.append(item["boots"])
# print(item["sword"])
# print(room["narrow"].items)
# print(room["outside"])
# print(room["narrow"].items[0])

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


# for r in room:
#     print(room[r])

# for i in item:
#     print(item[i])

# print(f'{room["outside"].name}')
##
# print(player)
# print(player.room.name)
# print(player.room.description)

# print(room)
# print(room["outside"].print_room)
