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

# Add items to rooms
# Note: item names (first param) must be all lowercase

room['treasure'].items.append(
    Item('coin',
    'A gold coin, leftover from the treasure taken long ago.')
)

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

# set up variables
wants_to_quit = False
player = Player(input("What is your name? "), room['outside'])

# Move command, will handle move attempts
def go(dir):
    """
    dir values:
    0: north
    1: east
    2: south
    3: west
    """
    # print('Moving in direction',dir)

    if hasattr(player.cur_room, dir+"_to"):
        player.cur_room = getattr(player.cur_room, dir+"_to")
    else:
        print("You can't go that way.")

# item transfer function
def transfer(item, taking):
    '''
    params:
    item: name of item to take
    taking: boolean,
        True = take from floor
        False = put from pockets
    '''
    # standardize input
    item = item.lower()
    # print(item)

    # # create some shortcuts (it doesn't work)
    # r_i = player.cur_room.items
    # p_i = player.items
    # if taking an item
    if taking:
        # print([i.name for i in player.cur_room.items])
        # if the name is found in the room
        if item in [i.name for i in player.cur_room.items]:
            # iterate through item list and grab item object via index
            for i, item_obj in enumerate(player.cur_room.items):
                if item_obj.name == item:
                    player.items.append(player.cur_room.items.pop(i))
                    print("You pick up the",item)
        else:
            # didn't find the item
            print("You can't seem to find that here.")
    # putting down an item
    else:
        if item in [i.name for i in player.items]:
            # iterate through item list and grab item object via index
            for i, item_obj in enumerate(player.items):
                if item_obj.name == item:
                    player.cur_room.items.append(player.items.pop(i))
                    print("You drop the",item,"on the ground.")
        else:
            # didn't find the item
            print("You can't seem to find that while rummaging through your pockets.")

# print inventory function
def pinv():
    if len(player.items) > 1:
        print('You check your pockets, you have:')
        for item in player.items:
            if item.name[0] in ['a','e','i','o','u']:
                print('An',item.name)
            else:
                print('A ',item.name)
    else:
        ('You rummage through your pockets and find nothing.')

def inspect(itemname):
    # tell player to pick up item before being able to inspect it
    if itemname in [i.name for i in player.cur_room.items]:
        print(f"You see the {itemname} on the floor but can't get a good look at it.")
    elif itemname in [i.name for i in player.items]:
        print("You inspect the",itemname)
        for item in player.items:
            if item.name == itemname:
                print(item.desc)
    else:
        print("You try to imagine what it is, but it doesn't come to you.")
# print help function
def ph():
    print(
        """Controls:
Go north: n, north
Go east: e, east
Go south: s, south
Go west: w, west
Show this help screen: ?, help
Quit the game: q, quit
Take an item: get, grab, take
Drop an item: put, drop
View inventory: i, inv, inventory
Inspect an item: look, inspect
"""
    )

# action table, deals with 
def act(c):
    # split command by word
    c_list = c.split()
    if not c_list:
        c_list.append('')
    c = c_list[0]
    # print(c_list)
    if c in ['n','north']:      # go north
        go('n')
    elif c in ['e','east']:     # go east
        go('e')
    elif c in ['s','south']:    # go south
        go('s')
    elif c in ['w','west']:     # go west
        go('w')
    elif c in ['?','help']:     # get help
        ph()
    elif c in ['q','quit']:     # quit game
        global wants_to_quit
        wants_to_quit = True
    elif c in ['get','grab','take']: # grab an item
        # check to make sure that there's an item specified
        if len(c_list) > 1:
            transfer(c_list[1], True)
        else:
            print("You can't decide what to take.")
    elif c in ['put','drop']:
        if len(c_list) > 1:
            transfer(c_list[1], False)
        else:
            print("You go to drop something, but forget what you're doing.")
    elif c in ['inv','i','inventory']:
        pinv()
    elif c in ['inspect','look']:
        inspect(c_list[1])
    else:
        print("You don't know how to do that.")

# Initial printing
ph()
print()

# REPL game loop
while not wants_to_quit:
    # print("quitting:",~wants_to_quit)
    print(player.cur_room.name)
    print(player.cur_room.desc)
    print()

    if len(player.cur_room.items) > 0:
        itemlist = ''
        for item in player.cur_room.items:
            if item.name[0] in ['a','e','i','o','u']:
                itemlist += 'an '
            else:
                itemlist += 'a '
            itemlist += item.name + ", "
        itemlist = itemlist.strip(', ')

        # single item
        print('On the ground you see', itemlist)

    comm = input("Command: ")

    act(comm.lower())

    # spacing
    print()
