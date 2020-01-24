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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


item = {
    "Sword" : Item('sword', 'a very sharp sword'),
    "Armor" : Item('armor', 'some very sturdy armor'),
    "Potion" : Item('potion', 'drink it and see what happens'),
    "Hammer" : Item('hammer', 'not a war hammer or anything, just a normal hammer someone seems to have left here'),
    "Wand" : Item('wand', 'a broken wand')
}

room['outside'].add_item(item['Sword'])
room['foyer'].add_item(item['Armor'])
room['overlook'].add_item(item['Potion'])
room['narrow'].add_item(item['Hammer'])
room['treasure'].add_item(item['Wand'])
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(input('Enter name'), room['outside'])


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

while True:
    input = input('\nWhere do you want to go? Enter n, s, e, or w. Press q to quit.\n')

    print(player)
    print(player.current_room.print_item())

    try:
        if input == 'n':
            if player.room.n_to !=0:
                player.room = player.room.n_to
            else:
                print('There is no room in that direction. Please select another direction')

        if input == 'e':
            if player.room.e_to !=0:
                player.room = player.room.e_to
            else:
                print('There is no room in that direction. Please select another direction')

        if input == 'w':
            if player.room.w_to !=0:
                player.room = player.room.w_to
            else:
                print('There is no room in that direction. Please select another direction')

        if input == 's':
            if player.room.s_to !=0:
                player.room = player.room.s_to
            else:
                print('There is no room in that direction. Please select another direction')

        if input == 'q':
            break

        if input == 'get':
            player.get_item(input)

        if input == 'drop':
            player.remove_item(input)
            player.room.add_item(input)
