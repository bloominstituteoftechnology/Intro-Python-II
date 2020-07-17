import re
from room import Room
from player import Player
from item import Item
from prop import Prop
from fixed import Fixed

cardinals = re.compile('north|south|east|west', re.IGNORECASE)
shortCards = re.compile('nesw', re.IGNORECASE)

# Declare all the rooms

room = {
    'outside':  Room("Outside the Cave Entrance",
                     "North of you, the cave mount beckons."),

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

"""
          *light*
        /\/\/\/\/\/
        [overlook ]         [treasure]
            | |                 | |
        [  foyer  ]   <==>  [ narrow ]
            | |
        [ outside ]
"""

# Props
room['foyer'].add_item('key', Prop('Key', 'A glinting, golden key'))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("Welcome. What is your name, traveler?\n: ")
player = Player(name, room['outside'])

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


def movePlayer(player, direction):
    """ Checks to see if there is a room in the direction the player wants
       to move, and moves them if there is """
    if direction == "n" and player.in_room.n_to != None:
        player.in_room = player.in_room.n_to
        return True
    elif direction == "e" and player.in_room.e_to != None:
        player.in_room = player.in_room.e_to
        return True
    elif direction == "s" and player.in_room.s_to != None:
        player.in_room = player.in_room.s_to
        return True
    elif direction == "w" and player.in_room.w_to != None:
        player.in_room = player.in_room.w_to
        return True
    else:
        return False


def wait():
    input(': [OK]')


print(f'\n\nWelcome, {player.name.capitalize()}')
print('Your objective is to find the treasure... without dying first! 😱')
print('You can enter ? for help.')
wait()

while player.alive:
    print("\n\n")
    print(player.in_room)
    for item in player.in_room.items:
        print(f'🔹 {player.in_room.items[item]}')
    for prop in player.props:
        print(f'👜 {player.props[prop]}')
    print('\nWhat do you want to do?')
    selection = input(': ')

    # print(f"SELECTION: {selection}")
    if selection != '':
        sl = selection.lower().split(' ')   # lowercase and split the string
        if len(sl) == 1:
            # `verb-only` selection
            if cardinals.match(sl[0]) or sl[0] == 'n' or sl[0] == 'e' or sl[0] == 's' or sl[0] == 'w':
                # take the first letter of the input string
                s = sl[0][0]
                if not movePlayer(player, s):
                    print('\n\n🤔 There is no path leading in that direction.')
                    wait()
            elif sl[0] == 'q':
                player.alive = False
            elif sl[0] == '?':
                print('Please enter the direction you wish to travel:')
                print('\t[N]orth, [E]ast, [S]outh, or [W]est.')
                print('\nFor items:')
                print('\t[T]ake [item] \t\tto pick up an item')
                print('\t[D]rop [item] \t\tto drop an item')
                print('\t[U]se [item1] on [item2] to use an item.')
                print('\nOr enter [Q] to quit.')
                print('\n\nPress ENTER to continue.')
                wait()
        elif len(sl) == 2:
            # implement `verb noun` selection here
            # only Take and Drop are valid here
            prop_name = sl[1]
            if sl[0] == 't' or sl[0] == 'take':
                if prop_name in player.in_room.items.keys():
                    if isinstance(player.in_room.items[prop_name], Prop):
                        if player.pick_up(player.in_room.items[prop_name]):
                            player.in_room.remove_item(prop_name)
                    else:
                        # if this is a fixed item
                        print("That's not something you can pick up.")
                        wait()
                else:
                    print(f'\n\n🤔 There is no {prop_name} in this room.')
                    wait()
            elif sl[0] == 'd' or sl[0] == 'drop':
                prop = player.put_down(prop_name)
                if prop != None:
                    player.in_room.add_item(prop_name, prop)
        else:
            print(
                'That is not a valid choice. Please try again. Enter ? for help. Enter Q to quit.')
            wait()
