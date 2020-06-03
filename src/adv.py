from game import Game
from room import Room
from room import KeyedRoom
from item import Item
from item import CursedItem
from player import Player


cursed_key = CursedItem("blood-stained key", "A key that may or may not be cursed")
coins = Item("coins", "Shiny gold coins")
sword = Item("sword", "A shiny golden sword")

# Declare all the rooms
rooms = {
    "outside": Room(
        "Outside Cave Entrance", """North of you, the cave mouth beckons."""
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.
A groan eminates from the west.""",
    ),
    "curse": Room(
        "Cursed Room",
        """You're not sure how you know it,
but this room is definitely cursed.
The entrance is to the east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": KeyedRoom(
        "Treasure Chamber",
        """You've found the long-lost
treasure chamber! The only exit is to the south.""",
        cursed_key,
    ),
}

rooms["curse"].items_list.append(cursed_key)
rooms["treasure"].items_list.append(coins)
rooms["treasure"].items_list.append(sword)

# Link rooms together

rooms["outside"].n_to = rooms["foyer"]
rooms["outside"].n_to = rooms["foyer"]
rooms["foyer"].s_to = rooms["outside"]
rooms["foyer"].n_to = rooms["overlook"]
rooms["foyer"].e_to = rooms["narrow"]
rooms["foyer"].w_to = rooms["curse"]
rooms["curse"].e_to = rooms["foyer"]
rooms["overlook"].s_to = rooms["foyer"]
rooms["narrow"].w_to = rooms["foyer"]
rooms["narrow"].n_to = rooms["treasure"]
rooms["treasure"].s_to = rooms["narrow"]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(rooms["outside"])

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

game = Game(player, rooms)
game.start()
