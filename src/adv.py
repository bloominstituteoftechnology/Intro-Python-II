# from room import Room
from room import (Room, valid_directions)
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
player_name = input('Enter Name Here: ')
player = Player(player_name, room['outside'])

print(room)

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


def is_direction(str):
    return str in valid_directions

print(f'Welcome {player.name}, press q at any time to quit')
print(f'You are currently {player.current_room.name}')
print(player.current_room.description)
current_room = player.current_room

while True:
    if current_room != player.current_room:
        print(player.current_room)
        current_room = player.current_room
    current_room = player.current_room
    user_input = input('Enter Your Direction? click n --> North, e --> East, s --> South or w --> West?: ')
    if user_input == 'q':
        break
    elif is_direction(user_input):
        player.move(user_input)
    else:
        print('Sorry that is not a valid command, please try again!')