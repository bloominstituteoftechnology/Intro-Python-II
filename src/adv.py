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

# Creating Items


sword = Item("Sword", "This is a sword. *Shwing*")

room['outside'].addItem(sword)

#
# Main
#


# Make a new player object that is currently in the 'outside' room.

player = Player(room["outside"])


def try_direction(direction, location):
    attribute = direction + "_to"

    if hasattr(location, attribute):

        return getattr(location, attribute)

    else:
        print(
            "\n - You can't head in that direction - \n")
        return player.location

# Write a loop that:


while True:

    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).

    print(
        "\n " + f"Your Location: {player.location.title} \n \n     {player.location.description} \n\n  Items in room: {player.location.items} \n  Inventory: {player.items}")

    # * Waits for user input and decides what to do.
    inp = input(
        "\n Enter a direction or pick up an item from the current room >").lower().split()
    # If the user enters a cardinal direction, attempt to move to the room there.

    print("---------------------------------------------------------------")

    if len(inp) == 1:

        inp = inp[0][0]

        if inp == "q":
            break

        player.location = try_direction(inp, player.location)

    elif len(inp) > 1 and (inp[0] == "get" or inp[0] == "take"):
        itemToGet = player.location.findItemByName(inp[1])
        if itemToGet is not None:
            player.addItem(itemToGet)
            player.location.removeItem(itemToGet)
            print(f" \n You picked up : {inp[1]}")
        else:
            print(f"\n There is no {inp[1]} here.")

    elif len(inp) > 1 and (inp[0] == "drop" or inp[0] == "remove"):
        itemToGet = player.findItemByName(inp[1])
        if itemToGet is not None:
            player.removeItem(itemToGet)
            player.location.addItem(itemToGet)
        else:
            print(
                f"\n You have nothing in your inventory by the name of {inp[1]} ")
