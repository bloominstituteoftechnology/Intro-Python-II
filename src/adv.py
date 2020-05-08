from item import Item
from room import Room
from player import Player

# Define the default prompt.

prompt = '> '

# Define commands.


def drop(player, item_names):
    for name in item_names:
        try:
            if items[name] in player.inventory.keys():
                player.room.contents[items[name]] += 1
                player.inventory[items[name]] -= 1
                if player.inventory[items[name]] == 0:
                    player.inventory.pop(items[name])
                print(f'You dropped {items[name].short}.')
            else:
                print(f'The {name} doesn\'t seem to be something you can drop '
                      'at the moment.')
        except KeyError:
            print(f'The {name} doesn\'t seem to be something you can drop at '
                  'the moment.')


def get(player, item_names):
    for name in item_names:
        try:
            if items[name] in player.room.contents:
                player.inventory[items[name]] += 1
                player.room.contents[items[name]] -= 1
                if player.room.contents[items[name]] == 0:
                    player.room.contents.pop(items[name])
                    print(f'You have picked up {items[name].short}.')
            else:
                print(f'The {name} doesn\'t seem to be something you can get, '
                      'at least not here and now.')
        except KeyError:
            print(f'The {name} doesn\'t seem to be something you can get, '
                  'at least not here and now.')


def inv(player, filter):
    if len(player.inventory) == 0:
        print('You are empty-handed.')
    else:
        print('You are carrying:')
        for item, count in player.inventory.items():
            if ' '.join(filter) in item.short:
                if count == 1:
                    print(item.short)
                else:
                    print(f'{count} of {item.short}')


def look(player, item_names):
    if len(item_names) == 0:
        print(player.room)
    else:
        for name in item_names:
            try:
                if items[name] in player.inventory or \
                 items[name] in player.room.contents:
                    print(items[name].full)
            except KeyError:
                print(f'The {name} doesn\'t appear to be visible at the '
                      'moment.')


# Define aliases.
aliases = {'i': 'inv',
           'inventory': 'inv',
           'l': 'look',
           'take': 'get',
           }


# Declare all the rooms

rooms = {
    'outside':  Room('Outside Cave Entrance',
                     'North of you, the cave mouth beckons.'),

    'foyer':    Room('Foyer',
                     ('Dim light filters in from the south. Dusty passages '
                      'run north and east.')),

    'overlook': Room('Grand Overlook',
                     ('A steep cliff appears before you, falling into the '
                      'darkness. Ahead to the north, a light flickers in the '
                      'distance, but there is no way across the chasm.')),

    'narrow':   Room('Narrow Passage',
                     ('The narrow passage bends here from west to north. The '
                      'smell of gold permeates the air.')),

    'treasure': Room('Treasure Chamber',
                     'You\'ve found the long-lost treasure chamber! Sadly, it '
                     'has already been completely emptied by earlier '
                     'adventurers. The only exit is to the south.'),
}

# Link rooms together

rooms['outside'].exits['n'] = rooms['foyer']
rooms['foyer'].exits['s'] = rooms['outside']
rooms['foyer'].exits['n'] = rooms['overlook']
rooms['foyer'].exits['e'] = rooms['narrow']
rooms['overlook'].exits['s'] = rooms['foyer']
rooms['narrow'].exits['w'] = rooms['foyer']
rooms['narrow'].exits['n'] = rooms['treasure']
rooms['treasure'].exits['s'] = rooms['narrow']


# Define items, if any.

items = {
        'lantern': Item('lantern',
                        'a battered brass lantern',
                        'A battered brass lantern rests on the ground here.',
                        'It\'s worn and dented, but still holds oil.'),
        'flyer': Item('flyer',
                      'a tattered flyer',
                      'A tattered flyer lies nearby.',
                      'It\'s an advertisement for a lantern company: "Do you '
                      'sweat when you adventure? Can you really trust a mere '
                      'spray to keep GRUES from smelling YOU? Acme Lanterns '
                      'has the answer!"'
                      )
        }

# Place item(s) in rooms.

rooms['outside'].contents[items['lantern']] = 1
rooms['narrow'].contents[items['flyer']] = 1

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(rooms['outside'])

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
action = input(f'{player.room}\n\n{prompt}')
while action not in ['q', 'quit']:
    try:
        action = action.lower().split()
        if action[0] in aliases:
            action[0] = aliases[action[0]]
        elif action[0] == 'go':
            if len(action) == 1:
                print('Go where?')
            else:
                action = action[1:]
        try:
            player.room = player.room.exits[action[0]]
            print(player.room)
        except (TypeError, KeyError):
            eval(f'{action[0]}(player, {action[1:]})')
    except NameError:
        print(f'There\'s no obvious way to do that.')
    except Exception as e:
        print(e)
    finally:
        action = input(f'\n{prompt}')
