#!/bin/env python3
from room import Room
from player import Player
from item import Item

# Declare all the rooms
h2g2 = Item(name="book",
            description='''An electronic tablet branded with the words "don't panic".''')
lightsword = Item(name="lightsword",
                  description="is that a lightsword?")

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [lightsword]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [h2g2]),

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

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']


#
# Main
#


def repl(name):
    """
    A loop that:

    * Prints the current room name.
    * Prints the current description.
    * Waits for user input and decides what to do.

    When the user enters a cardinal direction, <Player> will attempt to move to
    the room there. 

    An error message will print if the movement is not allowed.

    If the user enters "q", the game will quit.
    """
    cmd = "start"  # the first command for < Player > to evaluate.
    startAt = rooms['outside']  # < Player > starts here
    player1 = Player(room=startAt, name=name)  # create new < Player >

    while not (cmd in ["q", "quit"]):
        # EVALUATE
        player1.evaluate(cmd)
        # PRINT
        print(player1.status())  # show our < Player >'s current status.
        print(player1.look())  # scene from perspective of our < Player >
        # READ
        cmd = input("what now ? ").lower()  # ask user for the next command

    print(f'\nThanks for playing, goodbye')  # user has exited the REPL


if __name__ == "__main__":
    # Make a new player object that is currently in the 'outside' room.
    name = input("Please enter your name. ")
    if len(name) < 1:
        name = "𝝺 student"
    repl(name)
