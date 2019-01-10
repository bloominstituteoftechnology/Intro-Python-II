from room import Room
from player import Player
from item import Item
import textwrap

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
earlier adventurers. The only exit is to the south.""", [Item('love', 'Foundation of all.'), Item('inspiration', 'Gift from above.'), Item('motivation', 'New perspective.')]),
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

player = Player(room['outside'])

"""
direction is the dicrectioin the user inputs
location is the current room the player is in

returns the new room that the player moves to if the
move was siccessful, or returns current room if 
the move was not
"""

def try_direction(direction, location):
    attribute = direction + '_to'

    # See if the inputted direction is one we can move to
    if hasattr(location, attribute):
        # fetch the new room
        return getattr(location, attribute)
    else:
        print('You can\'t go that way!')
        return location

# Write a loop that:
while True:
    # * Prints the current room name
    print('\n' + player.location.name)
    # * Prints the current description (the textwrap module might be useful here).
    for line in textwrap.wrap(player.location.description, 50):
        print(line)
    if len(player.location.item_list) > 0:
        print('\nItems in this room:\n')
        for item in player.location.item_list:
            print(item.name)
    else:
        print('\nThere are no items in this room.\n')

    print(f'\nPlayer inventory: {player.inventory}')
    # * Waits for user input and decides what to do.
    # command = input('\n>').lower()[0]

    command = input('\n> ').lower().split()

    if len(command) == 1:
        command = command[0]
        if command == 'q':
            print('See you next time!')
            break
        else:
            player.location = try_direction(command, player.location)
    elif len(command) == 2:
        verb = command[0]
        noun = command[1]

        location_item_list_names = [item.name for item in player.location.item_list]
        inventory_names = [item.name for item in player.inventory]

        if noun not in inventory_names + location_item_list_names:
            print('Item not found.')

        if verb in ['grab', 'get', 'take']:
            new_list = [item for item in player.location.item_list]
            for i in range(len(player.location.item_list)):
                if noun == player.location.item_list[i].name:
                    player.inventory.append(player.location.item_list[i])
                    new_list.remove(player.location.item_list[i])
                    player.location.item_list[i].on_take()
            player.location.item_list = new_list
            
        elif verb == 'drop':
            new_inventory_list = [item for item in player.inventory]
            for i in range(len(player.inventory)):
                if noun == player.inventory[i].name:
                    new_inventory_list.remove(player.inventory[i])
                    player.location.item_list.append(player.inventory[i])
                    player.inventory[i].on_drop()
            player.inventory = new_inventory_list
            
        else:
            print('\nI don\'t understand that.')
    else:
        print('I don\'t understand that.')
        continue




    if command == 'q':
        print('See you next time!')
        break


    # if command == 'q':
    #     break
    # elif command == 'n':
    #     player.location = player.location.n_to
    # elif command == 'e':
    #     player.location = player.location.e_to
    # elif command == 's':
    #     player.location = player.location.s_to
    # elif command == 'w':
    #     player.location = player.location.w_to
    # else:
    #     print('Not a valid direction!')

    """
    North, South, East, West, north, south, east, west
    N, S, E, W, n, s, e, w
    """
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
