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
p = Player(room['outside'])

print('Welcome to life. Please make a decision.')
print(p.current_room.name)
print(p.current_room.description)
print('What will you do with yourself?')

# print(room[p.current_room].name)


user = input("[n] North  [s] South  [e] East  [w] West  [q] Quit\n")

# Write a loop that:
# Prints the current room name
# * Prints the current description (the textwrap module might be useful here).


#gamplay loop
while not user == 'q':q
    if user == 'n':
        if  p.current_room.n_to != 'wall':
            p.current_room = p.current_room.n_to
            print(p.current_room.name)
            print(p.current_room.description)
            user = input("[n] North  [s] South  [e] East  [w] West  [q] Quit\n")
        else:
            print('There is nothing for you in this direction. Where-to now?')
            user = input("[n] North  [s] South  [e] East  [w] West  [q] Quit\n")
    elif user == 's':
        if  p.current_room.s_to != 'wall':
            print('got inside 2nd if loop')
            p.current_room = p.current_room.s_to
            print(p.current_room.name)
            print(p.current_room.description)
            user = input("[n] North  [s] South  [e] East  [w] West  [q] Quit\n")
        else:
            print('There is nothing for you in this direction. Where-to now?')
            user = input("[n] North  [s] South  [e] East  [w] West  [q] Quit\n")
    elif user == 'e':
        if  p.current_room.e_to != 'wall':
            print('got inside 2nd if loop')
            p.current_room = p.current_room.e_to
            print(p.current_room.name)
            print(p.current_room.description)
            user = input("[n] North  [s] South  [e] East  [w] West  [q] Quit\n")
        else:
            print('There is nothing for you in this direction. Where-to now?')
            user = input("[n] North  [s] South  [e] East  [w] West  [q] Quit\n")
    elif user == 'w':
        if  p.current_room.w_to != 'wall':
            print('got inside 2nd if loop')
            p.current_room = p.current_room.w_to
            print(p.current_room.name)
            print(p.current_room.description)
            user = input("[n] North  [s] South  [e] East  [w] West  [q] Quit\n")
        else:
            print('There is nothing for you in this direction. Where-to now?')
            user = input("[n] North  [s] South  [e] East  [w] West  [q] Quit\n")
    else:
        print("You must be confused by the limitations of this world. Try to find your way again.")
        user = input("[n] North  [s] South  [e] East  [w] West  [q] Quit\n")
