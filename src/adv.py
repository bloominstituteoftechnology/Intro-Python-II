import sys
from room import Room
from player import Player
from item import Item
# from parser import parser

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    room_items=[
                        Item("Key [key]", "Appears to unlock something ...")
                    ]),

    'foyer': Room(
        "Foyer",
        """
        Dim light filters in from the south. Dusty
        passages run north and east.
        """,
        room_items=[
            Item(
                "Unopened Water Bottle [water]",
                "Lucky! Some drinking water!")
        ]),

    'overlook': Room(
        "Grand Overlook",
        """
        A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm.
        """,
        room_items=[
            Item("Skeleton [skeleton]", "An unlucky traveler ...")
        ]),

    'narrow': Room(
        "Narrow Passage",
        """
        The narrow passage bends here from west
        to north. The smell of gold permeates the air.
        """),

    'treasure': Room(
        "Treasure Chamber",
        """
        You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. The only exit is to the south.
        """,
        room_items=[
            Item(
                "Strange Map [map]",
                "A strange map ... does another adventure beckon!?")
        ]),
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


# To reference if item is in room
room["outside"].item_key = room["outside"].room_items[0]
room["foyer"].item_water = room["foyer"].room_items[0]
room["overlook"].item_skeleton = room["overlook"].room_items[0]
room["treasure"].item_map = room["treasure"].room_items[0]

# room["outside"].room_items[0].name #> Key


# Make a new player object that is currently in the 'outside' room.

player1 = Player("Mercedes", room['outside'])
print(f"Hello {player1.name}! Welcome to The Adventure Game ...")

choices = ["n", "s", "e", "w"]
objects = ["key", "skeleton", "water", "map"]

# Reference possible inventory items
# player1.inventory.item_key =

if __name__ == "__main__":

    # Write a loop that:
    while True:
        # * Prints the current room name and items
        print(f"\nYOUR CURRENT {player1.current_room}")
        print(player1.current_room.view_items())

        # View Player Inventory
        print(player1.view_inventory())

        # * Prints the current description (the textwrap module might be useful here).
        # print(f"\nLOCATION INFO: {player1.current_room.description}")

        # * Waits for user input and decides what to do.
        action = input(
            "Please enter a directional move (n, s, e or w; q to quit): ")

        # Rules for when command is a single word
        if len(action.split()) == 1:
            action = action.strip().lower().split()[0]
            action = action[0]

            # If the user enters a cardinal direction, attempt to move to the
            # room there.
            if action in choices:
                player1.try_direction(action)

            # Print an error message if the movement isn't allowed.
            elif action not in choices and action != "q":
                print("\nERROR: invalid movement")

            # If the user enters "q", quit the game.
            elif action == "q":
                sys.exit("\nThanks for playing!")

        # Rules for when command is multiple words
        elif len(action.split()) >= 2:
            action = action.strip().lower().split()
            # Ex. `get water`
            get_action = action[0]  # > `get`
            action_object = action[1]  # > `water`
            # action_object = action_object[0][0] #> `w`

            # If the user enters a get/take [item] command, attempt to add item
            # to player inventory
            if (get_action == "get" or get_action ==
                    "take") and action_object in objects:
                if len(player1.current_room.room_items) > 0:
                    # add item to player inventory
                    player1.add_to_inventory(action_object)
                    # remove item from room
                    player1.current_room.drop_item()
                    if len(player1.inventory) > 0:
                        # on take print out for most recently added item
                        print(player1.inventory[-1].on_take())
                    else:
                        print(player1.inventory[0].on_take())
                else:
                    print("\nIllegal operation - item has been picked up")

            # Usage message if invalid entry
            elif (get_action == "get" or get_action == "take") and action_object not in objects:
                print(
                    "\nUSAGE ERROR: pick up item with `get [item]`. water, key, skeleton or map")
                continue

            # If the user enters a drop [item] command, attempt to drop item in
            # current room
            elif get_action == "drop" and action_object in objects:
                # Loop into inventory
                for i in player1.inventory:
                    # grab item if object name string includes action_object
                    if action_object in i.name and len(player1.inventory) > 0:
                        item = i
                        player1.current_room.catch_item(item)
                        print(i.on_drop())
                    else:
                        print("USAGE ERROR: check inventory")
                # drop item from player inventory
                player1.drop_from_inventory(action_object)

            # Catchall for any other invalid entry
            else:
                print(
                    "\nUSAGE ERROR: pick up item with `get [item]`. water, key, skeleton or map")
                continue

        else:
            print("Please enter a command!")
            continue
