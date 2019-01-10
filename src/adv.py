from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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

# Item List



# Create a function to give a player a random name if
# they leave it blank

def random_name():
    return 'Fanny Pack Shaman'

# A function to handle wrong direction
def wrong_direction():
    print('You can not go that way')

# Create a function that interprets the user input

def analize_input(string):
    global game_active
    s = string.lower().split(" ")
    print("Debugging input string ", s)

    if s[0][0] == 'q':
        print('\nAre you sure you wish to quit the game? [Y/N]\n')
        quit_game = input('>')
        if quit_game.lower() == 'y':
            game_active = False

    elif s[0][0] == 'm':
        if len(s) < 2:
            print('You must include a direction [N/S/E/W] when trying to move')
            return

        elif s[1][0] == 'n':
            attempt_move('n')
            
        elif s[1][0] == 'e':
            attempt_move('e')

        elif s[1][0] == 's':
            attempt_move('s')

        elif s[1][0] == 'w':
            attempt_move('w')
            
        else:
            print('You must include a direction [N/S/E/W] when trying to move')
            return

def attempt_move(direction):
    print('\nAttempted to move... \n')
    attribute = direction + '_to'

    if hasattr(player1.location, attribute):
        next_room = getattr(player1.location, attribute)
        player1.location = next_room
        return
    
    else:
        wrong_direction()



# MAIN

# Make a new player object that is currently in the 'outside' room.

current_room = room['outside']
game_active = True

# Prompt the player to name thier character and store it in a variable

char_name = input("Please name your hero to begin your quest:\n>")

if char_name == '':
    char_name = random_name()

player1 = Player(char_name, current_room, [])

print(f'\nWelcome {player1.name}!\n')

# Write a loop that:

while game_active:

    # * Prints the current room name

    print(f'Current location: {player1.location.name}')

    # * Prints the current description (the textwrap module might be useful here).

    print(f'-{player1.location.description}-\n')

    # * Waits for user input and decides what to do.
    print('Please choose an action')
    print('[M]ove: [N]orth, [S]outh, [E]ast, [W]est')
    print('[G]rab -item-, [D]rop -item-, [U]se -item-, [I]nventory')
    print('[Q]uit')

    in_loop = input("\n>").lower()

    analize_input(in_loop)
    

    
