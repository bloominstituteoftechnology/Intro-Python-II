from room import Room
from player import Player
from item import Item

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

# print(room)

# print(room)

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

# Players
player = Player("Thomas", room['outside'])

# Items
rock = Item("Rock", "This is a Rock")
sword = Item("Sword", "This is a Sword")
sheild = Item("Sheild", "This is a Sheild")

# Add Items to Rooms
room['outside'].inventory.extend([rock, sword, sheild])
room['foyer'].inventory.extend([rock, sword, sheild])
room['overlook'].inventory.extend([rock, sword, sheild])
room['narrow'].inventory.extend([rock, sword, sheild])
room['treasure'].inventory.extend([rock, sword, sheild])

# while loop

# Valid Directions
valid_directions = ["n", "e", "s", "w"]

# Current Room
print(f'Current Room:\n{player.current_room}\n')

def second_loop():
    item = ""
    while item is not "r":
        args = player.current_room.get_items_selector()
        player_inventory = player.get_items_selector()
        # print(f'player inventory:{player_inventory}')
        print(args)
        item = input(f"Aquire Item: [ {args} ] [ grab or drop ] or [r] to return => ")
        if item.find(" ") >= 0:
            cv = item.find(" ")
            # print(cv)
            item_value = item[:cv]
            item_command = item[cv+1:]
            # print(item_value)
            # print(item_command)
            if item_command == "grab" or item_command == "drop":
                if item_value in args:
                    # print(f"{item_command}ed item {item_value}")
                    player.handle_action(item_command, item_value)
                elif item_value in player_inventory:
                    # print(f"{item_command}ed item {item_value}")
                    player.handle_action(item_command, item_value)
                else:
                    print("Unacceptable Item Value! Try again.\n")
            else:
                print("Unacceptable Item Command! Try again.\n")
        elif item == "r":
            print("You choose not to pick up an item!")
            print(f'Current Room:\n{player.current_room}\n')
        else:
            print("Unacceptable Item Command! Try again.")

while True:
    cmd = input("Travel to: [n] [e] [s] [w], Grab/Drop an item: [gd] or [q] to quit => ")
    if cmd in valid_directions:
        player.travel(cmd)
    elif cmd == "gd":
        second_loop()
    elif cmd == "q":
        print("Goodbye!")
        break
    else:
        print("Unacceptable Command! Try again.\n")

