from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ()),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ()),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ()),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ()),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", (Item("Club", "Blunt wooden weapon"), Item("Sword", "Damaged and rusted iron sword"))),
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

def game():  
# Make a new player object that is currently in the 'outside' room.
    player = Player(room['outside'])
    currRoom = 'outside'
    print(player)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    print('Game Options:')
    direction = input('[N] North [S] South [E] East [W] WEST [Q] Quit\n').upper()
    while not direction == 'Q':
        if (direction == 'N') and (player.room == room['outside'] or player.room == room['narrow'] or player.room == room['foyer']):
            player.room = room[currRoom].n_to
        elif direction == 'S' and (player.room == room['foyer'] or player.room == room['treasure'] or player.room == room['overlook']):
            player.room = room[currRoom].s_to
        elif direction == 'E' and (player.room == room['foyer']):
            player.room = room[currRoom].e_to
        elif direction == 'W' and (player.room == room['narrow']):
            player.room = room[currRoom].w_to
        else:
            print('Could not move in that direction')
        if len(player.room.items) > 0:
            for item in player.room.items:
                print(item.name)
        currRoom = list(room.keys())[list(room.values()).index(player.room)]
        print(player)
        print('Game Options:\n')
        direction = input('[N] North [S] South [E] East [W] WEST [Q] Quit\n').upper()

game()

#
# If the user enters "q", quit the game.
