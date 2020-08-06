from room import Room
from player import Player
from game_controller import GameController
from item import Item
from item import LightSource

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
room['outside'].s_to = None
room['outside'].e_to = None
room['outside'].w_to = None
torch_foyer = LightSource('burning touch', 'A wooden touch, which should burn for some time.')
room['outside'].items.append(torch_foyer)
room['outside'].isLit = True

room['foyer'].n_to = room['overlook']
room['foyer'].s_to = room['outside']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = None

room['overlook'].n_to = None
room['overlook'].s_to = room['foyer']
room['overlook'].e_to = None
room['overlook'].w_to = None

room['narrow'].n_to = room['treasure']
room['narrow'].s_to = None
room['narrow'].e_to = None
room['narrow'].w_to = room['foyer']

room['treasure'].n_to = None
room['treasure'].s_to = room['narrow']
room['treasure'].e_to = None
room['treasure'].w_to = None

#
# Main
#

done = False
game_controller = GameController()

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Drizzt', room['outside'])

# Write a loop that:
while not done:
    
    game_controller.enterRoom(player1)

    print(f'\n{player1}')

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
    print(f'\n{player1.current_room}')

# * Waits for user input and decides what to do.
    commands = input('> ').split(',')
    # print(f'verified commands: {commands}') # TESTING ONLY
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    for command in commands:
            game_controller.roomOperation(player1, command)