import os
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

# Add items to rooms
room["foyer"].add_item(Item("sword", "a magical sword"))
room["foyer"].add_item(Item("ring", "a magical ring"))

room["overlook"].add_item(Item("lamp", "a magical lamp"))
room["overlook"].add_item(Item("potion", "a magical potion"))
room["overlook"].add_item(Item("hammer", "a magical hammer"))

room["narrow"].add_item(Item("food", "a magical food"))
room["narrow"].add_item(Item("book", "a magical book"))
room["narrow"].add_item(Item("key", "a magical key"))
room["narrow"].add_item(Item("shield", "a magical shield"))

#
# Main
#


def prompt(message):
    print(f">> {message}")


def location_info():
    prompt(f"You are in the {player.current_room.name}\n")
    prompt(f"{player.current_room.desc}\n")
    prompt(f"Found items: {player.current_room.print_items()}\n")


def direction_error(direction):
    if direction == "n":
        prompt("No way North!\n")
    elif direction == "e":
        prompt("No way East!\n")
    elif direction == "s":
        prompt("No way South!\n")
    elif direction == "w":
        prompt("No way West!\n")


def command_error():
    prompt("I don't quite understand\n")


def print_commands():
    prompt(
        f"""Commands:
        N - go to North
        E - go to East
        S - go to South
        W - go to West

        get [item] - to get an item
        drop [item] - to drop an item
        i or inventory - to show inventory

        Q - to quit game
        """
    )


def try_direction(direction, current_room):
    attribute = direction + "_to"

    # See if the inputted direction is one we can move to
    if hasattr(current_room, attribute):
        # fetch the new room
        return getattr(current_room, attribute)
    else:
        direction_error(direction)
        return current_room


def validate_item_in_room(item):
    room_items = player.current_room.list_items
    return any(i.name == item for i in room_items)


def validate_item_in_inventory(item):
    player_items = player.list_items
    return any(i == item for i in player_items)


def item_action(action, item):
    room_items = player.current_room.list_items
    player_items = player.list_items
    room = player.current_room

    if action == "get":
        # get item
        player.get_item(item)

        for i in room_items:
            if i.name == item:
                # remove item from room
                player.current_room.remove_item(i)

        prompt(f"Got {item}!\n")
    else:
        # drop item
        if len(player_items) > 0:
            player.drop_item(item)
            prompt(f"Dropped {item}! You can't get it back, sorry.\n")
        else:
            prompt(f"You don't have anything to drop.\n")


# Make a new player object that is currently in the 'outside' room.
player_name = input("Enter player name: ")
player = Player(player_name, room["outside"])
# player.current_room => room["outside"]

os.system("cls" if os.name == "nt" else "clear")

# Initial prompt of the game
welcome_title = f"Welcome to the Text Adventure Game, {player.name}!"
prompt(welcome_title)
prompt("=" * len(welcome_title))
prompt(f"You are now in the {player.current_room.name}\n")
prompt(f"{player.current_room.desc}\n")
prompt('Type "help" for commands.\n')

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

while True:
    command = input(f"What do you want to do, {player.name}? ").lower().split()
    # => returns a list

    os.system("cls" if os.name == "nt" else "clear")

    if len(command) == 1:
        command = command[0]
        prompt(f"command: {command}\n")

        # Make player move NESW
        if command in ["n", "s", "e", "w"]:
            player.current_room = try_direction(command, player.current_room)
        elif command == "help":
            print_commands()
        elif command == "i" or command == "inventory":
            prompt(f"Inventory: {player.list_items}\n")
        elif command == "q":
            break
        else:
            command_error()
    elif len(command) == 2:
        first_word = command[0]
        second_word = command[1]

        if first_word in ["get", "drop"]:
            if validate_item_in_room(second_word) or validate_item_in_inventory(
                second_word
            ):
                item_action(first_word, second_word)
            else:
                prompt(f"There's no item called {second_word}\n")
        else:
            command_error()
    else:
        command_error()

    location_info()


prompt("Thank you for playing!\n")
