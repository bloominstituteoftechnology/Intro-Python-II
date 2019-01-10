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
    prompt(f"You are now in the {player.current_room.name}\n")
    prompt(f"{player.current_room.desc}\n")
    prompt(f"Found items: {player.current_room.print_items()}\n")


def direction_error():
    prompt("There's no way out here")


def print_commands():
    prompt(
        f"""Commands:
        N - go to North
        E - go to East
        S - go to South
        W - go to West
        """
    )


# Make a new player object that is currently in the 'outside' room.
player_name = input("Enter player name: ")
player = Player(player_name, room["outside"])
# player.current_room => room["outside"]

prompt(f"Welcome {player.name}, you are now in the {player.current_room.name}")
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
    command = input("What do you want to do? (q to quit): ").lower()

    # Make player move NESW
    if command == "n":
        if hasattr(player.current_room, "n_to"):
            player.current_room = player.current_room.n_to
            location_info()
        else:
            direction_error()
    elif command == "e":
        if hasattr(player.current_room, "e_to"):
            player.current_room = player.current_room.e_to
            location_info()
        else:
            direction_error()
    elif command == "s":
        if hasattr(player.current_room, "s_to"):
            player.current_room = player.current_room.s_to
            location_info()
        else:
            direction_error()
    elif command == "w":
        if hasattr(player.current_room, "w_to"):
            player.current_room = player.current_room.w_to
            location_info()
        else:
            direction_error()
    elif command == "help":
        print_commands()
    elif command == "q":
        break
    else:
        prompt("I don't quite understand")


prompt("Thank you for playing!")
