from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
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

### make items and add them to rooms
## name, description

treasure_room = Item('goldbar', "you've found the gold! Not get out of there! The place is caving in!")
outside_room = Item('rock', 'a good starter weapon')
foyer_room = Item('blanket', 'used to keep you warm, can also be used as a cape.')
overlook_room = Item('armorbundle','used mostly for protective.')
narrow_room = Item('detector', 'used to find metals, such as gold.')

#add them in 

room['outside'].add_items(outside_room)
room['foyer'].add_items(foyer_room)
room['narrow'].add_items(narrow_room)
room['treasure'].add_items(treasure_room)
room['overlook'].add_items(overlook_room)






'''
items = {
    'gold': Item('bars of gold',
                "you've found the gold! Not get out of there! The place is caving in!"),
    'armor': Item('body armor',
                'used mostly for protective.'),
    'detector': Item('metal detector',
                        'used to find metals, such as gold.'),
    'blanket': Item('blanket', 
                'used to keep you warm, can also be used as a cape.')
}
'''

# Link rooms togetherk


'''
looks like from "outisde", if you go north direction
you go to the "foyer" room ok cool.
'''

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
#lay

# Make a new player object that is currently in the 'outside' room.


'''currently player has just self, and room as arg:
changing it to add name
'''





# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).


# * Waits for user input and decides what to do.

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

print("What's your name?")
player_name = input("~ ")
player = Player(player_name, room['outside'])
print(f"\nHi, {player.name}. It's up to you to find the GOLD!\nRight now, you're at the {player.current_room.name}.\n{player.current_room.desc}")


directions = ['n','s','e','w']

while True:
    print(f"What do you want to do now, {player.name}? (n, s, e, w to move | l to look around | i to view inventory | d to drop item - q to quit)")
    m = input("~ ")

    if m in directions:
        player.move(m)
    elif m == 'q':
        print(f"GGs {player.name}. Thanks for playing")
        exit()
    elif m == 'l':
        print(f"cool you found a {player.current_room.items.name}! {player.current_room.items.desc}\ntype p to pick it up")



    ### just need pickup, drop and view inventory
    ## did all this by jsut typing a letter, you can't really select a 
    # item yet, gonna have to add that later..

    elif m == 'p':
        player.get_item(player.current_room.items)
        print(f'you just picked up a {player.current_room.items}')

    elif m == 'd':
        player.drop_item(player.current_room.items)
        print(f'you just dropped a {player.current_room.items.name}')


    elif m == 'i':
        player.view_inventory()

    else:
        print('Invalid entry.')




#
# If the user enters "q", quit the game.

# for i in inventory:
#   print(i.name)


'''
python d2/adv.py
'''