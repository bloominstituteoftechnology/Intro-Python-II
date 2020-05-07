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
player = Player('John', 'outside')

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

def find_key(value, my_dict):
    key_list = list(my_dict.keys())
    value_list = list(my_dict.values())
    return key_list[value_list.index(value)]

while True:
    print('\n','I am in the room {}'.format(player.current_room), '\n')
    # text = f'I am in the room of {player.current_room}. I do not know where to go now However. I will explore around to find a room for treasure.'
    # print(textwrap.wrap(text)[0])
    user_input = input('Please enter the direction to go (for exit, enter "q"): ')

    if user_input == 'q':
        break
    # print('user_input',user_input)
    if user_input == 'n':
        print('\n', 'going north')
        if  room[player.current_room].s_to != None:
            player.current_room = find_key(room[player.current_room].s_to, room)
            print('\n',f'now I am in {player.current_room}')
        else: 
            print('\n', 'no room is in the direction, please choose others')
            
    elif user_input == 's':
        print('\n', 'going south')
        if room[player.current_room].n_to != None:
            player.current_room = find_key(room[player.current_room].n_to, room)
            print('\n',f'now I am in {player.current_room}')
        else:
             print('\n', 'no room is in the direction, please choose others')

    elif user_input == 'e':
        print('\n', 'going east')
        if room[player.current_room].w_to != None:
            player.current_room = find_key(room[player.current_room].w_to, room)
            print('\n',f'now I am in {player.current_room}')
        else:
             print('\n', 'no room is in the direction, please choose others')
            
    elif user_input == 'w':
        print('\n', 'going west')
        if room[player.current_room].e_to != None:
            player.current_room = find_key(room[player.current_room].e_to, room)
            print('\n',f'now I am in {player.current_room}')
        else:
             print('\n', 'no room is in the direction, please choose others')
    else:
        print('Wrong key is entered, please try again')      


