from room import Room
from player import Player
from Item import Item
from Item import Weapon
from Item import Treasure

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
    "torch": Item("torch", "The torch is well-fashioned and will shine brightly for a long time."),
    "hatchet": Weapon("hatchet", "A small hatchet that can easily fit inside your belt loop. It can be used as a tool or a weapon.", 1),
    "coins": Treasure("coins", "They shines in the light.", 10),
    "emerald": Treasure("emerald", "It looks real.", 5)
}

outside_room.items = [items_dict["torch"]]
overlook_room.items = [items_dict["hatchet"]]
treausure_room.items = [items_dict["coins"], items_dict["emerald"]]


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

new_player = Player(room['outside'])

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

single_letter_cmds = ["n", "s", "e", "w", "q", "i", "inventory"]
split_cmds = ["take", "get", "drop"]
item_cmds = ["torch", "hatchet", "coins", "emerald"]

def change_room(direction):
    if direction == "n":
        if new_player.current_room.n_to == None:
            cmd = input("Invalid command. Please reread the room description and choose a different direction.\n--> ")
        else:
            new_player.current_room = new_player.current_room.n_to
    if direction == "s":
        if new_player.current_room.s_to == None:
            cmd = input("Invalid command. Please reread the room description and choose a different direction.\n--> ")
        else:
            new_player.current_room = new_player.current_room.s_to
    if direction == "e":
        if new_player.current_room.e_to == None:
            cmd = input("Invalid command. Please reread the room description and choose a different direction.\n--> ")
        else:
            new_player.current_room = new_player.current_room.e_to
    if direction == "w":
        if new_player.current_room.w_to == None:
            cmd = input("Invalid command. Please reread the room description and choose a different direction.\n--> ")
        else:
            new_player.current_room = new_player.current_room.w_to

def single_letter_cmd(single_letter_cmd):
    if cmd == "q":
        exit()
    elif cmd == "n":
        change_room("n")
    elif cmd == "s":
        change_room("s")
    elif cmd == "e":
        change_room("e")
    elif cmd == "w":
        change_room("w")

def split_cmd(cmd):
    if "take" in cmd:
        if "torch" in cmd and items_dict["torch"] in new_player.current_room.items:
            new_player.take_item(items_dict["torch"])
            new_player.current_room.lose_item(items_dict["torch"])
            items_dict["torch"].on_take()
        elif "hatchet" in cmd and items_dict["hatchet"] in new_player.current_room.items:
            new_player.take_item(items_dict["hatchet"])
            new_player.current_room.lose_item(items_dict["hatchet"])
            items_dict["hatchet"].on_take()
        elif "coins" in cmd and items_dict["coins"] in new_player.current_room.items:
            new_player.take_item(items_dict["coins"])
            new_player.current_room.lose_item(items_dict["coins"])
            items_dict["coins"].on_take()
        elif "emerald" in cmd and items_dict["emerald"] in new_player.current_room.items:
            new_player.take_item(items_dict["emerald"])
            new_player.current_room.lose_item(items_dict["emerald"])
            items_dict["emerald"].on_take()
        else:
            print(f"You can't take that. There is no {cmd.split()[1]} here.")
    elif "get" in cmd:
        if "torch" in cmd and items_dict["torch"] in new_player.current_room.items:
            new_player.take_item(items_dict["torch"])
            new_player.current_room.lose_item(items_dict["torch"])
            items_dict["torch"].on_take()
        elif "hatchet" in cmd and items_dict["hatchet"] in new_player.current_room.items:
            new_player.take_item(items_dict["hatchet"])
            new_player.current_room.lose_item(items_dict["hatchet"])
            items_dict["hatchet"].on_take()
        elif "coins" in cmd and items_dict["coins"] in new_player.current_room.items:
            new_player.take_item(items_dict["coins"])
            new_player.current_room.lose_item(items_dict["coins"])
            items_dict["coins"].on_take()
        elif "emerald" in cmd and items_dict["emerald"] in new_player.current_room.items:
            new_player.take_item(items_dict["emerald"])
            new_player.current_room.lose_item(items_dict["emerald"])
            items_dict["emerald"].on_take()
        else:
            print("You can't take that.")
    elif "drop" in cmd:
        if "torch" in cmd and items_dict["torch"] in new_player.items:
            new_player.drop_item(items_dict["torch"])
            new_player.current_room.get_item(items_dict["torch"])
            items_dict["torch"].on_drop()
        elif "hatchet" in cmd and items_dict["hatchet"] in new_player.items:
            new_player.drop_item(items_dict["hatchet"])
            new_player.current_room.get_item(items_dict["hatchet"])
            items_dict["hatchet"].on_drop()
        elif "coins" in cmd and items_dict["coins"] in new_player.items:
            new_player.drop_item(items_dict["coins"])
            new_player.current_room.get_item(items_dict["coins"])
            items_dict["coins"].on_drop()
        elif "emerald" in cmd and items_dict["emerald"] in new_player.items:
            new_player.drop_item(items_dict["emerald"])
            new_player.current_room.get_item(items_dict["emerald"])
            items_dict["emerald"].on_drop()
        else:
            print("You can't drop that.")


while True:
    print(new_player.current_room.name)
    print(new_player.current_room.description)
    if new_player.current_room.items != None:
        for item in new_player.current_room.items:
            print(f"You see a {item.name}.")
    cmd = input("--> ")
    if cmd not in single_letter_cmds and cmd not in item_cmds and cmd not in split_cmds:
        print(f"That command is not valid. Valid commands are: n, s, e, w, q, get, take, drop, i, inventory")
    if len(cmd.split()) > 1:
        split_cmd(cmd)
    elif cmd == "i" or cmd == "inventory":
        if len(new_player.items) > 0:
            for item in new_player.items:
                print(f"You have a {item.name}.")
        else:
            print("You currently have no items.")
    elif cmd in single_letter_cmds:
        single_letter_cmd(cmd)


