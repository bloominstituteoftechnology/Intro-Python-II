from room import Room, TreasureRoom
from player import Player
from item import Item

# Declare some lists of items
basic_items = [
    Item('Glove', 'A leather glove'),
    Item('Hat', 'A hat with a feather'),
    Item('Boot', 'An old leather boot')
]

magic_items = [
    Item('Bazooka', 'Kaboom'),
    Item('Gun', 'Brrrat, brrrat'),
    Item('Wand', 'Wait a wand?')
]

fruity_items = [
    Item('Banana', 'Yellow, curved, with a single bruise'),
    Item('Plantain', 'Green and curved'),
    Item('Mango', 'Yellow, orange and delicious')
]

# Declare all the rooms
room = {
    'outside':  TreasureRoom("Outside Cave Entrance",
                     "North of you, the cave mount beckons", fruity_items),

    'foyer':    TreasureRoom("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", basic_items),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': TreasureRoom("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", magic_items),
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

def main():
    
    print('Welcome to Lambda Quest')

    player = Player('Felix Peone')
    player.current_room = room['outside']

    while True:
        # printing the room name and description
        print(player.current_room)
        
        # checking if the room has the items attribute,
        # then checking if it is empty, and if not printing the items
        if hasattr(player.current_room, 'items'):
            if len(player.current_room.items) > 0:
                print('You see the following items: ')
                print(player.current_room.pstring_items())

        # Taking user input and processing it
        cmd = input('>> ')
        arg, itm = argument_parser(cmd)
        func = cmd_switch(arg)
        print(func(player, itm))

        #The conditional to break our loop, must remain at end of loop
        if cmd == 'q':
            break

def north(plyr, itm = None):
    toroom = plyr.current_room.n_to
    if toroom:
        plyr.current_room = toroom
        return 'You move to:'
    else:
        return 'There is nothing to the north of you.'
def south(plyr, itm = None):
    toroom = plyr.current_room.s_to
    if toroom:
        plyr.current_room = toroom
        return 'You move to:'
    else:
        return 'There is nothing to the south of you.'
def east(plyr, itm = None):
    toroom = plyr.current_room.e_to
    if toroom:
        plyr.current_room = toroom
        return 'You move to:'
    else:
        return 'There is nothing to the east of you.'
def west(plyr, itm = None):
    toroom = plyr.current_room.w_to
    if toroom:
        plyr.current_room = toroom
        return 'You move to:'
    else:
        return 'There is nothing to the west of you.'
def get(plyr, itm = None):
    if itm is None:
        # TODO left over from debuggin, shouldn't happen, consider removing
        return 'No such item exists'
    if hasattr(plyr.current_room, 'items'):
        if plyr.get_item(itm):
            # TODO I don't like this, rethink this
            return '----------------------------------------------------------'
        else:
            return f'{itm} not found.'
    else:
        return 'This room has no items'
def drop(plyr, itm = None):
    if itm is None:
        # TODO left over from debuggin, shouldn't happen, consider removing
        return 'No such item exists'
    if hasattr(plyr.current_room, 'items'):
        if plyr.drop_item(itm):
            # TODO I don't like this, rethink this
            return '----------------------------------------------------------'
        else:
            return f'{itm} not found in inventory.'
    else:
        return f'There is no place to drop the {itm}'
def inventory(plyr, itm = None):
    return plyr.check_inventory()
def quiter(plyr, itm = None):
    '''Accepts player object strictly for conformity'''
    return 'It has been fun. See you nex time.'
def error(plyr, itm = None):
    '''Accepts player object strictly for conformity'''
    err_msg = """Invalid command please use one of the following
---------------------------------------------------
'n' to travel north
's' to travel south
'e' to travel east
'w' to travel west
'get item' to take an item from a room
'drop item' to drop an item from your inventory
'i' or 'inventory' to check the player's inventory
'q' to quit the game
---------------------------------------------------
"""
    return err_msg

def cmd_switch(argument):
    '''
    A quick switch block for processing user input
    '''
    switcher = {
        'n': north,
        's': south,
        'e': east,
        'w': west,
        'q': quiter,
        'get': get,
        'take': get,
        'drop': drop,
        'i': inventory,
        'inventory': inventory
    }

    function = switcher.get(argument, error)

    # returning the reference to the function
    return function

def argument_parser(cmd):
    '''
    A quick helper function to check if there is a space in the user input
    '''
    if cmd.strip().count(' ') == 1:
        verb, item = cmd.strip().split()
        return (verb, item)
    else:
        return (cmd.strip(), None)


if __name__ == "__main__":
    main()
