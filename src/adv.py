from room import Room
from player import Player
import sys

class NoRoomThatDirection(Exception):
    pass

def change_rooms(move):
    """
    Function to change the room a player is in.
    Valid inputs are ['n','s','e','w']
    """
    try:
        # get attribute corresponding to player move
        attr = move+"_to"
        
        # check that there is a room in that direction
        if getattr(player.room, attr, 'error') == 'error':
            raise NoRoomThatDirection

        # updating room based on user move
        player.room = getattr(player.room,attr)
    
    except NoRoomThatDirection:
        print("There's nowhere to go in that direction, try another direction.")


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     ["old boot"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['torch']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['moldy bread']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['rusty sword']),
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
print("Please enter name")
name = input()
player = Player(name, room['outside'])

# Write a loop that:
while(True):
    # initializing has_moved variable
    has_moved = False

    # printing room name and description
    print(player.room.name)
    player.room.print_description()
    player.print_items()

    # get user move
    print('What would you like to do?')
    move = input().lower()

    # if player enters get command, ensure item is valid
    # then remove item from room and add it to player
    if move.split(' ')[0] == 'get':
        item = move[4:]
        if item in player.room.items:
            player.items.append(item)
            player.room.items.remove(item)
            print(f'You have picked up the {item}.')
            has_moved = True
        else:
            print('That is not a valid item')

    # if player enters drop command, ensure item is valid
    # then remove item from player and add it to room
    elif move.split(' ')[0] == 'drop':
        item = move[5:]
        if item in player.items:
            player.room.items.append(item)
            player.items.remove(item)
            has_moved=True
            print(f'You have dropped the {item}.')
        else:
            print('That is not a valid item')

    # defining remaining valid moves
    directions = ['n', 's', 'e', 'w']

    # if player entered a direction, move to the room in that direction
    if move in directions:
        change_rooms(move)
        has_moved = True

    # if player enters 'q' quit the game
    if move == 'q':
        print('Thanks for playing!')
        sys.exit(0)

    # if player has not moved yet, print error message
    if has_moved == False:
        print("That is an invalid move. To move, please enter 'n', 's', 'e', or 'w'.\n" \
        "To pick up or drop an item, please enter 'get [item]' or 'drop [item]\n" \
        "To quit the game, enter 'q'.")
