from room import Room
from item import Item
from player import Player
from monster import Monster

# Declare and link the rooms
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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Make a new player object that is currently in the 'outside' room.

# player = Player(input('What is your name?\n'), 'outside')
player = Player('Debugger Steve', room['outside']) # Speed up tests!

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.

item_cmds = ['get','take','leave','throw','swing','eat','drink']
cardinals = ['n','e','w','s','north', 'east','west','south']
cmd = ''
print(f'Welcome {player.name}!\nGood luck on your adventure!\n')
while cmd != 'q':
    print('\n', player.current_room.description, '\n')
    print('Current Inventory:', player.inventory)
    print('Room Contents', player.current_room.contents)
    cmd = input("What do you do?\n").lower()
    split_cmd = cmd.split()
    if cmd in cardinals:
        try:
            player.change_room(cmd)
        except: 
            print('You cant go that way!\n')
    elif split_cmd[0] in item_cmds:
        try:
            player.item_interaction(split_cmd[0],split_cmd[-1])
        except:
            print('Can\'t use item in that way')
    else:
        print('not recognized')
        print('That\'s not possible!')  
print('Thanks for playing!')
