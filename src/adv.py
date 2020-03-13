from room import Room
from player import Player
from item import Item, Food
# Declare all the rooms
import sys
argv = sys.argv

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
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

# Make a new player object that is currently in the 'outside' room.
sandwich = Food('sandwich', 'a tasty treat', 100)
flashlight = Item('flashlight', 'a rusty flashlight. It works, though.')
sword = Item('sword', 'a dusty sword. well made, and it seems to glow a little..')
shield = Item('shield', 'a rusty kite shield with an old leather strap')
spyglass = Item('spyglass', 'a spyglass for seeing long distances')

player = Player(
    input("What is your name, noble adventurer? "),
    room['outside'])
print(f'Excellent! Your adventure begins here, {player.name}')
print(player.current_room.description)
player.items.append(sandwich)
room['outside'].items.append(flashlight)
room['foyer'].items.append(shield)
room['overlook'].items.append(spyglass)
room['treasure'].items.append(sword)

# proof of picking up items
# player.current_room.show_room_items()
# player.print_inventory()
# player.take_item(flashlight)
# player.print_inventory()
# player.current_room.show_room_items()

# player.take_item(flashlight)
# player.print_inventory()
# player.current_room.show_room_items()
# player.print_inventory()
# player.items.remove(sandwich)
# print(type(sandwich))
# player.current_room.items.append(sandwich)
# player.current_room.show_room_items()
# player.print_inventory()


while True:
    direction = input('~~>')
    if direction in ['n', 's', 'e', 'w']:
        player.move(direction)
    elif direction == 'i':
        player.print_inventory()
    elif direction.startswith('take'):
        item = direction.split(' ')[1]
        player.take_item(item)
        player.print_inventory()
    elif direction.startswith('drop'):
        item = direction.split(' ')[1]
        player.drop_item(item)
        player.print_inventory()
    elif direction == 'q':
        print(f'Farewell, {player.name}!')
        break
    else:
        print("You can't do that!")