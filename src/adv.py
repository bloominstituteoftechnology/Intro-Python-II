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

#! Create the input command parser which allows the program to receive player input 
#! and commands to move to rooms in the four cardinal directions

player = Player("Player", room["outside"])


while True:
    player.current_room
    # * Prints the current room name
    print(f'{player.current_room}')


 
    print('Where would you like to go?')
    cmd = input('Please press N, S, E, W to choose a direction. Q will quit the game')

    if cmd == 'n':
        print('Heading North')
        if player.current_room.n_to is None:
            print('There is nothing north of you, please choose a new direction')
        else:
            player.current_room = player.current_room.n_to
                
    elif cmd == 's':
        print('Heading South')
        if player.current_room.s_to is None:
            print('There is nothing south of you, please choose a new direction')
        else:
            player.current_room = player_1.current_room.s_to
    
    elif cmd == 'e':
        print('Heading East')
        if player.current_room.e_to is None:
            print('There is nothing east of you, please choose a new direction')
        else:
            player.current_room = player_1.current_room.e_to
    
    elif cmd == 'w':
        print('Heading West')
        if player.current_room.w_to is None:
            print('There is nothing west of you, please choose a new direction')
        else:
            player.current_room = player_1.current_room.w_to

# Print an error message if the movement isn't allowed.
    else:
        print ('Movement not allowed, try something else')

# If the user enters "q", quit the game.    
    if cmd == 'q':
        print('Way to quit, loser') #* trying to spice things up lmao 
    break

        
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

#! All of this is done above? I will review when I am not so tired.

