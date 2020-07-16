from room import Room
from player import Player
from item import Item
import helpers

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
    'Sword': Item('sword', 'A Sharp sword'),
    'Axe': Item('axe', 'A deadly Viking Battleaxe'),
    'Staff': Item('staff', 'A Magic Staff'),
    'Crystal': Item('crystal', 'A Magic Crystal')

}

# print("N_TO!", room['outside'].n_to)

print()

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Khajit',  room['outside'])


# Nlocation = room[player1.current_room].n_to


# print('Player1 N_TO!', Nlocation)


# print("NTO", player1.current_room.n_to)

SLocation = player1.current_room.s_to

print('PLAYER1 S_TO!', SLocation)

player2 = Player('Nord',   'foyer')

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
play = str(input('Which way to Travel?\n press N for North, \n S for South,\n W for west,\n E for East \n or Q for quit.'))


while True:
    print(player1.name, 'is located', player1.current_room)

    play = str(input(
        'Which way to Travel?\n press N for North, \n S for South,\n W for west,\n E for East \n or Q for quit.'))
    if play == 'q':
        break
    if play == 'n':
 
        if player1.current_room.n_to :
            player1.current_room = player1.current_room.n_to
        else:
            print('cannot go that way.')
            print()

    if play == 's':
        if player1.current_room.s_to :
            player1.current_room = player1.current_room.s_to
        else:
            print('cannot go that way.')
            print()
    if play == 'w':
        if player1.current_room.w_to:
            player1.current_room = player1.current_room.w_to
        else:
            print('cannot go that way.')
            print()
    if play == 'e':
        if player1.current_room.e_to:
            player1.current_room = player1.current_room.e_to
        else:
            print('cannot go that way.')
            print()
