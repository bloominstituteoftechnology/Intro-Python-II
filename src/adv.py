from room import Room
from player import Player
from item import Item, Weapon, Healing


# Declare all items

item = {
    'sword1': Weapon("Rusty Sword", "A rusty sword but still sturdy enough to swing.", 2),
    'sword2': Weapon("Sword", "A basic looking sword, perhaps left here by a less fortunate adventurer.", 5),
    'healing1': Healing("Bandage", "A basic stip of cloth use to patch wounds.", 3),
    'healing2': Healing("Potion", "A vial of Red liquid used to heal wounds.", 5),
    'coins': Item("Pile of Gold", "A small pile of gold coins used to buy items")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['sword2', ]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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
player = Player(input('Please Enter your name: '), room['outside'], [item['sword1'], item['coins']])
print('Hello, ', player.name)
print(player.current_room)
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

while 1:
    command = input(">").split(" ")
    if command == 'q':
        break
    elif command[0] in ('n', 's', 'e', 'w'):
        player.travel(command[0])
    elif command[0] == 'drop':
        if(len(command) > 0):
            if player.drop_item(command[1]):
                player.current_room.add_item(command[1])
        else:
            print("No item under that name.")
    elif command[0] in ('get', 'take'):
        if(len(command) > 1):
            if player.current_room.remove_item(command[1]):
                player.pickup_item(command[1])
        else:
            print("No item under that name.")
    elif command[0] == 'i':
        player.show_inventory()
    else:
        print("I can't do that", player.name)