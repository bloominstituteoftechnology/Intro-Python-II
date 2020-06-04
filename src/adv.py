from room import Room
from player import Player
from item import Item

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
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


items = {
    'chocolate': Item('chocolate', 'eat to regain strength to code'),
    'peanut butter': Item('peanut butter', 'the power food that never spoils'),
    'book': Item('book', 'to strengthen the mind and the soul'),
    'highlighter': Item('highlighter', 'to highlight the pertinent parts of your book'),
    'computer': Item('computer', 'to code until you cannot code anymore')
}

room['outside'].add_item(items['highlighter'])
room['foyer'].add_item(items['book'])
room['foyer'].add_item(items['computer'])
room['narrow'].add_item(items['chocolate'])
room['treasure'].add_item(items['peanut butter'])

#
# Main
#
player1 = Player('player1', room['outside'])

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.
while True:
    command = input(
        'Enter a direction using the keys n,s,e,w to go to different rooms, q to quit the game, i to see items, g to get items, or d to drop items. ').lower()

    if command == 'n':
        if player1.current_room.n_to != None:
            player1.current_room = player1.current_room.n_to
            print(
                f'room:{player1.current_room.name} \n description: {player1.current_room.description}')
        else:
            print('You cannot move north')
    elif command == 's':
        if player1.current_room.s_to != None:
            player1.current_room = player1.current_room.s_to
            print(
                f'room:{player1.current_room.name} \n description: {player1.current_room.description}')
        else:
            print('You cannot move south')
    elif command == 'e':
        if player1.current_room.e_to != None:
            player1.current_room = player1.current_room.e_to
            print(
                f'room:{player1.current_room.name} \n description: {player1.current_room.description}')
        else:
            print('You cannot move east')
    elif command == 'w':
        if player1.current_room.w_to != None:
            player1.current_room = player1.current_room.w_to
            print(
                f'room:{player1.current_room.name} \n description: {player1.current_room.description}')
        else:
            print('You cannot move west')
    elif command == 'i':
        if len(player1.current_room.items) > 0:
            for i in player1.current_room.items:
                print(f'name: {i.name} \n description: {i.description}')
    elif command == 'q':
        quit()
