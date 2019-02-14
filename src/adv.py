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

print(f"\nGreetings {player.playerName}, you can control your adventure using the keys: N, E, S, W to move around the dungeon and Q to end your time here")


game_over = False

while game_over == False:

    player_move = input("\n[N] North, [E] East, [S] South, [W] West, [Q] Quit, [I] Items >> ").upper()

    if player_move == 'I':
        item_input = input("[Drop] or [Take] [Item] >> ").upper()
        
        if item_input == 'DROP SWORD':
            print('Sword has been dropped')
            

    if player_move == 'N' or player_move == 'E' or player_move == 'S' or player_move == 'W' or player_move == 'Q':

        if player_move == 'N' and player.currentRoom.n_to != None:
            player.currentRoom = player.currentRoom.n_to
            print(player.currentRoom)

        elif player_move == 'E' and player.currentRoom.e_to != None:
            player.currentRoom = player.currentRoom.e_to
            print(player.currentRoom)
        
        elif player_move == 'S' and player.currentRoom.s_to != None:
            player.currentRoom = player.currentRoom.s_to
            print(player.currentRoom)

        elif player_move == 'W' and player.currentRoom.w_to != None:
            player.currentRoom = player.currentRoom.w_to
            print(player.currentRoom)

        elif player_move == 'N' and player.currentRoom.n_to == None or player_move == 'E' and player.currentRoom.e_to == None or player_move == 'S' and player.currentRoom.s_to == None or player_move == 'W' and player.currentRoom.w_to == None:
            print('This seems to be the wrong way, please choose a different direction')

        elif player_move == 'Q':
            print("Good bye!")
            game_over = True

    else:
        print('Invalid command, please choose from the given options')
