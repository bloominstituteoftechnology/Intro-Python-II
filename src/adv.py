from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons.  A few stalactites and stalagmites dangle from the ceiling and floor", rm_layout = """
          ____  _ ________  ___   _
        VV    VV / _ \\   VV   VVV V
                / / \\ \\
               / /   \\ \\
    ^ ^^^^ ^ /  /     \\ \\^^^^^^
    ^^ ^  ^        x        ^^^^^   ^^^
"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", rm_layout = """
                     | |
        ___/ \\_______| |         __
       |               |        /
        \\       x      |_______/  /
         >_______  _______________/
                 | |
                    
"""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", rm_layout = """
                                              ()
    _______x____                    __________||
               |                   |
               |                   |
               |                   |
               |                   |
               |                   |
"""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", rm_layout = """
               | |
               | |
               | |
    __________/  |
    ______x______/
        
"""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south. A dusty key lies in the middle 
of the floor, with an ornate handle with a socket, presumably once holding a gem""", rm_layout = """
      __________________
     /                 \\
     |                  |
     |       k          |
     |         x        |
     \\_______  _______/
              ||       

""", items = [Item('ornate key', '''a long-handled key with a socket missing a gem.  
Something was etched here, long ago, but it has long since faded'''), Item('gold piece', '''all 
that is left of the old treasure...''')] ),

    'path': Room("Pathway", """The pathway has been winding slowly down and around 
for some time, becoming steeper and steeper until it finally terminates here, at 
this small hill.  Above you, you see the hill flatten, and a dark hole yawning above it. """, rm_layout = """
_______________\\             |  |   
                \\___    _____|  |
               _____/   /
              \\_____x_/
""")
}

# Link rooms together
room['outside'].s_to = room['path']
room['path'].n_to = room['outside']
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

Player_1 = Player('Player 1', char_class ='spelunker', location = room['path'])

# Write a loop that:
# print current room
user_input = (input('You approach the cavern.. Could the stories of treasure and crime..and worse... be true?? \n[N]orth\n\n'))

while not user_input == 'q':
    if user_input in ['n', 'north']:
        print('You Head North...')
        Player_1.move_location(Player_1.location.n_to)
        print(Player_1.location)
    
    elif user_input in ['s', 'south']:
        print('You head South...')
        Player_1.move_location(Player_1.location.s_to)
        print(Player_1.location)
    
    elif user_input in ['e', 'east']:
        print('You head East...')
        Player_1.move_location(Player_1.location.e_to)
        print(Player_1.location)
    
    elif user_input in ['w', 'west']:
        print('You head West')
        Player_1.move_location(Player_1.location.w_to)
        print(Player_1.location)
    
    elif user_input in ['x', 'inspect self', 'me']:
        print(Player_1)
    
    elif user_input in ['l', 'look', 'look at items']:
        print(f'in this room, you find... \n{[x.name for x in Player_1.location.items]}')

    else:
        print('Invalid selection.  Please try again!')
        print(Player_1.location)
    user_input = (input('Where do you want to do? \n\n GO: [N]orth  [S]outh  [E]ast  [W]est\nDO:[X]amine self  [I]nventory  [L]ook at items [Q]uit\n\n')).lower()

    #quit option
if user_input == 'q':
    raise SystemExit


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.


# If the user enters "q", quit the game.