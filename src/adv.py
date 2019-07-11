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
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Items & assoc rooms
rock = Item("rock", "This is a rock")
sword = Item("sword", "This is a sword")
pencil = Item("pencil", "This is a pencil")
burger = Item("burger", "This is a hamburger")
watch = Item("watch", "This is a watch")
bike = Item("bike", "This is a bike")

room["outside"].items.append(rock)
room["foyer"].items.append(sword)
room["overlook"].items.append(pencil)
room["narrow"].items.append(burger)
room["treasure"].items.append(watch)
room["outside"].items.append(bike)

initial_room = room["outside"]
name = input("Enter your name: ")
player = Player(name, initial_room)
print(player)

while True:
    print(f'Your current inventory: {player.inventory}')

    action = input("Do you want to 'get x' an item or 'drop x' an item: ")
    detail = action.split(" ")

    if detail[0] not in ["get", "drop"]:
        pass
    elif detail[0].lower() == "get":
        item = player.current_room.get_item(detail[1])
        if item == None:
            print("That item is not in the room.")
        else:
           player.current_room.items.remove(item)
           player.inventory.append(item)
           item.on_take()
    elif detail[0].lower() == "drop":
        item = player.get_item(detail[1])
        if item == None:
            print("That item is not in your inventory.")
        else:
            player.current_room.items.append(item)
            player.inventory.remove(item)
            item.on_drop()

    direction = input("Please input a direction 'n'/'s'/'e'/'w' or 'q' to end: ")

    if direction in ['n', 's', 'e', 'w']:
        player.move(direction)
    elif direction == 'q':
        break
    else:
        print("==>>Invalid direction<<==")

print("See ya!")
