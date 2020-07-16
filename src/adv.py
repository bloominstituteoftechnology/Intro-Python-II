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

#
# Main
#

# Items
sword = Item("sword", "A rusty, old sword.")
lantern = Item("Lantern", "Still has some light left to illuminate the dark!")
coins = Item("Coins", "Silver and gold coins")
arrow = Item("Arrow", "A single arrow. Where is the bow?")

# Add items to rooms
def add_items_to_rooms():
    room['outside'].add_item(sword)
    room['foyer'].add_item(lantern)
    room['outside'].add_item(arrow)
    room['overlook'].add_item(coins)

def items_in_current_room(room):
    if not room.items:
        print("This room appears to be empty!")
    else:
        print("There appears to be something here!")

add_items_to_rooms()
is_playing = True
player = Player(room['outside'])
wrongway = "You cannot go that way!"

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

while is_playing:
    print(f'\nCurrent location: {player.room.name}')
    print(player.room.description, "\n")

    items_in_current_room(player.room)
    direction = input('Which way would you like to go?\n`n` for North, `e` for East, `s` for South, `w` for West, `q` to quit\nEnter selection here:  ')

    try:
        if direction == 'n':
            player.room = player.room.n_to
    except:
        print(wrongway)

    try:
        if direction == 'e':
            player.room = player.room.e_to
    except:
        print(wrongway)

    try:
        if direction == 's':
            player.room = player.room.s_to
    except:
        print(wrongway)

    try:
        if direction == 'w':
            player.room = player.room.w_to
    except:
        print(wrongway)

    if direction == 'q':
        print("\n\nGame over!")
        is_playing = False
