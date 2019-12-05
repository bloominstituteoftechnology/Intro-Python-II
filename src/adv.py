from room import Room
from player import Player
from item import Item


# Declare all the rooms
item = {
    'light': Item("light"),
    'enos_key': Item("enos_key"),
    'chamber_key': Item("chamber_key")
}

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


# Link rooms together
room['outside'].n_to = room['foyer']

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']

room['overlook'].s_to = room['foyer']

room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']

room['treasure'].s_to = room['narrow']


# Add items to rooms
# for r in room:
#     print(room[r].name)
room['overlook'].items.append(item['light'])
room['narrow'].items.append(item['chamber_key'])


# Set dark room
room['narrow'].is_dark = True


# Set locked room
room['treasure'].is_locked = True


# Make a new player object that is currently in the 'outside' room.
name = input("Enter Name ->")
player = Player(name, room['outside'])


#
# Main
#

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

print("ROOM NAME", room["foyer"].n_to.name)
print("PLAYER CURR ROOM", player.curr_room)

while True:
    print("CURRENT LOCATION NAME", player.curr_room.name)
    print("CURRENT LOCATION DESC", player.curr_room.desc)
    cmd = input(" -> ")
    split_cmd = cmd.split(" ")
    if split_cmd[0] == "q":
        break
    elif split_cmd[0] == "n":
        player.move_n()
    elif split_cmd[0] == "s":
        player.move_s()
    elif split_cmd[0] == "w":
        player.move_w()
    elif split_cmd[0] == "e":
        player.move_e()

    elif split_cmd[0] == "view":
        if len(split_cmd) == 2:
            if split_cmd[1] == "items":
                player.curr_room.view_items()
            elif split_cmd[1] == "inventory":
                player.view_inventory()
            else:
                print("Incorrect command")
        else:
            print("Missing command")

    elif split_cmd[0] == "take":
        if len(split_cmd) == 2:
            player.take_item(split_cmd[1], player.curr_room)
        else:
            print("Missing command")

    elif split_cmd[0] == "drop":
        if len(split_cmd) == 2:
            player.drop_item(split_cmd[1], player.curr_room)
        else:
            print("Missing command")
    else:
        print("incorrect commands")



# data is everywhere
# need to refactor, better handling of conditionals
  # dark room, items in room, items in inventory, adding/removing items

  