from room import Room
from player import Player

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

room['foyer'].n_to = room['foyer']
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

print('\n\n======================================================')
print('                Welcome to Adventure Game:')
print('======================================================\n')

# Make a new player object that is currently in the 'outside' room.
player = Player(input('Enter a name: '), room['foyer'])
player.current_room = player.current_room.s_to
print('Your are in the ', player.current_room.name)
print('Description: ', player.current_room.description)

def wichWay():
    global direction
    print('------------------------------------------')
    direction = input('Choose a compass direction: \n N = North, S = South, E = East, or W = West \n')
wichWay()

# Write a loop that:

while True:
    if direction == 'n':
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
            print('Description: ', player.current_room.description)
            wichWay()
        else:
            print('Can not go North from here')
            wichWay()

    if direction == 's':
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
            print('Your are in the ', player.current_room.name)
            print('Description: ', player.current_room.description)
            wichWay()
        else:
            print('Can not go to South from here')
            wichWay()
    if direction == 'e':
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to
            print('You are in the ', player.current_room.name)
            print('Description: ', player.current_room.description)
            wichWay()
        else:
            print('Can not go Easth from here')
            wichWay()
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to
            print('You are in the ', player.current_room.name)
            print('Description: ', player.current_room.description)
            wichWay()
        else:
            print('Can not go West frm here')
            wichWay()
    if direction == 'q':
        print('Good bye')
        break
        
    else:
        print('Wrong Entry')
        wichWay()