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

lantern = Item('lantern', 'The light will guide you')
sword = Item('Sword','A dusty sword is better than no sword')
coins = Item('coins', 'oooh you have found some gold coins')

player = Player(input("""Please tell me your name:"""), room['outside'])
print(f'Thank you are you ready to begin, {player.name}')
print(player.current_room.description)

room['outside'].items.append(lantern)
room['foyer'].items.append(sword)
room['narrow'].items.append(coins)
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



game = 1

while True:

    command = input('Where would you like to move? choose from the following n for north, e for east s for south w for west, i for inventory, type take item name to take item or drop item name to drop and item or q (quit)')
    if command == 'n':
        player.move(command)

    elif command == 's':
        player.move(command)

    elif command == 'e':
        player.move(command)

    elif command == 'w':
        player.move(command)

    elif command == 'i':
        player.print_invent()

    elif command.startswith('take'):
        item = command.split(' ')[1]
        player.take_item(item)
        player.print_invent()
    
    elif command.startswith('drop'):
        item = command.split(' ')[1]
        player.drop_item(item)
        player.print_invent()

    elif command == 'q':

        print(f'Goodbye, {player.name}')
        break ## break exits the loop and sends it back to the start without break when we quit it will just say goodbye but loop back to the start
    else:
        print("You can't do that!")