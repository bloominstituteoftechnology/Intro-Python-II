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

from item import Item
items = {
    'sword': Item('outside',"sword", "notched and rusted blade."),
    'daffodil': Item('outside','daffodil', 'lovely blooming flower.'),
    'pipe': Item('foyer', 'pipe', 'intricately carved wood pipe.'),
    'snakeskin': Item('foyer', 'snakeskin', 'big one, too.'),
    'boot': Item('overlook', 'boot', 'bleached-white human skull!!'),
    'spoon': Item('overlook', 'spoon', 'sturdy spoon for adventures!'),
    'feathers': Item('narrow', 'feathers', 'mound of downy feathers'),
    'bucket': Item('narrow', 'bucket', 'bucket with a hole in it'),
    'sock': Item('treasure', 'sock', 'bleached-white human skull!!'),
    'purse': Item('treasure', 'purse', 'bag of silver coins!'),
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
    wantPickup = input('\nWould you like to pick up an item here? y n')
    itemToPickup = input('What would you like to pick up (e.g. sword)? Enter item: ')

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
        
