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

room['outside'].items.append(items['highlighter'])
room['foyer'].items.append(items['book'])
room['foyer'].items.append(items['computer'])
room['narrow'].items.append(items['chocolate'])
room['treasure'].items.append(items['peanut butter'])

#
# Main
#
user = Player('Totoro', room['outside'], inventory=None)

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
    print(
        f"\n\nWelcome {user.name}!\n You are currently standing in the {user.current_room}")

    direction = input(
        "Choose a direction (n, s, e, w) and enter q to end the game: ").lower()

    if direction in ['n', 's', 'e', 'w']:
        user.current_room = user.move_to(direction, user.current_room)
        continue
    elif direction == 'q':
        print('Have a great day!')
        break
    else:
        direction != 'n' or 's' or 'w' or 'e' or 'q'
        print("Please enter a valid command")
