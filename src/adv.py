from room import Room
from player import Player
from item import Item

import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     Item(["Sword of Destiny", 50])),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item(["Sword of Destiny", 50])),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item(["Sword of Destiny", 50])),
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


def newPlayer():
    races = ['Human', 'Ogre', 'Troll', 'Genie', 'Centaur']
    archetypes = ['Stealth', 'Brute', 'Priest', 'Mage', 'Pacifist']

    name = input("What would you like to be called, stranger? ")
    race = int(input(
        "What are you ??? 1 - Human, 2 - Ogre, 3 - Troll, 4 - Genie, 5 - Centaur "))
    archetype = int(input(
        "What's your archetype? 1 - Stealth, 2 - Brute, 3 - Priest, 4 - Mage, 5 - Pacifist "))

    return Player(name, races[race], archetypes[archetype], current_room=room['outside'])


player = newPlayer()


def checkMove(player):
    print(f'{player.current_room}')

    allotted_moves = player.move()

    dead_end = "You have reached a deadend please select another path!"
    move = ""

    while move not in allotted_moves.keys():
        move = input(
            'Where would you like to traver? N - North, S - South, E - East, W - West ').upper()
        if move == 'Q':
            print('Hope you enjoyed your visit!')
            sys.exit()

        try:
            if move == 'N':
                player.current_room = player.current_room.n_to
            if move == 'S':
                player.current_room = player.current_room.s_to
            if move == 'E':
                player.current_room = player.current_room.e_to
            if move == 'W':
                player.current_room = player.current_room.w_to
        except AttributeError:
            print(dead_end)

        return move


def get_or_drop_item(player):
    if player.current_room.items != None:
        if player.current_room.room_items() == None:
            pass
        else:
            print(player.current_room.room_items())
    else:
        pass


move_player = None

while move_player is not 'Q':
    move_player = checkMove(player)
    get_or_drop_item(player)
