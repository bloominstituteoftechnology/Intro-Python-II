
from room import Room
from player import Player
from item import Item
import csv
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
earlier adventurers. The only exit is to the south."""),
}

wrapper = textwrap.TextWrapper(width=70)

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Define items from the item_src list
item_list = {}

with open('item_src.txt', 'r') as f:
    for line in f:
        data = eval(line)
        item_list[data['id']] = Item(data['name'], data['description'])

# Establish items in rooms
foyer_items = [item_list['bronzesword'], item_list['giraffestatuette']]
room['foyer'].add_items(foyer_items)

#
# Main
#

# Takes in a list of item names and returns a list of the associated ids
def name_to_id(names):
    split = names.split(',')
    base = ''
    for item in split:
        base = base + "'"+item.replace(' ','').lower()+"',"
    return eval("["+base+"]")

# Helper function to check current room's items and return a string 
# which can be printed based on what it finds

        
# Make a new player object that is currently in the 'outside' room.
player_name = input('Enter a name for your character: ')
p1 = Player(player_name, room['outside'])

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
while(True):
    # Determine current room
    c_room = p1.current_room

    # Print Buffer space to make it easier to read
    print('')
    print('-'*70)

    # Print current Location and location description/items
    print('Current Room: {}'.format(c_room.name))
    [print(line) for line in wrapper.wrap(text=c_room.description)]
    item_str = 'Items in room:\t{}'.format(c_room.check_items())
    [print(line) for line in wrapper.wrap(text=item_str)]

    # Input from user
    inp = input('What would you like to do? ')

    # Print buffer to make it easier to read
    print('-'*70)
    
    # Preprocess input
    inputs = inp.split(maxsplit=1)

    # Process Input
    if(len(inputs) == 1):
        inp = inputs[0]
        if(inp in ['q', 'quit', 'exit']):
            break
        elif(inp in ['n','e','s','w']):
            p1.move_player(inp)
        if(inp in ['i', 'inventory']):
            print('Inventory:')
            [print(line) for line in p1.get_items()]

    elif(len(inputs) == 2):
        verb, obj = inputs[0], inputs[1]
        if(verb in ['take', 'grab', 'get']):
            # Generate list of target item's id's from input
            targ_items = name_to_id(obj)
            # Attempt to remove target items from room
            removed_items_ids, removed_items = c_room.remove_items(targ_items)
            # Add items to player inventory
            p1.add_items(removed_items)
            # Print items that were actually given to player
            added_items = [item.name for item in removed_items]
            print('Items added: {}'.format(added_items))

        elif(verb in ['remove', 'drop', 'toss']):
            # Generate list of target item's id's from input
            targ_items = name_to_id(obj)
            # Attempt to remove target items from room
            removed_items = p1.remove_items(targ_items)
            # Add items to player inventory
            items = {id:item for id in removed_items}
            c_room.add_items(removed_items)
            # Print items that were removed from the player
            added_items = [item.name for item in removed_items]
            print('Items removed: {}'.format(added_items))

    else:
        print('Invalid Input')