from room import Room
from player import Player
from item import Item

# Declare all the rooms
# We're going to need a REPL that prints the name and description of the player's current room
    # REPL:
    # R - Read the user input
    # E - Evaluate your code
    # P - Print any results
    # L - Loop back to step 1

items = {
    "jacket":  Item("Jacket", "It's cold, wear this to warm yourself up"),
    "lantern":  Item("Lantern", "Use this to illuminate the way"),
    "telescope": Item("Telescope", "Get a birds eye view"),
    "money": Item("money", "You found some gold. The treasure must be near"),
    "paperclip": Item("paperclip", "This is all that was left")
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", items["jacket"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items["lantern"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items["telescope"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items["money"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items["paperclip"]),
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

player = Player("You", room["outside"])

# Welcome message for when the user starts up the game
print("\nWelcome to the Adventure game! Will you be able to find the treasure?")
print("The controls are simple. N for North, S for South, E for east, W for West. Press Q at anytime to quit the game.\n")
# North, South, East, West
moves = ["n", "s", "e", "w"]


# goggles = Item("night vision goggles", "It's dark, these will help you see better")

while True:

    print(f"\n{player.current_room}")

    command = input("\nWhich direction would you like to go? ").strip().lower().split()[0]
    command = command[0]

    if command == 'q':
        break

    if command in moves:
        player.try_direction(command)

    if player.current_room.items != None:
        print(f"\nYou see a {player.current_room.items.name}\n")
        grab_item = input("Would you like to pick up the item? (y/n): ").lower()
        if grab_item == "y" or grab_item == "yes":
            player.pickup_item(player.current_room.items)
            player.current_room.items = None
            print("\nSuccessfully added to your inventory")
