from room import Room
from player import Player
from os import system, name

# A function that clears the console for the user


def clearScr():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
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

# This is creating
clearScr()
player_name = ''
while player_name == '':
    player_name = input("Please enter your name: ")


player = Player(player_name, room['outside'])
print('You are entering at your own risk! Type q to quit now!')
print('Hello', player.name + '!', 'You are in', player.current_room)
print('Now choose where you would like to explore!')
directions = {
    'n': 'North',
    's': 'South',
    'e': 'East',
    'w': 'West',
    'q': 'Quit'
}

direction = ''

# Confirms user has not quite and tells the user to choose direction
options = ''

for opt_direction in directions:
    options += f'\n Choose {directions[opt_direction]} enter "{opt_direction}"'

print(options)
while direction != 'q':
    direction = input('Which way would you like to go? ')
    try:
        chosen = f'You chose  {direction}, Now lets go {directions[direction]}'
        if direction == 'n':
            print(chosen)
            player.current_room = player.current_room.n_to
            print('You are in', player.current_room)
        elif direction == 's':
            player.current_room = player.current_room.s_to
            print('You are in', player.current_room)
        elif direction == 'e':
            player.current_room = player.current_room.e_to
            print('You are in', player.current_room)
        elif direction == 'w':
            player.current_room = player.current_room.w_to
            print('You are in', player.current_room)
        elif direction == 'q':
            print('See you later, Thanks for playing!')
    except KeyError:
        print("Please enter valid key option")
    except AttributeError:
        print('Please choose a valid direction!')

# The above code is not complete for testing purposes
# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
