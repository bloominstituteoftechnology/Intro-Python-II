from player import Player
from room import Room
import random


print('Welcome to "Where the heck are my keys?!!!"')
print()
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you,
    falling into the darkness. Ahead to the north,
    a light flickers in the distance,
    but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from
    west
to north. The smell of cmdld permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

name_add = ['Forgetful', 'Scatter Brain', 'Wandering', 'Air Head', 'Goofy']
name_in = input('What do they call you?')
name = random.choice(name_add) + ' ' + name_in
print()
print(f'OK we will call you {name}')
print()
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# dirs = ['n', 's', 'e', 'w']
player1 = Player(name, room['outside'])
go = input(f"""You'd better start looking for those keys
{player1.name} or you will be late to work! You are currently in
{player1.current_room}. To move North press the [n] key, to move South
 press the [s] key, to move East press the [e] key and to move west press the
[w] key.To quit at any point please press the [q] key. Enjoy! \n""")

# if u_in not in dirs:
#     print(f"Please press one of the ddirections {dirs} to continue")
# else:
#     p_location = player1.room
#     print(f'You arrive at {p_location}')
#     print(p_location.description)


def move(u_in, player1):
    error1 = f'''You done messed up {name}! Please input a
            correct direction to move, You are at {player1.current_room}'''
    if u_in == 'n':
        if player1.current_room.n_to is not None:
            player1.current_room = player1.current_room.n_to
            return player1.current_room.description
        else:
            print(error1)
    elif u_in == 's':
        if player1.current_room.s_to is not None:
            return player1.current_room.s_to
        else:
            print(error1)
    elif u_in == 'e':
        if player1.current_room.e_to is not None:
            return player1.current_room.e_to
        else:
            print(error1)
    elif u_in == 'w':
        if player1.current_room.w_to is not None:
            return player1.current_room.w_to
        else:
            print(error1)
    elif u_in == 'q':
        print(f'Have fun on the bus {name}')


u_in = None
while u_in != 'q':
    print(player1.current_room, '\n')
    u_in = move(
        input('Press [n], [s], [e], [w] to move or [q] to quit \n'), player1)


# Make a new player object that is currently in the 'outside' room.

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
