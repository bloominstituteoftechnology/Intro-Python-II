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

# Check Room class is being called correctly
# for x, i in room.items():
#     print(x)

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
name = input("What is your adventurer's name? ")
player = Player(room['outside'], name)

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


game_over = False

while game_over == False:

    player_move = input("[n] North, [e] East, [s] South, [w] West, [q] Quit >> ")

    if player_move == 'n' or player_move == 'e' or player_move == 's' or player_move == 'w' or player_move == 'q':

        if player_move == 'n' and player.currentRoom.n_to != None:
            player.currentRoom = player.currentRoom.n_to
            print(player.currentRoom)

        elif player_move == 'e' and player.currentRoom.e_to != None:
            player.currentRoom = player.currentRoom.e_to
            print(player.currentRoom)
        
        elif player_move == 's' and player.currentRoom.s_to != None:
            player.currentRoom = player.currentRoom.s_to
            print(player.currentRoom)

        elif player_move == 'w' and player.currentRoom.w_to != None:
            player.currentRoom = player.currentRoom.w_to
            print(player.currentRoom)

        elif player_move == 'n' and player.currentRoom.n_to == None:
            print('This seems to be the wrong way, please choose a different direction')

        elif player_move == 'e' and player.currentRoom.e_to == None:
            print('This seems to be the wrong way, please choose a different direction')
        
        elif player_move == 's' and player.currentRoom.s_to == None:
            print('This seems to be the wrong way, please choose a different direction')

        elif player_move == 'w' and player.currentRoom.w_to == None:
            print('This seems to be the wrong way, please choose a different direction')

        elif player_move == 'q':
            print("Good bye!")
            game_over = True

