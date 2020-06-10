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

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

item = {
    'sword': Item('Sword', 'A cool sword'),
    'grail': Item('Grail', 'THE GRAIL')
}

room['foyer'].items = item['sword']
room['treasure'].items = item['grail']

player = Player('Pete', room['outside'])

# Write a loop that:

while True:
    print("\n")
    print(player.location)

    d = input("\nChoose direction: ").lower()    

    if d == 'q':
        print('quit check')
        break
    elif d == 'n' or d == 's' or d == 'e' or d == 'w':
        print('move check')
        player.move(d)
    elif d == 'i':
        print('inv check')
        player.print_inventory()
    elif len(d.split(' ')) > 1:
        print(d)
        action, item_name = d.split(' ')
        print('test')
        if action == 'get' or action == 'take':
            print('action')
            if item_name not in item or hasattr(player.location, 'items') == False:
                print("You can't take it with you. Because that item isn't here.")
            else:
                picked_up_item = item[item_name]
                player.location.remove_item(picked_up_item)
                player.get(picked_up_item)
                picked_up_item.on_take()        
        if action == 'drop':
            if item_name not in item or item[item_name] not in getattr(player, 'items'):
                print("You can't lose what you don't have. Because you're not carrying that item.")
            else:
                dropped_item = item[item_name]
                player.drop(dropped_item)
                player.location.store_item(dropped_item)
                dropped_item.on_drop()
    else:
        print("didn't work")             

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.