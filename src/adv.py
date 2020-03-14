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
from item import Food, Medicine, Artifact, Weapon, Armor
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
# === Instantiate items === #
helmet = Armor("Helmet", "Protects the noggin", effect=9)
gauntlets = Armor("Gauntlets", "Protects the hands/wrists", effect=3)
boots = Armor("Boots", "Protects the feet/ankles", effect=4)
shield = Armor("Shield", "All around protection", effect=5)
sword = Weapon("Sword", "Good for close combat encounters", effect=6)
bow = Weapon("Bow", "Good for long-range attacks", effect=3, requires="Arrow")
arrow = Weapon("Arrow", "Missile shot by bow", effect=4, requires="Bow")
dagger = Weapon("Dagger", "Good for close quarters", effect=2)
potion1 = Medicine("Potion", "May help, may hurt", effect=-12)
potion2 = Medicine("Potion", "May help, may hurt", effect=-2)
potion3 = Medicine("Potion", "May help, may hurt", effect=20)
jerky = Food("Jerky", "A nice slab of jerky", effect=2)
gem1 = Artifact("Gem", "A sparkling gem", ability="confidence", effect=1)
gem2 = Artifact("Gem", "A sparkling gem", ability="confidence", effect=1)

# === Add items to rooms === #
room["outside"].add_item(helmet)
room["foyer"].add_item(gauntlets)
room["foyer"].add_item(arrow)
room["foyer"].add_item(potion2)
room["narrow"].add_item(sword)
room["narrow"].add_item(potion1)
room["overlook"].add_item(bow)
room["overlook"].add_item(jerky)
room["overlook"].add_item(potion3)
room["treasure"].add_item(shield)
room["treasure"].add_item(gem1)
room["treasure"].add_item(gem2)

# %%
# === Define the key commands === #
verbs = {
    "n": "move north",
    "s": "move south",
    "e": "move east",
    "w": "move west",
    "inv": "display inventory",
    "get": "add item to inventory",
    "take": "add item to inventory",
    "drop": "remove item from inventory",
    "q": "quit",
}

# %%
# ====== Main ====== #
def initiate_game(player_name: str, rooms: dict = room):
    """Initiates the bewilder REPL."""

    # Instantiate player, which prints initial room
    player = Player(player_name, rooms["outside"])

    while True:
        cmd = prompt(verbs).lower()  # Make lowercase
        cmd = cmd.split()  # Convert to list
        verb = cmd[0]  # Extract the verb
        if cmd[0] not in verbs:  # Filter out incorrect key commands
            print("Command not available...\nTry again.")
        elif cmd[0] == "q":  # Quit game upon pressing "q"
            print("Exiting game...")
            sys.exit(0)
        else:  # If command is valid, player takes action on it
            if len(cmd) == 1:  # Single commands
                if verb == "inv":  # Display inventory
                    player.inventory()
                else:  # Move player
                    # Look up destination room and move the player into it
                    verb = getattr(player.current_room, f"{verb}_to")
                    player.move(verb) if verb else print("No room in that direction!")
            else:
                # Allow for multiple items to be acted upon
                for obj in cmd[1:]:
                    if verb in ["get", "take"]:  # Pick up item
                        # Try to get the item object from the current_room's item dict
                        try:
                            item = player.current_room.items[obj]
                        except KeyError:
                            print("Item not available.")
                        finally:
                            player.add_item(item)
                    else:  # Drop item
                        try:
                            item = player.items[obj]
                        except KeyError:
                            print("Item not available to drop.")
                        finally:
                            player.rm_item(item)


# %%
initiate_game("jeopard")
