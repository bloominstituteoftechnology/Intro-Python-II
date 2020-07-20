from room import Room
from player import Player
from item import Item

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

# Make a new player object that is currently in the 'outside' room.
player = Player("Jose JP Joe Joe", room['outside'])

# initialize items to rooms
room["foyer"].items = ["coins", "sword"]

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
user_is_playing = True
# welcome message
print("Welcome to the adventure game")

while user_is_playing:
    # print current room & room description
    print(f"Current room: {player.current_room.name}")
    for line in textwrap.wrap(player.current_room.description, width=200):
        print(line)
    # print out item list
    print(player.current_room)

    # get user input
    user_input = input(
        "Please choose [n]North, [s]South, [e]East  [w]West to MOVE, [i]Inventory [take item_name] Take an item, [drop item_name] Drop an item, or [q] Quit\n").lower().split(" ")

    # if user inputs 1 word
    if len(user_input) == 1:
        # if user inputs 1 of 4 directions
        if user_input[0] in ["n", "s", "e", "w"]:
            user_input[0] = f"{user_input[0]}_to"
            player.move(user_input[0])

        # if user inputs i for inventory
        if user_input[0] == "i":
            player.get_inventory()

        # if user inputs quit
        elif user_input[0] == "q":
            print("You exited the game. Thank you for playing!")
            user_is_playing = False

    # if user inputs 2 words
    elif len(user_input) == 2:
        # take item from a room
        if user_input[0] == "take" or user_input[0] == "get":
            # check room content to see if content is there
            for item in player.current_room.items:
                if item == user_input[1]:
                    player.take_item(user_input[1])
                else:
                    print("There is no such item in this room.")
        # drop item to a room
        elif user_input[0] == "drop":
            for item in player.inventory:
                if item == user_input[1]:
                    player.drop_item(user_input[1])
                else:
                    print(f"{player.name} doesn't have this item in inventory")
        else:
            print("Invalid entry. Please enter 'get' or 'drop' followed by the item. ")

    # else error message of not valid entry
    else:
        print("Invalid entry.")