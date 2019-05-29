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

outside_room.items = [Item("Torch", "The torch is well-fashioned and will shine brightly for a long time.")]
overlook_room.items = [Weapon("Hatchet", "A small hatchet that can easily fit inside your belt loop. It can be used as a tool or a weapon.", 1)]
treausure_room.items = [Treasure("Gold Coin", "It shines in the light.", 1), Treasure("Emerald", "It looks real.", 5)]


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

single_letter_cmds = ["n", "s", "e", "w", "q"]


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
    if cmd == "n":
        change_room("n")
    if cmd == "s":
        change_room("s")
    if cmd == "e":
        change_room("e")
    if cmd == "w":
        change_room("w")



while True:
    print(new_player.current_room.name)
    print(new_player.current_room.description)
    if new_player.current_room.items != None:
        for item in new_player.current_room.items:
            print(f"You see a {item.name}.")
    cmd = input("--> ")
    if cmd in single_letter_cmds:
        single_letter_cmd(cmd)

