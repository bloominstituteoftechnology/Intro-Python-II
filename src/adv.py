from room import Room
from player import Player
from item import Item
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

"""
  | V | T
  | F _ N
  | O |
"""

fork = Item("Fork", "An eating utensil")
axe = Item("Axe", "A beat up old battle axe")
torch = Item("Torch", "An unlit torch")
match = Item("Match", "A match for starting a fire")

room['outside'].items = []
room['foyer'].items = [torch]
room['overlook'].items = [match]
room['narrow'].items = [axe, fork]
room['treasure'].items = []

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_1 = Player(room["outside"])
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

def get_room_choice(player):
    print(player.current_room)
    direction_choice = input("Which direction would you like to go? (n, s, e, w or q to quit) ").lower()
    if direction_choice == "n":
        player.try_north()
        get_room_choice(player)
    elif direction_choice == "s":
        player.try_south()
        get_room_choice(player)
    elif direction_choice == "e":
        player.try_east()
        get_room_choice(player)
    elif direction_choice == "w":
        player.try_west()
        get_room_choice(player)
    elif direction_choice == "q":
        print("Bye!")

get_room_choice(player_1)

