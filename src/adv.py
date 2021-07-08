from room import Room

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

def on_take_fn():
    print("\nYou just never know when you'll need something like this...")

def on_drop_fn():
    print("\nWon't be needing this anymore!")

from item import Item
items = {
    'sword': Item('outside',"sword", "notched and rusted blade.", on_take_fn, on_drop_fn),
    'daffodil': Item('outside','daffodil', 'lovely blooming flower.', on_take_fn, on_drop_fn),
    'pipe': Item('foyer', 'pipe', 'intricately carved wood pipe.', on_take_fn, on_drop_fn),
    'snakeskin': Item('foyer', 'snakeskin', 'big one, too.', on_take_fn, on_drop_fn),
    'boot': Item('overlook', 'boot', 'bleached-white human skull!!', on_take_fn, on_drop_fn),
    'spoon': Item('overlook', 'spoon', 'sturdy spoon for adventures!', on_take_fn, on_drop_fn),
    'feathers': Item('narrow', 'feathers', 'mound of downy feathers', on_take_fn, on_drop_fn),
    'bucket': Item('narrow', 'bucket', 'bucket with a hole in it', on_take_fn, on_drop_fn),
    'sock': Item('treasure', 'sock', 'bleached-white human skull!!', on_take_fn, on_drop_fn),
    'purse': Item('treasure', 'purse', 'bag of silver coins!', on_take_fn, on_drop_fn),
}

# Link rooms together

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
from player import Player

player = Player() #player is initialized with currentRoom='outside'

# Game loop
while True:
    # Player status **
    # Location
    currentRoom = room[player.currentRoom]
    # Print Room Name, Description
    roomName = currentRoom.name
    print(f'\nCurrent location: {roomName}')
    roomDesc = currentRoom.description
    print(roomDesc)
    # Print Items
    for item in items:
        if items[item].location == player.currentRoom:
            print(f'There is a {items[item].name}, a {items[item].description}')
    
    # Player action input
    action = input("Choose an action: take / drop / inventory / move. Enter action: ")

    # Player action responses
    if action == 'take':
        itemToTake = input('\nWhat do you want to take? Enter item: e.g. sword ')
        # Items players currently hold are kept in inventory
        items[itemToTake].location = 'inventory'
        player.inventory.append(itemToTake)
        items[itemToTake].on_take()

    elif action == 'drop':
        # Show the player's current inventory
        for item in player.inventory:
            print(item)

        itemToDrop = input('\nWhat do you want to drop? Enter item: e.g. daffodil ')
        # The item's new location is the room in which it was dropped
        items[itemToDrop].location = player.currentRoom

        #remove item from inventory
        player.inventory.remove(itemToDrop)

        items[itemToDrop].on_drop()

    elif action == 'inventory':
        for item in player.inventory:
            print(item)

    elif action == 'move':
        # Player movement input **
        print('\nWhere do you want to go? n s e w q')
        direction = input('Enter a direction: ')

        # Player movement responses **
        if direction =='n':
            try:
                player.currentRoom = currentRoom.n_to
            except AttributeError:
                print("\n*** You can't move north! ***")
        elif direction == 's':
            try:
                player.currentRoom = currentRoom.s_to
            except AttributeError:
                print("\n*** You can't move south! ***")
        elif direction == 'e':
            try:
                player.currentRoom = currentRoom.e_to
            except AttributeError:
                print("\n*** You can't move east! ***")
        elif direction == 'w':
            try:
                player.currentRoom = currentRoom.w_to
            except AttributeError:
                print("\n*** You can't move west! ***")
        elif direction == 'q':
            break
        else:
            continue

    


        
