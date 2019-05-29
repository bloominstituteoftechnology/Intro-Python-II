from textwrap3 import wrap
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('rope', 'for climbing'),
                                                              Item('breadcrumbs', 'to find way back')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('compass', 'for direction'),
                                  Item('binoculars', 'to see farther'),
                                  Item('drone', 'to scout')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('lattern', 'for light'),
                                                         Item('bucket', 'for carrying things')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('mre', 'to eat'),
                                                    Item('water', 'to drink'),
                                                    Item('shovel', 'to dig'),
                                                    Item('ax', 'to chop')
                                                    ]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")
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
# Print an error message if the movement isn't allowed.q
#
# If the user enters "q", quit the game.
croom = room['outside']
player = Player('Mark', croom, [Item('walking_stick', 'for walking')])
directions = 'enter "n", "s", "e", or "w" , or "get/take" or "drop" item, or i[nventory] or q to exit '
dlist = list("ewns")
while True:
    print(croom.name)
    lines = wrap(croom.description, 110)
    for line in lines:
        print(line)
    text = input(directions)
    texts = text.split(' ')
    if len(texts) > 1:
        if len(texts) == 2:
            if texts[0] in ['get', 'take']:
                names = [i.name for i in croom.items]
                if texts[1] in names:
                    index = names.index(texts[1])
                    item = croom.items[index]
                    croom.items.remove(item)
                    player.items.append(item)
                    item.on_take()
                else:
                    print(f"room doesn't have item {texts[1]}")
            elif texts[0] == 'drop':
                names = [i.name for i in player.items]
                if texts[1] in names:
                    index = names.index(texts[1])
                    item = player.items[index]
                    player.items.remove(item)
                    item.on_drop()
                    croom.items.append(item)
                else:
                    print(f"player doesn't have item {texts[1]}")
            else:
                print('usage: <get/take or drop> item name')
        else:
            print('maximum of two words')
        continue

    if text in ['i','inventory']:
        print(f'player {player.name} items')
        for item in player.items:
            print(f'name: {item.name}  description:')
            lines = wrap(item.description, 110)
            for line in lines:
                print(line)  
        continue          


    if text == 'q':
        break
    if text in dlist:
        # print(f'{text} in "ewns"')
        if text == 'e':
            if hasattr(croom, 'e_to'):
                croom = croom.e_to
            else:
                print("Can't move East")
        elif text == 'w':
            if hasattr(croom, 'w_to'):
                croom = croom.w_to
            else:
                print("Can't move West")
        elif text == 'n':
            if hasattr(croom, 'n_to'):
                croom = croom.n_to
            else:
                print("Can't move North")
        elif text == 's':
            if hasattr(croom, 's_to'):
                croom = croom.s_to
            else:
                print("Can't move South")
        else:
            throw('logic error')
    else:
        print(f'{text} not found')
        print(directions)
