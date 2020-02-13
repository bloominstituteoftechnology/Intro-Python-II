from src.room import Room
from src.directions import Direction
from src.player import Player

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

# Link rooms together
# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

room['outside'].nearby_rooms[Direction.North] = room['foyer']
room['foyer'].nearby_rooms[Direction.South] = room['outside']
room['foyer'].nearby_rooms[Direction.North] = room['overlook']
room['foyer'].nearby_rooms[Direction.East] = room['narrow']
room['overlook'].nearby_rooms[Direction.South] = room['foyer']
room['narrow'].nearby_rooms[Direction.West] = room['foyer']
room['narrow'].nearby_rooms[Direction.North] = room['treasure']
room['treasure'].nearby_rooms[Direction.South] = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
x = str(input("Enter player name: "))
player = Player(x, room['outside'])


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
def switch():
    print("Press n for North \n press s for South \n press e for East \n press w for West \n press q to Quit")

    player_option = str(input("\n where to next?: "))

    def North():
        player.move(Direction.North)

    def South():
        player.move(Direction.South)

    def East():
        player.move(Direction.East)

    def West():
        player.move(Direction.West)

    def quit():
        quit()

    def default():
        print("Incorrect option")

    dict = {
        "n": North,
        "s": South,
        "e": East,
        "w": West,
        "q": quit
    }.get(player_option, default)()

switch()