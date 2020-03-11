from room import Room
from player import Player
from items import Item 

from random import choice

# Declare items
item_dict = {
    'stone':'not very valuable, but you could throw it', 
    'coin':'looks like gold!', 
    'cobweb':'not pleasant', 
    'bone':'could make some bone broth with it..', 
    'gem':'ooo, sparkly!', 
    'book':'cannot read. better consult a wizard about the contents', 
    'sword':'pointy'}
game_items = [Item(k,v) for k,v in item_dict.items()]

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [choice(game_items)]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [choice(game_items) for i in range(2)]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [choice(game_items) for i in range(4)]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [choice(game_items) for i in range(4)]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [choice(game_items) for i in range(6)]),
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

# Make a new player object that is currently in the 'outside' room.
player = Player('Sam', room['outside'])

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


# function for player commands
def player_command(input_text):
    opposite_directions = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

    if input_text == 'q': 
        print('gg')
        exit()  

    elif input_text in opposite_directions.keys():
        location = eval(f'player.location.{opposite_directions[input_text]}_to')
        if location:
            player.location = location
        else:
            print("You can't go there. Try another direction or command..")

    elif input_text == 'look around':
        location_items = '\n'.join([item.name for item in player.location.items])
        if len(location_items)==0:
            print('there are no items in this area..')
        else:
            print(f'you see these items: \n{location_items}')

    elif 'get' in input_text:
        try:
            requested_item = next(i for i in player.location.items if i.name in input_text)
            player.items.append(requested_item)
            player.location.items.remove(requested_item)
            print(f'you added a {requested_item.name} to your inventory!')
        except:
            pass

    elif 'drop' in input_text:
        try:
            dropped_item = next(i for i in player.items if i.name in input_text)
            player.items.remove(dropped_item)
            player.location.items.append(dropped_item)
            print(f'you dropped a {dropped_item.name}!')
        except:
            pass

    else:
        print('Try another command..')

while True:
    print(f' Current locationn: {player.location.name} '.center(100, '-'))
    print(f' Location description: {player.location.description} '.center(100, '-'))

    text = input('---> ')
    player_command(text)
