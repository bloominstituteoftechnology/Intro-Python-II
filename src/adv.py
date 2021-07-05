from room import Room
from room import PuzzleRoom
from player import Player
from character import Spider
from Item import Item
from Item import PuzzleItem
from Item import Treasure
from Item import LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", True),

    'overlook': PuzzleRoom("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. You see a rope going into the
wall by the south entrance and disappearing into a hole in the ground.""", "hatchet", "rope", False),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False),
    
    'door': Room("Heavy Door", """The passage ends at this heavy door. The smell
of gold is stronger than ever. The door holds firm and seems impossible to open.""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),
}


# Put rooms into properties for easier coding

outside_room = room['outside']
foyer_room = room['foyer']
overlook_room = room['overlook']
narrow_room = room['narrow']
treausure_room = room['treasure']

# Link rooms together

outside_room.n_to = room['foyer']
foyer_room.s_to = room['outside']
foyer_room.n_to = room['overlook']
foyer_room.e_to = room['narrow']
overlook_room.s_to = room['foyer']
narrow_room.w_to = room['foyer']
narrow_room.n_to = room['treasure']
treausure_room.s_to = room['narrow']

# Add items to rooms

items_dict = {
    "lamp": LightSource("lamp", "\nThe lamp looks well-fueled and should shine brightly for a long time.\n", 2),
    "hatchet": PuzzleItem("hatchet", "\nA small hatchet that can easily fit inside your belt loop. It can be used as a tool or a weapon.\n", 3),
    "coins": Treasure("coins", "\nThey shines in the light.\n", 2),
    "emerald": Treasure("emerald", "\nIt looks real.\n", 2)
}

narrow_room.items = [items_dict["lamp"]]
overlook_room.items = [items_dict["hatchet"]]
treausure_room.items = [items_dict["coins"], items_dict["emerald"]]


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

new_player = Player(input("What is your name?\n--> "), room['outside'])
spider = Spider(1, treausure_room ,True)

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

single_cmds = ["n", "s", "e", "w", "q", "quit", "i", "inventory", "help", "look"]
all_cmds = ["n", "s", "e", "w", "q", "i", "inventory", "take", "get", "drop", "look"]

def single_cmd(single_cmd):
    if cmd == "q" or cmd == "quit":
        print("Thanks for playing!")
        exit()
    elif cmd in ("n", "s", "e", "w"):
        new_player.travel(cmd)
    elif cmd == "i" or cmd == "inventory":
        new_player.display_inventory()
    elif cmd == "h" or cmd == "help":
        display_available_cmds()
    elif cmd == "look":
        new_player.look()

def split_cmd(cmd):
    if "take" in cmd or "get" in cmd:
        new_player.get_item(cmd.split(" ")[1])
    elif "drop" in cmd:
        new_player.drop_item(cmd.split(" ")[1])
    elif "look" in cmd:
        new_player.look_item(cmd.split(" ")[1])

def display_available_cmds():
    print(f"""Available commands are {all_cmds}.\nYou may interact with different items in the world using the commands take, get, drop and look. For example, you can say \"get lamp\" and your character will pick up a lamp.""")

new_player.current_room.__str__()

while True:
    cmd = input("--> ")
    if len(cmd.split()) > 1:
        split_cmd(cmd)
    elif cmd in single_cmds:
        single_cmd(cmd)
    spider.travel()


