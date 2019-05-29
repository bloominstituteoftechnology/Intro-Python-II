from textwrap3 import wrap
from colorama import Fore, Back, Style 
import re

from room import Room
from player import Player
from item import Item, LightSource


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True, [Item('rope', 'for climbing'),
                                                                    Item('breadcrumbs', 'to find way back')] ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False, [Item('compass', 'for direction'),
                                         Item('binoculars', 'to see farther'),
                                         Item('drone', 'to scout'),
                                         LightSource('candle', "to see")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", True, [LightSource('lattern', 'for light'),
                                                               Item('bucket', 'for carrying things')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False, [Item('mre', 'to eat'),
                                                           Item('water', 'to drink'),
                                                           Item('shovel', 'to dig'),
                                                           Item('ax', 'to chop')]),

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


def is_light(player, room):
    return (len([i for i in player.items if isinstance(i, LightSource)]) > 0) or \
           (len([i for i in room.items if isinstance(i, LightSource)]) > 0)    
def prCyan(skk): print(f"\033[96m{skk}\033[00m") 
def prBold(skk): print(f"\033[01m{skk}\033[00m")
def fmLightGray(skk): return f"\033[44m\033[33m{skk}\033[00m"
#\e[0;37m
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
player = Player('Mark', croom, [Item('walking stick', 'for walking'),LightSource('flashlight', 'for searching')])
directions = fmLightGray('enter "n", "s", "e", or "w" , or "get/take" or "drop" item, or i[nventory] or q to exit ')
black = "It's pitch black!"
dlist = list("ewns")
while True:
    prBold(croom.name)
    lines = wrap(croom.description, 110)
    print("\033[33m")
    for line in lines:
        print(line)
    print("\033[00m")
    text = input(directions)
    texts = text.split(' ')
    if len(texts) > 2:
        m = re.match(r"(\w+)\s\"([\w\s]+)\"", text)
        if len(m.groups()) == 2:
            texts = [m.group(1),m.group(2)]
    if len(texts) > 1:
        if len(texts) == 2:
            if texts[0] in ['get', 'take']:
                names = [i.name for i in croom.items]
                if texts[1] in names:
                    if is_light(player, croom):
                        index = names.index(texts[1])
                        item = croom.items[index]
                        croom.items.remove(item)
                        player.items.append(item)
                        item.on_take()
                    else:
                        print(fmLightGray("Good luck finding that in the dark!"))
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
        if is_light(player, croom):
            print(f'{fmLightGray("player")} {Fore.BLACK}{Back.GREEN}{player.name}{Style.RESET_ALL} {fmLightGray("items")}')
            for item in player.items:
                print(f'{fmLightGray("name:")} {Fore.GREEN}{item.name}{Fore.WHITE}  {fmLightGray("description:")}')
                lines = wrap(item.description, 110)
                for line in lines:
                    prCyan(line)

        else:
            print("\033[04m\033[31m" + black + "\033[00m")  
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
