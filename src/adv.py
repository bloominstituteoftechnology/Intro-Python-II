from room import Room
from player import Player

titlecard = """
 ██▓███ ▓██   ██▓   ▓█████▄  █    ██  ███▄    █   ▄████ ▓█████  ▒█████   ███▄    █ 
▓██░  ██▒▒██  ██▒   ▒██▀ ██▌ ██  ▓██▒ ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒ ██ ▀█   █ 
▓██░ ██▓▒ ▒██ ██░   ░██   █▌▓██  ▒██░▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒██░  ██▒▓██  ▀█ ██▒
▒██▄█▓▒ ▒ ░ ▐██▓░   ░▓█▄   ▌▓▓█  ░██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██   ██░▓██▒  ▐▌██▒
▒██▒ ░  ░ ░ ██▒▓░   ░▒████▓ ▒▒█████▓ ▒██░   ▓██░░▒▓███▀▒░▒████▒░ ████▓▒░▒██░   ▓██░
▒▓▒░ ░  ░  ██▒▒▒     ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░▒ ░     ▓██ ░▒░     ░ ▒  ▒ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
░░       ▒ ▒ ░░      ░ ░  ░  ░░░ ░ ░    ░   ░ ░ ░ ░   ░    ░   ░ ░ ░ ▒     ░   ░ ░ 
         ░ ░           ░       ░              ░       ░    ░  ░    ░ ░           ░ 
         ░ ░         ░                                                             
"""

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        "Dim light filters in from the south. Dusty passages run north and east.",
    ),
    "overlook": Room(
        "Grand Overlook",
        "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.",
    ),
    "narrow": Room(
        "Narrow Passage",
        "The narrow passage bends here from west to north. The smell of gold permeates the air.",
    ),
    "treasure": Room(
        "Treasure Chamber",
        "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Brace", room["outside"])


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

running = True
directions = ["north", "east", "south", "west"]
direction_attr = {"north": "n_to", "east": "e_to", "south": "s_to", "west": "s_to"}
incomplete_actions = {
    "go": "Go where? Please specify north, east, south, or west.",
    "take": "Take what?",
}


def Check_Direction(direction):
    if direction.casefold() in directions:
        return direction
    else:
        return False


def Move_Player(player, direction):
    valid_dir = Check_Direction(split_inp[0])
    if not valid_dir:
        print("Not a valid direction, adventurer.")
        return
    else:
        next_room = getattr(player.current_room, direction_attr[valid_dir])
        if next_room == None:
            print(f"You cannot go {valid_dir} from here.")
            return
        else:
            player.current_room = next_room
            print(f"{next_room}")


print(f"\u001b[38;5;190m{titlecard}\033[0m")
print(f"\n{player.current_room}")
while running:
    inp = input("> ").casefold().strip()

    if "quit" in inp or inp == "q":
        print("Safe travels, adventurer")
        running = False
        break

    split_inp = inp.split(" ", 1)

    if len(split_inp) < 2:
        action = split_inp[0]
        valid_dir = Check_Direction(action)
        if valid_dir:
            Move_Player(player, valid_dir)
        else:
            print(incomplete_actions.get(action, f"{action} what now?"))
    elif len(split_inp) > 1:
        action, subject = split_inp[0], split_inp[1]
        if action == "go":
            Move_Player(player, subject)

