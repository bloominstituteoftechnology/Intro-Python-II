from room import Thee_Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Thee_Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Thee_Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Thee_Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Thee_Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Thee_Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
 
# Outside
room['outside'].n_to = room['foyer']
# Overlook
room['overlook'].s_to = room['foyer']
# Foyer
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
# Narrow
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
# Treasure
room['treasure'].s_to = room['narrow']


# print(type(room["outside"]))
# print(room["outside"].n_to)
# room["outside"].n_to = 5
# print(room["outside"].n_to)  ---------This is an example dont ask me how to use it though

move_map = {
    "n": "n_to",
    "s": "s_to",
    "e": "e_to",
    "w": "w_to" 
}

chocolate = Item("chocolate", "a piece of candy to fill up your tummy")
watch = Item("watch", "an old watch used to tell time")
dirtymap = Item("dirtymap", "a dirty map of some island with the word Lambda at the bottom. ")
coin = Item("coin", "a golden coin. A golden with Latin writing and a picture of Sir Francis Duke.")
sodapop = Item("sodapop", "a small can of tiki punch soda. A great source of sugar.")

room['foyer'].items.append(chocolate)
room['foyer'].items.append(watch)
room['overlook'].items.append(dirtymap)
room['narrow'].items.append(sodapop)
room['treasure'].items.append(coin)
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


player_1 = Player("Majin Buu", room["outside"])

# while True:
#     print("\n\n")
#     print(f"The current room you are in is: {player_1.current_room.name}")
#     print(player_1.current_room.description)
#     user_input = input("Please enter move direction ")
#     if user_input in move_map.keys():
#         try:
#             player_1.current_room = getattr(
#             player_1.current_room, move_map[user_input])
#         except AttributeError:
#             print("There is no room in that direction")
#     elif user_input == "q":
#         quit()

while True:

    quit = player_1.input_instructions()

    if quit == True:
        break
        
        



