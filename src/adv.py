from room import Room
from player import Player
from item import Item

# Declare items

items = {
    'scuttle': Item('scuttle', 'Gain 20/20 vision.'),

    'axe': Item('axe', 'Rather sharp.'),

    'biscuit': Item('biscuit', 'Oh you know.')
}

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

room['outside'].items = [items['scuttle']]
room['overlook'].items = [items['axe'], items['biscuit']]


# Main
#

# Make a new player object that is currently in the 'outside' room.

new_player = Player('Billy', room['outside'])


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

paths = ['n', 'e', 's', 'w']

while True:
    print(f'\nCurrent room: {new_player.current_room.name}.')

    if new_player.current_room.name == "Grand Overlook" and new_player.enlightened == True:
        print(f'\nThe effects of the potion allow you to see magic platforms that traverse the chasm.\n')

    print(f'"{new_player.current_room.description}"\n')

    if new_player.current_room.name == "Secret Room":
        break

    if new_player.current_room.items:
        print(f'Loot available: {new_player.current_room.items}\n')

    access = input("How will you proceed? ").lower()
    access = access.split(" ")

    if len(access) == 2:
        action = access[0]
        item = access[1]

        if action == 'grab' or action =='collect':
            for i in new_player.current_room.items:
                if i.name == item:
                    new_player.current_room.items.remove(i)
                    new_player.inventory.append(i)
                    i.on_collect()
                else:
                    print('\nError: No loot available')
        if action == 'drop':
            for i in new_player.inventory:
                if i.name == item:
                    new_player.inventory.remove(i)
                    new_player.current_room.items.append(i)
                    i.on_drop()
        if action == 'use':
            for i in new_player.inventory:
                if i.name == item:
                    if item == 'axe':
                        new_player.inventory.remove(i)
                        print('\n Player picks up sharp axe. ')
                        room['overlook'].n_to = room['secret']
                        new_player.enlightened = True

    if len(access) == 1:
        access = access[0]

        if access in paths:
            if access == 'n' and new_player.current_room.n_to != None:
                new_player.current_room = new_player.current_room.n_to
            elif access == 'e' and new_player.current_room.s_to != None:
                new_player.current_room = new_player.current_room.s_to
            elif access == 's' and new_player.current_room.e_to != None:
                new_player.current_room = new_player.current_room.e_to
            elif access == 'w' and new_player.current_room.w_to != None:
                new_player.current_room = new_player.current_room.w_to
            else:
                access = input("Could not enter, please procced with different path. (Enter to continue)\n").lower()
        elif access == 'i' or access == 'inventory':
            print(f'\nInventory: {new_player.inventory}')
        elif access == 'q':
            print(f'Farewell {new_player.name}! (Better luck next time!)')
            break
        else:
            print("Try different input value, input unrecognized. (Hint: N, E, S, or W)\n")