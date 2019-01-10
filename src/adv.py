from room import Room
from player import Player
from items import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'cliff':    Room("The Cliff",
                     "This feature comes from nowhere, you're dead. Try again."),

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
room['outside'].s_to = room['cliff']
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

# Make a new player object that is currently in

name = input('Hello n00b. What is your name?')
player = Player(name, room['outside'])
print('Welcome' + ' ' + name + ',' + 'let\'s start the adventure! \v')


def try_direction(direction, current_location):
    attribute = direction + '_to'

    if hasattr(current_location, attribute):
        return getattr(current_location, attribute)


while True:
    print(Player(player.name, player.current_location))
    print(player.current_location.room_name + '\v')
    print(player.current_location.room_description)
    print('Which direction do you choose? (n,s,e or w)')

    s = input("\n>").lower()[0]

    if s == 'n':
        player.current_location = player.current_location.n_to
    elif s == 's':
        player.current_location = player.current_location.s_to
    elif s == 'e':
        player.current_location = player.current_location.e_to
    elif s == 'w':
        player.current_location = player.current_location.w_to
    else:
        print("Not a valid direction! Enter a new direction.")

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
