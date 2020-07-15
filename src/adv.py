import re
from room import Room
from player import Player

cardinals = re.compile('north|south|east|west', re.IGNORECASE)
shortCards = re.compile('nesw', re.IGNORECASE)

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

"""
          *light*
        /\/\/\/\/\/
        [overlook ]         [treasure]
            | |                 | |
        [  foyer  ]   <==>  [ narrow ]
            | |
        [ outside ]
"""

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("Welcome. What is your name, traveler?\n: ")
player = Player(name, room['outside'])

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


def movePlayer(player, direction):
    """ Checks to see if there is a room in the direction the player wants
       to move, and moves them if there is """
    if direction == "n" and player.inRoom.n_to != None:
        player.inRoom = player.inRoom.n_to
        return True
    elif direction == "e" and player.inRoom.e_to != None:
        player.inRoom = player.inRoom.e_to
        return True
    elif direction == "s" and player.inRoom.s_to != None:
        player.inRoom = player.inRoom.s_to
        return True
    elif direction == "w" and player.inRoom.w_to != None:
        player.inRoom = player.inRoom.w_to
        return True
    else:
        return False


selection = ''
print(f'\n\nWelcome, {player.name.capitalize()}')
print(player.inRoom)
while not selection == 'q':
    # check current input and take action, if possible
    if selection == 'n' or selection == 'e' or selection == 's' or selection == 'w':
        if movePlayer(player, selection):
            print("\n\n\n\n\n")
            print(player.inRoom)
        else:
            print('There is no path leading in that direction.')
    elif selection == '?':
        print(
            'Please enter the direction you wish to travel: [N]orth, [E]ast, [S]outh, or [W]est.')
    elif selection == 'bad':
        print('That is not a valid choice. Please try again. Enter ? for help. Enter Q to quit.')

    # get next input and validate
    print('What do you want to do?')
    s = input(': ')
    if s != '':
        sl = s.lower().split(' ')   # lowercase and split the string
        if len(sl) == 1:
            # `verb-only` selection
            if cardinals.match(sl[0]) or sl[0] == 'n' or sl[0] == 'e' or sl[0] == 's' or sl[0] == 'w':
                # take the first letter of the input string
                selection = sl[0][0]
            elif sl[0] == 'q' or sl[0] == '?':
                selection = sl[0]
            else:
                selection = 'bad'
        elif len(sl) > 1:
            # implement `verb noun` selection here
            selection = 'bad'   # not really but just for now
        else:
            selection = 'bad'
