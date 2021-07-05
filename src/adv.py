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
# player
player_1 = Player('Jim', room['outside'])

print(room['outside'])
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

# for name in room:
#         if player_1.current_room.name == room[name].name:
#             print()

# print(player_1)
direction = input(
    'Where do you want to go \n  N, S, E, W, Q (please use single letter only Q is to quit)').lower().strip()


flag = True


while flag:
    current_room = player_1.current_room
    print("Your current location:", player_1.current_room.name)
    print(player_1.current_room.description)
    direction = input(
        'Where do you want to go \n  N, S, E, W, Q (please use single letter only Q is to quit)').lower()
    if direction == 'n' and player_1.current_room != None:
        player_1.current_room = current_room.n_to
        print('GOING north')
    elif direction == 's' and player_1.current_room.s_to != None:
        player_1.current_room = current_room.s_to
        print('HEADING south')
    elif direction == 'e' and player_1.current_room.e_to != None:
        player_1.current_room = current_room.e_to
        print('MOVING east')
    elif direction == 'w' and player_1.current_room.w_to != None:
        player_1.current_room = current_room.w_to
        print('TRAVELING west')
    elif direction == 'q':
        print('You Were Never my friend')
        break
