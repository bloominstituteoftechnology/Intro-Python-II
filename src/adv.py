from room import Room
from player import Player
from drop import Drop
from direction import Direction
import os
import time

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

room['outside'].north = room['foyer']
room['foyer'].south = room['outside']
room['foyer'].north = room['overlook']
room['foyer'].east = room['narrow']
room['overlook'].south = room['foyer']
room['narrow'].west = room['foyer']
room['narrow'].north = room['treasure']
room['treasure'].south = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_a = Player("A", room['outside'])
room['foyer'].items.append(Item("X", "XXXXX"))
room['foyer'].items.append(Item("Y", "YYYY"))
room['overlook'].items.append(Item("Z", "ZZZ"))
room['outside'].items.append(Item("L", "LL"))
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
print_location(True)
def answer(input: str):
    input = input.lower()
    
    for direction in Direction:
        if input == direction.value:
            if player_a.allow(direction):
                player_a.move(direction)
                print_location(True)
            else:
                print("invalid move(type m to see map)")
            return

    if input == 'q':
        exit()
    elif input == 'm':
        show_map()
    elif input == 'b':
        if len(player_a.drops) > 0:
            print("f{player_a.drops}")
        else:
            print("no drops in bag")
    else:
        print("Please enter a valid key\nm: map\nb:bag\nq:exit")

def take_drop(input: str, obj: str):
    input = input.lower()
    obj = obj.lower()

    if input == "take":
        for item in player_a.room.drops:
            if obj == item.name.lower():
                player_a.pick_up(item)
                return

    elif input == "drop":
        for item in player_a.room.drops:
            if obj == item.name.lower():
                player_a.put_down(item)
                return

    else:
        print("invalid input(take to pick item up and drop to put item down)")

def quit():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_location():
    quit()
    print(player_a.room.name)
    print(player_a.room.description)

def show_map():
    quit()

    nothing = "invalid direction"
    north = player_a.room.north.name if player_a.room.north is not None else nothing
    south = player_a.room.south.name if player_a.room.south is not None else nothing
    west = player_a.room.north.west if player_a.room.west is not None else nothing
    east = player_a.room.north.east if player_a.room.east is not None else nothing

    print("Map".center(50, ' '))
    print(''.center(50, '='))

    print('\n' + north.center(50, ' '))
    for _ in range(5):
        print('|'.center(50, ' '))
    print(west, end='')
    print("You".center(50 - len(west) - len(east), '-'), end='')
    print(east)
    for _ in range(5):
        print('|'.center(50, ' '))
    print(south.center(50, ' '))

    print('\n' + "".center(50, '='))

    input("\nPress enter key to continue")
    print_location(False)

while True:
    message = input("\nEnter a command: ")
    print('')
    words = message.split()

    if len(words) == 1:
        answer(words[0])
    elif len(words) == 2:
        take_drop(words[0], words[1])

