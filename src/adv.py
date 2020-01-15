from room import Room
from player import Player
import sys

class InvalidMove(Exception):
    pass

class NoRoomThatDirection(Exception):
    pass


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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Scott', room['outside'])



# Write a loop that:
while(True):

    # printing room name and description
    print(player.room.name)
    print(player.room.description)

    try:
        # defining valid moves
        moves = ['n', 's', 'e', 'w', 'q']

        # get user move
        print('What would you like to do?')
        move = input().lower()
            
        # check that move is valid
        if move not in moves:
          raise InvalidMove
          
        # getting name of next room attribute corresponding to the user move
        attr = move+"_to"
        
        # check that there is a room in that direction
        if getattr(player.room, attr, 'error') == 'error':
            raise NoRoomThatDirection

        # updating room based on user move
        player.room = getattr(player.room,attr)
    
    except InvalidMove:
        # if move is invalid, print error message   
        print("That is an invalid move. To move, please enter 'n', 's', 'e', or 'w'.\n" \
                "To quit the game, enter 'q'.")
    
    except NoRoomThatDirection:
        # if there is no room that direction, print error message
        print("There's nowhere to go in that direction. Try another direction.")
    
    finally:
        # if player enters 'q' quit the game
        if move == 'q':
            print('Thanks for playing!')
            sys.exit(0)

#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
