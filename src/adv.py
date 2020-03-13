"""
BeWilder - a *wild* text adventure game :: Main game module

# Make a new player object that is currently in the 'outside' room.

Write a loop that:

- Prints the current room name
- Prints the current description (the textwrap module might be useful here).
- Waits for user input and decides what to do.
    - If the user enters a cardinal direction, attempt to move to the room there.
    - Print an error message if the movement isn't allowed.
    - If the user enters "q", quit the game.
"""

# %%
import sys

from adv_utils import justify_center, table_printer, prompt, link_rooms
from item import Item, Food, Artifact, Weapon, Armor
from room import Room
from player import Player

# %%
# === Declare all the rooms === #
room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons."),
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

# %%
# === Link rooms together === #
room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

# %%
# === Define the key commands === #
verbs = {
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
    "q": "quit",
}

# %%
# === Add items to rooms === #
item1 = Item("Thing1", "This is one thing")
item2 = Item("Thing2", "This is two thing")
item3 = Item("Thing3", "This is three thing")
item4 = Item("Thing4", "Another thing")
room["outside"].add_item(item1)
room["foyer"].add_item(item2)
room["foyer"].add_item(item3)
room["foyer"].add_item(item4)

# %%
player = Player("jeopard", room["outside"])
player.get_item(item1)

# %%
# ====== Main ====== #
def initiate_game(player_name: str, rooms: dict = room):
    """Initiates the bewilder REPL."""

    # Instantiate player, which prints initial room
    player = Player(player_name, rooms["outside"])

    while True:
        cmd = prompt(verbs).lower()
        if cmd not in verbs:  # Filter out incorrect key commands
            print("Command not available...\nTry again.")
        elif cmd == "q":  # Quit game upon pressing "q"
            print("Exiting game...")
            sys.exit(0)
        else:  # If command is valid, player takes action on it
            player.take_action(cmd)


# %%
initiate_game("jeopard")
