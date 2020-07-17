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
passages run north, east, and west."""),

    'armory':   Room("Armory", """An ancient armory lies before you, mostly filled
    with dust and rusted or broken weapons. There's an opening to the North, and
    the foyer back to the South."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'dungeon': Room("Dungeon", """A small dungeon with rusted bars on its cells.
    Skeletons are the permenant residents of each cell. No way out but the way you came."""),

    'narrow':   Room("Narrow Passage", """The narrow passage stretches from west
to east. The smell of gold permeates the air."""),

    'hall':     Room("Hall", """A great hall stands here, the ringing cries of celebrated battle
    victories still dimly filling the air. There are two grand doors, one to the North and one
    to the East. The narrow passage is to the West."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! The only exit is to the south."""),

    'chamber': Room("King's Chamber", """The chamber of a long forgotten king. The only
    exit is the way you came in, to the West.""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['armory']
room['armory'].s_to = room['foyer']
room['armory'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['armory']
room['foyer'].w_to = room['dungeon']
room['dungeon'].e_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].e_to = room['hall']
room['hall'].w_to = room['narrow']
room['hall'].e_to = room['chamber']
room['chamber'].w_to = room['hall']
room['treasure'].s_to = room['hall']
room['hall'].n_to = room['treasure']

"""
                      *light*
                    /\/\/\/\/\/
                    [overlook ]
                        | |
                    [  armory ]                          [treasure]
                        | |                                 | |
[ dungeon ]  <==>   [  foyer  ]   <==>  [ narrow ]  <==> [  hall  ]  <==> [ chamber ]
                        | |
                    [ outside ]
"""

# Props
keyProp = Prop('Key', 'A glinting, golden key')    # in the zombie

sword = Prop('Sword', 'A shining, magical sword. You can feel its power')
room['chamber'].add_item(sword)

bow = Prop('Bow', 'A bow with a strange power: it creates an arrow with each pull')
room['armory'].add_item(bow)

cyrstal = Prop('Crystal', 'A round, dingy crystal that probably has no value')
room['overlook'].add_item(cyrstal)

rope = Prop('Rope', 'A very long bit of rope')
room['foyer'].add_item(rope)

treasure = Prop('Treasure', "The riches you've been seeking")  # in the chest

# Fixed items
zombie = Fixed('Zombie', 'A disgusting and deadly-looking zombie',
               'The zombie ate your brain.', 'The zombie dropped a Key as it faded away!')
zombie.open_when_used = True
zombie.item_inside = keyProp
zombie.used_with = sword
room['dungeon'].add_item(zombie)

demon = Fixed('Demon', 'This demon is clearly the guardian of this place', 'The demon visciously attacks, and....',
              'It screams horribly as it sinks into the flames of hell, never to been seen again.')
demon.used_with = bow
demon.blocking_path = 'n'
room['hall'].add_item(demon)

boulder = Fixed('Boulder', 'An immovable boulder, with an odd circular hole in the center',
                '', 'With the crystal in place, the boulder rolls itself away from the passage.')
boulder.used_with = cyrstal
boulder.blocking_path = 'e'
room['narrow'].add_item(boulder)

chasm = Fixed('Chasm', "It's really quite beautiful, and you can hear water rushing below",
              'You fell down the chasm. That was stupid.')
chasm.blocking_path = 'n'
room['overlook'].add_item(chasm)

chest = Fixed('Chest', 'A locked chest, clearly filled with treasure')
chest.open_when_used = True
chest.item_inside = treasure
chest.used_with = keyProp
room['treasure'].add_item(chest)

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
    # check to see if any items are blocking a path
    n_blocked = None
    e_blocked = None
    s_blocked = None
    w_blocked = None

    for item_name in player.in_room.items:
        item = player.in_room.items[item_name]
        if isinstance(item, Fixed):
            if item.blocking_path == 'n':
                n_blocked = item
            if item.blocking_path == 'e':
                e_blocked = item
            if item.blocking_path == 's':
                s_blocked = item
            if item.blocking_path == 'w':
                w_blocked = item

    if direction == "n" and player.in_room.n_to != None:
        if n_blocked == None:
            player.in_room = player.in_room.n_to
            return True
        else:
            player.use_fixed(n_blocked)
            return False
    elif direction == "e" and player.in_room.e_to != None:
        if e_blocked == None:
            player.in_room = player.in_room.e_to
            return True
        else:
            player.use_fixed(e_blocked)
            return False
    elif direction == "s" and player.in_room.s_to != None:
        if s_blocked == None:
            player.in_room = player.in_room.s_to
            return True
        else:
            player.use_fixed(s_blocked)
            return False
    elif direction == "w" and player.in_room.w_to != None:
        if w_blocked == None:
            player.in_room = player.in_room.w_to
            return True
        else:
            player.use_fixed(w_blocked)
            return False
    else:
        return False


def wait():
    input(': [OK]')


def invalid_choice():
    print('That is not a valid choice. Please try again. Enter ? for help. Enter Q to quit.')
    wait()


print(f'\n\nWelcome, {player.name.capitalize()}')
print('Your objective is to find the treasure and escape... without dying first! 😱')
print('You can enter ? for help.')
wait()

while player.alive:
    print("\n\n")
    print(player.in_room)
    for item_name in player.in_room.items:
        item = player.in_room.items[item_name]
        if isinstance(item, Prop) or item.removed == False:
            print(f'🔹 {item}')
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
            else:
                invalid_choice()
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
                    player.in_room.add_item(prop)
            else:
                invalid_choice()
        elif len(sl) == 4:
            if sl[2] == 'on' and (sl[0] == 'use' or sl[0] == 'u'):
                if sl[1] in player.props.keys() and sl[3] in player.in_room.items.keys():
                    prop = player.props[sl[1]]
                    fixed = player.in_room.items[sl[3]]
                    player.use_prop(prop, fixed)
        else:
            invalid_choice()

    if player.in_room == room['outside'] and 'treasure' in player.props.keys():
        print('You found the treasure and escaped! You win!')
        print("...but didn't you know the treasure was cursed?")
        player.die()
