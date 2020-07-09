from room import Room
from player import Player
from textwrap import TextWrapper

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

player1 = Player("matt", "outside")
# print(player1)

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


def player_input():
    return int(input("[1] North [2] South [3] East [4] West [9] Quit"))


input = player_input()


def move():
    print(player1.current_room)
    print("What is your next move???")
    global input
    input = player_input()


def bad_move():
    print("Sorry, you can't move in that direction. Please try another move!")
    global input
    input = player_input()


while not input == 9:
    if player1.current_room == room['outside']:
        if input == 1:
            player1.current_room = room["outside"].n_to
            move()
        else:
            bad_move()
    elif player1.current_room == room['foyer']:
        if input == 1:
            player1.current_room = room['foyer'].n_to
            move()
        elif input == 2:
            player1.current_room = room['foyer'].s_to
            move()
        elif input == 3:
            player1.current_room = room['foyer'].e_to
            move()
        else:
            bad_move()
    elif player1.current_room == room['overlook']:
        if input == 2:
            player1.current_room = room['overlook'].s_to
            move()
        else:
            bad_move()
    elif player1.current_room == room['narrow']:
        if input == 1:
        player1.current_room = room['narrow'].n_to
        move()
        elif input == 4:
            player1.current_room = room['narrow'].w_to
