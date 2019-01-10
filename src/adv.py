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

items = {
    'sword': Item('sword', 'It looks rusty. Don\'t get tetanus!'),
    'coin': Item('coin', 'Is that gold!! Oh no wait... it is silver.'),
    'knife': Item('knife', 'Ouch sharp!'),
    'bat': Item('bat', 'Don\'t know why you would take a live animal but ok.')
}

# Link items to rooms
room['foyer'].items = [items['sword'], items['coin']]
room['overlook'].items = [items['knife']]
room['narrow'].items = [items['bat']]


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
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def try_direction(direction, currentRoom):
    attribute = direction + '_to'

    if hasattr(currentRoom, attribute):
        newRoom = getattr(currentRoom, attribute)
        return newRoom
    else:
        print('\nCan not go this way!!!')
        return currentRoom


userName = input('What is your name? ')
player = Player(userName, room['outside'])

print(f'\nHello {userName}! Let\'s go on an adventure!')

userInput = ''


while not userInput == 'q':
    # newRoom = ''
    print(player.currentRoom)
    userInput = input('Which way do you want to do or go?\n'
                      'Directions: [n] North [s] South [e] East [w] West\n'
                      'Items: take (item), drop (item), or inspect (item)\n'
                      '[i] Inventory\n'
                      'or [q] Quit:\n')

    if userInput == 'n'\
            or userInput == 's'\
            or userInput == 'e'\
            or userInput == 'w':

        player.currentRoom = try_direction(userInput, player.currentRoom)

    elif 'take' in userInput or 'drop' in userInput or 'inspect' in userInput:
        action = userInput.split()
        actionVerb = action[0]
        actionItem = action[1]

        try:
            item = items[actionItem]

            if actionVerb == 'take':
                if item in player.currentRoom.items:
                    player.currentRoom.removeItem(items[actionItem])
                    player.takeItem(items[actionItem])
                    print(items[actionItem].on_take())
                else:
                    print('\nItem is not in the room')

            elif actionVerb == 'drop':
                if item in player.items:
                    player.currentRoom.addItem(items[actionItem])
                    player.dropItem(items[actionItem])
                    print(items[actionItem].on_drop())
                else:
                    print('You do not have this item.')

            elif actionVerb == 'inspect':
                if item in player.items:
                    print(item.inspect())
                else:
                    print('\nThis is not an item in your inventory.')

        except KeyError:
            print('\nThis is not an item.\n')

        print(f'{player.name}\'s items: ', player.items)

    elif userInput == 'i':
        print(f'\nYour items: {player.items}')

    elif userInput == 'q':
        print('Thanks for playing!!!')

    else:
        print('Incorrect input. Please follow instructions.')
