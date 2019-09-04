from room import Room
from player import Player
import textwrap

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

player1 = Player("Player One", "outside")
direction = ''


def ask_for_location():
    global direction
    direction = input("Choose the direction you want to go next: w, n, e, s \nTYPE HERE: ")
    startGame(direction)

def describe_the_room():
    for key, value in room.items():
        if player1.current_room == key:
            print(f"Current Room: \n      {key} \n{value}")
            
    

def startGame(direction):
    if player1.current_room == "outside":
        if direction == 'n':
           player1.current_room = "foyer"
           describe_the_room()
           ask_for_location()
        else:
            print ("You hit the wall, try again. You can only go North from outside.")
    elif player1.current_room == "foyer":
        if direction == 's':
           player1.current_room = "outside"
           describe_the_room()
           ask_for_location()
        else:
            print(f"player1 {player1.current_room}")
        
describe_the_room()
ask_for_location()
    