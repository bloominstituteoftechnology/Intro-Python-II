from room import Room
from player import Player
import textwrap
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
directions = ['n', 's', 'e', 'w']
player = Player("Ezra Black", room ['outside'])
# Write a loop that:
#
while True:
    selection = input('Where to? ').lower().split(' ')
    if len(selection) > 2 or len(selection) < 1:
        print("please type help for more valid commands.")
    elif len(selection) == 2:
        if selection[0] in item_actions:
            if selection[0] == 'get' or selection[0] == 'take':
                item = player.current_room.search_items(selection[1])
                player.current_room.drop_item(item)
                player.add_item(item)
                item.on_take(item)
            elif selection[0] == 'drop':
                item = p.search_items(selection[1])
                player.current_room.add_item(item)
                player.drop_item(item)
                item.on_drop(item)
        else: 
            print("type help for more information")
    else:
        if selection[0] == 'q' or selection[0] == 'quit':
            print(f'See you next time {player.name}!') 
            break

        if selection[0] == 'h' or selection[0] == 'help':
            print("Commands:\n'n' - North\n's' - South\n'e' - East\n'w' - West\n'i'\nor 'quit' - Exit Game\n")
            continue

        # if selection[0] == 'inventory' or selection[0] == 'inventory':
        #     player.print_items()
        #     continue

        if selection[0] in directions:
            try:
                player.move_room(selection[0])
                print(f'Location: {player.current_room.name} - {player.current_room.description}\n')
                player.current_room.print_items()
            except AttributeError:
                print('Go a different way')
        else:
            print('Enter a direction (n, s, e, w)')