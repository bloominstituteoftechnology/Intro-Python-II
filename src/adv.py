from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

items = {
    'rock':     Item("rock",
                     "Unremarkable rock."),

    'lantern':  Item("lantern",
                     "Small lantern."),

    'coins':    Item("coins",
                     "Small bag of coins."),

    'sword':    Item("sword",
                     "Ordinary sword."),
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [items['rock']]),

    'foyer':    Room("Foyer",
                     "Dim light filters in from the south. Dusty passages run "
                     "north and east.",
                     [items['lantern'], items['coins']]),

    'overlook': Room("Grand Overlook",
                     "A steep cliff appears before you, falling into the "
                     "darkness. Ahead to the north, a light flickers in the "
                     "distance, but there is no way across the chasm.",
                     []),

    'narrow':   Room("Narrow Passage",
                     "The narrow passage bends here from west to north. The "
                     "smell of gold permeates the air.",
                     [items['sword']]),

    'treasure': Room("Treasure Chamber",
                     "You've found the long-lost treasure chamber! Sadly, it "
                     "has already been completely emptied by earlier "
                     "adventurers. The only exit is to the south.",
                     []),
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

player = Player('Nate', room['outside'], [])

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


def update_items(user_input):
    if user_input.split()[1] in items:
        item = items[user_input.split()[1]]
        if user_input.split()[0] in actions[:-1]:
            if item in player.current_room.items:
                player.current_room.items.remove(item)
                player.items.append(item)
                item.on_take()
            else:
                print('\n\nITEM NOT IN THIS ROOM!')
        if user_input.split()[0] == actions[-1]:
            if item in player.items:
                player.items.remove(item)
                player.current_room.items.append(item)
                item.on_drop()
            else:
                print('\n\nITEM NOT IN INVENTORY!')
    else:
        print('\n\nTHERE IS NO SUCH ITEM!')


def process_input(user_input):
    if user_input == 'n':
        if player.current_room.n_to is None:
            print(
                '\n\nTHERE IS NO ROOM IN THAT DIRECTION!\nYou are still in...')
        else:
            player.current_room = player.current_room.n_to
    elif user_input == 's':
        if player.current_room.s_to is None:
            print(
                '\n\nTHERE IS NO ROOM IN THAT DIRECTION!\nYou are still in...')
        else:
            player.current_room = player.current_room.s_to
    elif user_input == 'e':
        if player.current_room.e_to is None:
            print(
                '\n\nTHERE IS NO ROOM IN THAT DIRECTION!\nYou are still in...')
        else:
            player.current_room = player.current_room.e_to
    elif user_input == 'w':
        if player.current_room.w_to is None:
            print(
                '\n\nTHERE IS NO ROOM IN THAT DIRECTION!\nYou are still in...')
        else:
            player.current_room = player.current_room.w_to
    elif user_input.split()[0] in actions:
        update_items(user_input)
    elif user_input in ['i', 'inventory']:
        print('\n\nINVENTORY:' +
              '\n' + '\n'.join([item.name for item in player.items]))
    elif user_input != 'q':
        print('\n\nNOT A CARDINAL DIRECTION!\nYou are still in...')


actions = ['get', 'take', 'drop']

instructions = ('\n\nTo move, enter a cardinal direction: "n", "s", "e", or ' +
                '"w".' +
                '\nTo pick up an item in the room, enter "get" or "take" ' +
                'followed by the name of the item.' +
                '\nTo drop an item in inventory, enter "drop" followed by ' +
                'name of the item.' +
                '\nTo check inventory, enter "intenvory" or "i".'
                '\nTo quit, enter "q".\n')

user_input = None
while user_input != 'q':

    print('\n\n' + player.current_room.name +
          '\n\n' + textwrap.fill(player.current_room.description, 87))

    if len(player.current_room.items) > 0:
        print('\nYou can see the following items:' +
              '\n' + '\n'.join(
                  [item.name for item in player.current_room.items]))
    else:
        print('\nNo items in this room!')

    user_input = input(instructions)
    process_input(user_input)
