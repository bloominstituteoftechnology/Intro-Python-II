import sys
import time
from room import Room
from player import Player
from items import Item

# controls main game loop
done = False

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("stick", "a small stick, perhaps useful for crafting a torch"), Item("rock", "a primitive but effective home defense tool")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("lamp", "an old, disused lamp that's run out of fuel"), Item("dagger", "a rusty shiv")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("rope", "a short rope, too short to use for climbing, but perhaps useful for other purposes?"), Item("chain", "a heavy chain")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("cannister", "a bent up fuel cannister, still a few drops left")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("goblet", "a shimmering golden goblet"), Item("necklace", "a jewel-encrusted necklace w/ cryptic engravings")]),
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

player = Player("jess", room['outside'])

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


def help():
    print("\n### NAVIGATION COMMANDS ###")
    print("west or w - travel west")
    print("east or e - travel east")
    print("north or n - travel north")
    print("south or s - travel south")
    print("\n### ITEM COMMANDS ###")
    print("take, grab, get [item name] - pick up an item")
    print("drop, toss, discard [item name] - drop an item\n")
    print("\n### GAME OPTIONS ###")
    print("q, quit, exit - exit the game")
    time.sleep(3)


def navigation(choice):
    try:
        if choice == "q" or choice == "quit" or choice == "exit":
            global done
            done = True
        elif choice == "n" or choice == "north":
            player.current_room = player.current_room.n_to
        elif choice == "s" or choice == "south":
            player.current_room = player.current_room.s_to
        elif choice == "e" or choice == "east":
            player.current_room = player.current_room.e_to
        elif choice == "w" or choice == "west":
            player.current_room = player.current_room.w_to
        elif choice == "help" or choice == "instructions" or choice == "man":
            help()
        else:
            print(
                "Invalid selection - valid inputs are 'n', 's,', 'e', 'w' directions or 'q' to quit")
    except:
        print("\n**** Can't go further in this direction! Try another. ****\n")


def item_interaction(choice):
    action, item = choice

    try:
        if action == "take" or action == "grab" or action == "get":
            for i in player.current_room.items:
                if i.name == item:
                    #pylint: disable=maybe-no-member 
                    player.pickup_item(i)
                    player.inventory[-1].on_take()

        elif action == "drop" or action == "toss" or action == "discard":
            #pylint: disable=maybe-no-member 
            for i in player.inventory:
                if i.name == item:
                    player.drop_item(i)
                    player.inventory[-1].on_drop()
        else:
            print("\nInvalid command - enter 'help' for a list of commands")
    except:
        print("\nItem not available - refer to the list of items in the current room.")


def display_room_items():
    if len(player.current_room.items):
        print("\nYou see the following items:")
        print(*player.current_room.items, sep="\n")
    else:
        print("\nThe room before you contains no useful items")


def display_player_inventory():
    #pylint: disable=maybe-no-member 
    if len(player.inventory):
        print("\nYou are carrying the following items:")
        print(*player.inventory, sep="\n")
    else:
        print("\nYou have no items in your inventory")
    time.sleep(5)

def display_current_location():
    print("\n----------------------------------------------\n")
    print("Current Location: " + player.current_room.name)
    print("\nDescription: " + player.current_room.description)


while done != True:
    display_current_location()
    display_room_items()
    choice = input("\nWhat will you do? ").split(" ")

    if (len(choice) == 1 and choice[0] != "i" and choice[0] != "inventory"):
        navigation(choice[0])
    elif (choice[0] == "i" or choice[0] == "inventory"):
        display_player_inventory()
    else:
        item_interaction(choice)