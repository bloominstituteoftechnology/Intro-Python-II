from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# This allows me to 1. Make use of auto complete and 2. Avoid potential typo-related bugs
out = 'outside'
foy = 'foyer'
over = 'overlook'
nar = 'narrow'
trea = 'treasure'

br = '----------------------------'

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

def showDirections(current):
    north = "North: " + current.n_to.name if current.n_to != None else "There's no path North"
    east = "East: " + current.e_to.name if current.e_to != None else "There's no path East"
    sout = "South: " + current.s_to.name if current.s_to != None else "There's no path South"
    west = "West: " + current.w_to.name if current.w_to != None else "There's no path West"
    print()
    print(north)
    print(east)
    print(sout)
    print(west)
    print()

#
# Main
#
# Make a new player object that is currently in the 'outside' room.

player1 = Player("Hector", room[out])

pot = Item('HPPOT', 'HP Potion')
room[out].add_item(pot)


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while True:
    # print(br)
    print("Info:" + br)
    print(f"\tCurrent room: \t{player1.current_room.name}")
    print(f"\t\t{player1.current_room.description}")
    player1.current_room.items_in_room()

    choice = str(input("\nWhere do you want to go?\t"))


    if choice.lower().strip() == "n":
        player1.current_room = player1.current_room.n_to
    elif choice.lower().strip() == "e":
        player1.current_room = player1.current_room.e_to
    elif choice.lower().strip() == "s":
        player1.current_room = player1.current_room.s_to
    elif choice.lower().strip() == "w":
        player1.current_room = player1.current_room.w_to
    elif choice.lower().strip() == "m":
        showDirections(player1.current_room)
    elif choice.lower().strip() == "q":
        break

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


