from room import Room
from room import PuzzleRoom
from player import Player
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
    "lamp": Item("lamp", "The lamp is well-fueled and will shine brightly for a long time.", 2),
    "hatchet": PuzzleItem("hatchet", "A small hatchet that can easily fit inside your belt loop. It can be used as a tool or a weapon.", 3),
    "coins": Treasure("coins", "They shines in the light.", 2),
    "emerald": Treasure("emerald", "It looks real.", 2)
}

narrow_room.items = [items_dict["lamp"]]
overlook_room.items = [items_dict["hatchet"]]
treausure_room.items = [items_dict["coins"], items_dict["emerald"]]


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

new_player = Player(input("What is your name?\n--> "), room['outside'])

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
item_cmds = ["lamp", "hatchet", "coins", "emerald"]
puzzle_cmds = ["use", "with"]

def change_room(direction):
    if direction == "n":
        if new_player.current_room.n_to == None:
            cmd = input("You can't do that. Please reread the room description and choose a different direction.\n--> ")
        else:
            new_player.current_room = new_player.current_room.n_to
    elif direction == "s":
        if new_player.current_room.s_to == None:
            cmd = input("You can't do that. Please reread the room description and choose a different direction.\n--> ")
        else:
            new_player.current_room = new_player.current_room.s_to
    elif direction == "e":
        if new_player.current_room.e_to == None:
            cmd = input("You can't do that. Please reread the room description and choose a different direction.\n--> ")
        else:
            new_player.current_room = new_player.current_room.e_to
    elif direction == "w":
        if new_player.current_room.w_to == None:
            cmd = input("You can't do that. Please reread the room description and choose a different direction.\n--> ")
        else:
            new_player.current_room = new_player.current_room.w_to

def single_letter_cmd(single_letter_cmd):
    if cmd == "q":
        print("Thanks for playing!")
        exit()
    elif cmd in ("n", "s", "e", "w"):
        new_player.travel(cmd)

def split_cmd(cmd):
    if "take" in cmd:
        if items_dict["lamp"] not in new_player.items and new_player.current_room.is_light == False and items_dict["lamp"] not in new_player.current_room.items:
            print("Good luck finding that in the dark!")
        elif "lamp" in cmd and items_dict["lamp"] in new_player.current_room.items:
            new_player.take_item(items_dict["lamp"])
            new_player.current_room.lose_item(items_dict["lamp"])
            items_dict["lamp"].on_take()
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
        if items_dict["lamp"] not in new_player.items and new_player.current_room.is_light == False and items_dict["lamp"] not in new_player.current_room.items:
            print("Good luck finding that in the dark!")
        elif "lamp" in cmd and items_dict["lamp"] in new_player.current_room.items:
            new_player.take_item(items_dict["lamp"])
            new_player.current_room.lose_item(items_dict["lamp"])
            items_dict["lamp"].on_take()
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
        if "lamp" in cmd and items_dict["lamp"] in new_player.items:
            new_player.drop_item(items_dict["lamp"])
            new_player.current_room.get_item(items_dict["lamp"])
            items_dict["lamp"].on_drop()
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
    if items_dict["lamp"] in new_player.items or new_player.current_room.is_light == True or items_dict["lamp"] in new_player.current_room.items:
        print(new_player.current_room.name)
        print(new_player.current_room.description)
        if new_player.current_room.items != None:
            for item in new_player.current_room.items:
                print(f"You see a {item.name}.")
    elif items_dict["lamp"] not in new_player.items and new_player.current_room.is_light == False:
        print("It's pitch black!")
    cmd = input("--> ")
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


