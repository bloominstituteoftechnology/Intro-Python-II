from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
    "North of you, the cave mount beckons", ['toast']),

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

item_list = {
    'toast':  Item("toast", """A little burnt piece 
of bread. Better hang on to it!""", """You swallow 
the burnt toast in one gulp and immediatly regret 
the decision you just made. The horrible taste will 
haunt you to the grave.""")
}

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
    print("\nDebugging input string ", s, '\n')

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

    elif s[0][0] == 'g':
        grab_item(s[1])

    elif s[0][0] == 'd':
        drop_item(s[1])

    elif s[0][0] == 'u':
        use_item(s[1])

    elif s[0][0] == 'i':
        print('INVENTORY:', player1.inventory, '\n')

    elif s[0][0] == 'l':
        list_controls()

def attempt_move(direction):
    print('\nAttempted to move... \n')
    attribute = direction + '_to'

    if hasattr(player1.location, attribute):
        next_room = getattr(player1.location, attribute)
        player1.location = next_room
        return
    
    else:
        wrong_direction()

# Handle item functions
def grab_item(item):
    global item_list

    try:
        player1.location.inventory.index(item)
        player1.location.inventory.remove(item)
        player1.inventory.append(item)
        print(item_list[item].description, '\n')

    except:
        print(item, 'is not here\n')

def drop_item(item):

    try:
        player1.inventory.index(item)
        player1.location.inventory.append(item)
        player1.inventory.remove(item)

    except:
        print(item, 'is not in your inventory\n')

def use_item(item):
    global item_list

    try:
        player1.inventory.index(item)
        player1.inventory.remove(item)
        print(item_list[item].usage, '\n')

    except:
        print('I do not see', item, 'in your inventory')
        

# make a function to print available controls
def list_controls():
    print('GAME CONTROLS')
    print('[M]ove: [N]orth, [S]outh, [E]ast, [W]est')
    print('[G]rab -item-, [D]rop -item-, [U]se -item-, [I]nventory')
    print('[Q]uit\n')


# MAIN

# Make a new player object that is currently in the 'outside' room.

current_room = room['outside']
game_active = True

# Prompt the player to name thier character and store it in a variable

char_name = input("Please name your hero to begin your quest:\n>")

# if char_name == '':
#     char_name = random_name()
char_name = random_name()

player1 = Player(char_name, current_room, [])

print(f'\nWelcome {player1.name}!\n')

list_controls()

# Write a loop that:

while game_active:

    # * Prints the current room name
    print(f'CURRENT LOCATION: {player1.location.name}')

    # * Prints the current description (the textwrap module might be useful here).
    print(f'-{player1.location.description}-')

    # Prints the current room inventory
    print("-Items in reach: ", player1.location.inventory, '-\n')

    # * Waits for user input and decides what to do.
    print('What will you do next?')
    print('Type [L]ist to view available commands')
    in_loop = input("\n>").lower()

    analize_input(in_loop)
    

    
