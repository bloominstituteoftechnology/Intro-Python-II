from room import Room
from player import Player
from os import system, name
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

def clear(): 
    # for windows 
    _ = system('cls' if name == 'nt' else 'clear') 

# def start_game():
#     print(f'\n***** Welcome to Adventure Quest! *****')
#     print(f'\n[Q] -- Quit \n ')
# start_game()    
print("")
print("*************Adventure Quest!**********************")
print('---- Lets get started! -----')
player = Player(input('What is your name?'), room["outside"])    
cin = 'p'
    

while cin != 'q':     
    
    print(player)
    #1 create options to move
    #2 if correct option selected, move in that direction
    #3 if incorrect option, re prompt
    cin = input('''\n Which direction do you want to go? 
             \n           [N] - North 
             \nWest - [W]  O  [E] - East 
             \n           [S] - South 
             \n     ''')
    
    
    if cin == 'n':
        player.move(cin)
        # player.current_room = room['outside'].n_to
        # print(player)
        # print('''\n Which direction do you want to go? 
        #     \n           [N] - North 
        #     \nWest - [W]  O  [E] - East 
        #     \n           [S] - South 
        #     \n ''')
        
        
    elif cin == 'e':
        player.move(cin)
            # player.current_room = room['outside'].n_to
            # print(player)
        # print('''\n Which direction do you want to go? 
        #     \n           [N] - North 
        #     \nWest - [W]  O  [E] - East 
        #     \n           [S] - South 
        #     \n ''')
        
        
    elif cin == 's':
        player.move(cin)
            # player.current_room = room['outside'].n_to
            # print(player)
        # print('''\n Which direction do you want to go? 
        #     \n           [N] - North 
        #     \nWest - [W]  O  [E] - East 
        #     \n           [S] - South 
        #     \n ''')
        
        
    elif cin == 'w':
        
        player.move(cin)
            # player.current_room = room['outside'].n_to
            # print(player)
        # print('''\n Which direction do you want to go? 
        #     \n           [N] - North 
        #     \nWest - [W]  O  [E] - East 
        #     \n           [S] - South 
        #     \n ''')
        
        
    # elif cin != 'g' or 'G':
    #         print('')
    #         print('Please press [S] to start the game or [Q] to quit the game.')   
    #         print(f'\n[G] -- Start Game \
    #                 \n[Q] -- Quit \n ')
    #         cin = input('') 
            

    else:
        clear()
        print('You have quit the game')

        
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


