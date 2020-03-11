from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

# Declare Items     >> 10 items

shoe = Item("shoe", "smelly", "1")
book = Item("book", "leather", "1")
knife = Item("knife", "sparkly", "1")
fish = Item("fish", "kinda gross", "2")
apple = Item("apples", "sleepy", "10")
spoon = Item("spoons", "rusty", "2")
mote = Item("motes", "wistful", "5,000")
coin = Item("coins", "dull", "2")
bar = Item("bars", "shiny", "5")
pizza = Item("pizza", "probably ok", "1")

# Link Items to Rooms

room["outside"].items = [shoe, book]
room["foyer"].items = [fish, knife]
room["overlook"].items = [apple, spoon]
room["narrow"].items = [mote, coin]
room["treasure"].items = [bar, pizza]

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

player_one = Player("Player", room["outside"])

directions = ["n", "e", "s", "w"]
actions = ["get", "drop"]

print(f"\n{player_one}")

while True:

    move = (
        input(
            "Move around with 'n', 'e', 's', or 'w'\nPick up/Drop items with 'get' & 'drop\nQuit with 'q'\n"
        )
        .lower()
        .split()
    )

    if move[0] == "q":
        print("\nBuh Bye\n")
        break

    elif len(move) == 1 and move[0] in directions:
        player_one.change_room(move[0])

    elif len(move) == 2 and move[0] == "get":
        player_one.item_add(move[1])

    elif len(move) == 2 and move[0] == "drop":
        player_one.item_remove(move[1])

    elif move[0] == "bag":
        player_one.get_items()

    else:
        print("\nPlease enter a valid command\n")
