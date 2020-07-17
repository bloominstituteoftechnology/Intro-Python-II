from room import Room
from player import Player
from items import Item
import time

# Declare all the rooms

room = {
    'outside':  Room("outside the Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("in a Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("on the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("in a Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("in the Treasure Chamber", """You've found the long-lost treasure
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

item = {
    'bottle' : Item('bottle', 'An empty glass bottle'),
    'stick' : Item('stick', 'A hefty knotted stick from a tree'),
    'book' : Item('book', 'A strange book full of glyphs and writing in an unknown language'),
    'lantern' : Item('lantern', 'A lantern lit with oil'),
    'coin' : Item('gold coin', 'A worn gold coin'),
    'key' : Item('pewter key', 'A rusted pewter skeleton key')
}

# Make a new player object that is currently in the 'outside' room.
print('\nWelcome to your quest, player... \n')
time.sleep(1)
name_input = input('Please select a name for your character.\n')
player = Player(room['outside'], name_input)
print(f'\n{player.name}?')
time.sleep(2)
print('\nWhat a strange name... ')
time.sleep(2)
print('\nAnyhow...\n')
time.sleep(1)
print(f'Hello, {player.name}.')
time.sleep(1)
print(f'\n\n{player.room}')
time.sleep(1)

#------------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------

# Setting up cardinal directions and decision prompt
cardinals = ['n', 'e', 's', 'w']

input_text = 'Which direction would you like to move? \n\
    [n] North  [e] East  [s] South  [w] West  [q] Quit\n\n'

decision = input(input_text)

# Item initialization
outside_items = [item['lantern']]
foyer_items = [item['bottle'], item['book']]
overlook_items = [item['stick']]
narrow_items = []
treasure_items = [item['coin'], item['key']]
player_items = []


# Main game loop
while not decision == 'q':
    if decision in cardinals:
        player.room = player.movement(decision)
        time.sleep(1)
        decision = input(input_text)
    else:
        print('Please select a valid direction. \n\
            [n] North  [e] East  [s] South  [w] West  [q] Quit\n\n')
        decision = input(input_text)

print('\nYour quest has been abandoned... farewell.')