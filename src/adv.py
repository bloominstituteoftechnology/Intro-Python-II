from room import Room
from player import Player
from items import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave  Entrance",
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

# Item Types
item = {
    "sword": Item("sword", "weapon", 5),
    "shield": Item("shield", "weapon", 7),
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
room['outside'].items = [item['sword'], item['shield']]

#
# Main
#


def try_dir(dir, current_room):
    attribute = dir+'_to'
    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
        print('you can not go that way')
        return current_room


# Make a new player object that is currently in the 'outside' room.
player = Player('Jb', room['outside'])

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
while True:
    print(player)
    cmd = input('=>').lower().split()
    first_arg = cmd[0]
    second_arg = cmd[-1]
    if first_arg[0] == 'q':
        break
    elif first_arg == 'move':
        player.current_room = try_dir(second_arg[0], player.current_room)
    elif first_arg == 'look':
        print(player.current_room.description)
    elif first_arg == 'inventory':
        print(player.item_list())
    elif first_arg == 'search':
        items = player.current_room.items
        if items:
            for i in items:
                print(i)
            inpt = input('=>').lower().split()
            first_arg = inpt[0]
            second_arg = inpt[-1]
            if first_arg[0] == 'q':
                break
            elif first_arg == 'take':
                for i in items:
                    if i.name == second_arg:
                        print(i)
                        player.items.append(item[i.name])
                        player.current_room.items.remove(i)
                        print(f'You take the {i.name}')

            elif first_arg == 'examine':
                print(player.current_room.description)
                print(inpt)
            else:
                print('You search the room, yet find nothing of use.')
