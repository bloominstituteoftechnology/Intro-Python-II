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

# Initializing list for item discovery
room_list = [key for key in room]

# Creating items for game
item = {
    'bottle' : Item('a bottle', 'an empty glass bottle'),
    'stick' : Item('a stick', 'a hefty knotted stick from a tree'),
    'book' : Item('a book', 'a strange book full of glyphs and writing in an unknown language'),
    'lantern' : Item('a lantern', 'a lantern lit with oil'),
    'coin' : Item('a single gold coin', 'a worn gold coin'),
    'key' : Item('a pewter key', 'a rusted pewter skeleton key'),
    'rug' : Item('a large rug', 'a large woven floor rug, intricate but worn and tattered')
}

# Item initialization
room['outside'].items = [item['lantern']]
room['foyer'].items = [item['bottle'], item['book']]
room['overlook'].items = [item['stick']]
room['narrow'].items = []
room['treasure'].items = [item['coin'], item['key']]


# Make a new player object that is currently in the 'outside' room.
print('\nWelcome to your quest, player... \n')
time.sleep(.5)
name_input = input('Please select a name for your character.\n')
player = Player(room['outside'], name_input)

# Introductory text
print(f'\n{player.name}?')
time.sleep(1)
print('\nWhat a strange name... ')
time.sleep(2)
print('\nAnyhow...\n')
time.sleep(1)
print(f'Hello, {player.name}.')
time.sleep(1)
print(f'\n{player.room}')
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
possible_choices = ['n', 'north', 'e', 'east', 's', 'south', 'w', 'west', 
                    'search', 'scan', 'look','get', 'pick', 'up', 'describe', 
                    'take', 'drop', 'leave', 'remove', 'use', 'room']  

cardinals = ['n', 'north', 'e', 'east', 's', 'south', 'w', 'west']

input_text = 'What would you like to do?'

decision = input(input_text)

# Main game loop
while 'quit' not in decision:
    matches = list(set(decision.split()).intersection(possible_choices))
    # print(matches[0])
    if len(matches) == 1:
        player.room = player.movement(matches[0][0])
        time.sleep(1)
        decision = input(input_text)
        
    elif len(matches) > 1:

        if matches[0] in ['search', 'scan', 'look']:
            print('You see the following items in the room: \n')
            print([item.item for item in player.room.items], '\n')
            decision = input(input_text)

        elif matches[0] in ['get', 'pick', 'up', 'take']:
            player.inventory.append(item[f'{decision.split()[-1]}'])
            player.room.items.remove(item[f'{decision.split()[-1]}'])
            print('You have picked up ', item[f'{decision.split()[-1]}'], '.\n')
            decision = input(input_text)

        elif matches[0] in ['drop', 'leave', 'remove']:
            player.room.items.append(item[f'{decision.split()[-1]}'])
            player.inventory.remove(item[f'{decision.split()[-1]}'])
            print('You have dropped ', item[f'{decision.split()[-1]}'], '.\n')
            decision = input(input_text)

        elif decision[0] == 'describe':
            print('It is a ', item[f'{decision[-1]}'].description, '.')

    elif decision == 'show inventory':
        print(player.player_inventory())
        decision = input(input_text)

    else:
        print("""Please select a valid command.\n 
        Example: 'Go north', 'pick up item', 'search room', or 'show inventory'""")
        decision = input(input_text)

print('\nYour quest has been abandoned... farewell.')