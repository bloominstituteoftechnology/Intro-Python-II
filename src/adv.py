from room import Room
from player import Player
from item import Item
from textwrap import wrap

# Welcome message
print('Welcome to "This Game!"\n')

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

# User inputs name
name = input('What is your name? ')

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

choices = ['n', 's', 'e', 'w']

# Make a new player object that is currently in the 'outside' room.
user = Player({name}, room['outside'])
go = input(f"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis et nulla in tortor maximus dignissim. 
            Phasellus elementum vestibulum nibh, vel congue risus. Praesent vitae mauris convallis, mollis enim non, 
            fermentum erat. Sed sed ex mi. Donec diam turpis, placerat eu ornare sed, ornare nec urna.
            To move North press the [n] key, to move South press the [s] key, to move East press the [e] key, to move 
            West press the [w] key. To quit the game press the [q] key. """)


# LOOP
cmd = None
while cmd != 'q':
    print(user.current_room, '\n')
    cmd = input('Press [n], [s], [e], [w] to move or [q] to quit\n')
    error_msg = f'''There is nowhere to go in that direction. Please select a valid direction to move. You are 
                    currently in {user.current_room}.'''
    if cmd == 'n':
        if user.current_room.n_to is not None:
            user.current_room = user.current_room.n_to
            print(user.current_room.description)
        else:
            print(error_msg)
    elif cmd == 's':
        if user.current_room.s_to is not None:
            user.current_room = user.current_room.s_to
            print(user.current_room.description)
        else:
            print(error_msg)
    elif cmd == 'e':
        if user.current_room.e_to is not None:
            user.current_room = user.current_room.e_to
            print(user.current_room.description)
        else:
            print(error_msg)
    elif cmd == 'w':
        if user.current_room.w_to is not None:
            user.current_room = user.current_room.w_to
            print(user.current_room.description)
        else:
            print(error_msg)
    elif cmd == 'q':
        print(f"Goodbye {name}!")
        break

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

# LOOP
# READ
# EVAL
# PRINT
