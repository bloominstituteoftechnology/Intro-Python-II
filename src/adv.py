from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 
                     [Item("Note", "A tattered note with hastily scrawled, unrecognizable text."),]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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
player = Player(room['outside'], [])

# print(player1.room.name)

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

def check_move(direction, room):
    attribute = direction + '_to'
    if hasattr(room, attribute):
        return getattr(room, attribute)
    else:
        print("You can't find a way to move in that direction.")
        return room

print("You are standing in the " + player.room.name + ".")

print(player.room.description)
print(player.room.items[0].name)
print("What would you like to do?")

action = input("[N] Move North [E] Move East [S] Move South [W] Move West [Q] Quit\n").lower()

while not action == 'q':
    
    print("What would you like to do?")
    
    print(player.room.description)
    
    action = input("[N] Move North [E] Move East [S] Move South [W] Move West [Q] Quit\n").lower()

    if action == 'n' or action == 'e' or action == 's' or action == 'w':
        player.room = check_move(action, player.room)
    else: 
        print("Unrecognized input, please try again.")

    
