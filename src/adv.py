from room import Room
from player import Player
from item import Item

# Declare items for various location.
rock = Item('rocks', 'Rock on the ground')
stick = Item('sticks','Wooden stick')
torch = Item('torch', 'Torch on the wall')
chest = Item('chest','Rusty opened chest')

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",[rock, stick]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [torch]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [chest]),
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

def isActionable(cmd):
    tokenList = cmd.split()

    if len(tokenList) == 2 :
        for token in tokenList:
            if token in player.capability:
                return True
            else:
                return False
    else:
        print('Missing or too many arguments. Correct action example: "take rock" ')
        return False

#
# Main
#

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

player = Player("Fool",room["outside"])
#room['outside'].items.append('Rock')


while True:
    print(player)
    cmd = input('---> ')
    
    if (cmd == 'q'):
        break
    elif cmd in ['n','s','e','w']:
        player.travel(cmd)
    elif isActionable(cmd):
        player.action(cmd)
    else:
        print(f'*****\n\
        Valid Direction: n-move north, s-south, e-east, w-west\n\
        Valid Command: {player.capability}\n\
        To quit: q\n*****\n')


