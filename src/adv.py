from room import Room
from player import Player

room = {
    'outside':  Room("Outside Cave Entrance","North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. 
    Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. 
    The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! 
    Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

# Map
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
wrongWay = "\n\nThere is no room in that direction!\n\n"

# Start Game
playGame = True
player = Player(room['outside'])

while playGame:

    print(f'\nCurrent location: {player.room.name}')
    print(player.room.description, "\n")
    direction = input('Which way would you like to go?\nn for North, e for East, s for South, w for West, q to quit\n')

    try:
        if direction == 'n':
            player.room = player.room.n_to
    except:
        print(wrongWay)

    try:
        if direction == 'e':
            player.room = player.room.e_to
    except:
        print(wrongWay)

    try:
        if direction == 's':
            player.room = player.room.s_to
    except:
        print(wrongWay)

    try:
        if direction == 'w':
            player.room = player.room.w_to
    except:
        print(wrongWay)

    if direction == 'q':
        print("\n\nGame over!")
        playGame = False

