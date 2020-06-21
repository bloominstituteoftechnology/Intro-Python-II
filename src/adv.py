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

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

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

player = Player('You', 'outside')

def print_controls():
    print('\nControls:')
    print(' n for north \n s for south \n e for east \n w for west')
    print(' c to see the controls')
    print(' r to see the room you are in')
    print(' q to exit game')

choices = ['n', 's', 'e', 'w', 'c', 'r', 'q']

print('\n______ Treasure Cave 1 ______ \nFind the treasure and it could be yours')
print_controls()
# player.name = input('\nEnter your name: ')
choice = 0

lantern = Item('lantern', 'This lantern will help light the way')
room['overlook'].add_item(lantern)

print(f'\n  You are standing at the {room[player.location].name} \n\n  {room[player.location].description}')

while choice != 'q':
    choice = input('\nChoose a direction: ')
    try:
        if choice == 'n':
            player.location = room[player.location].n_to
            print(f'\n  You walk north into the {room[player.location].name} \n\n  {room[player.location].description}')
            if len(room[player.location].items) is not 0:
                print(f'\n  You see a {room[player.location].items[0]}')

        if choice == 's':
            player.location = room[player.location].s_to
            print(f'\n  You walk south into the {room[player.location].name} \n\n  {room[player.location].description}')
            if len(room[player.location].items) is not 0:
                print(f'\n  You see a {room[player.location].items[0]}')
        
        if choice == 'e':
            player.location = room[player.location].e_to
            print(f'\n  You walk east into the {room[player.location].name} \n\n   {room[player.location].description}')
            if len(room[player.location].items) is not 0:
                print(f'\n  You see a {room[player.location].items[0]}')
        
        if choice == 'w':
            player.location = room[player.location].w_to
            print(f'\n  You walk west into the {room[player.location].name} \n\n   {room[player.location].description}')
            if len(room[player.location].items) is not 0:
                print(f'\n  You see a {room[player.location].items[0]}')

        if choice == 'c':
            print_controls()

        if choice == 'r':
            print(f'\n  You are in the {room[player.location].name} \n\n   {room[player.location].description}')

        if choice not in choices:
            print('\n   That is not a direction.  Type c to see the controls')

    except:
        print("\n   You can't go that way")
