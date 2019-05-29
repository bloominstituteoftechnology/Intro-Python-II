from room import Room
from player import Player
import textwrap as textwrap
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

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'], 'Michael')


def print_items(items):
    for item in items:
        print(item)


print(player)
while True:
    print(textwrap.dedent(
        f"""\
        You are in room {player.room.name}
        {player.room.description}!
        The items in this room are: {print_items(player.room.items)}\
        """))
    print(textwrap.dedent('''
            What would you like to do?
            [n] Go North [s] Go South [e] Go East [w] Go West [q] Quit
        '''))
    command = input("\n>").lower().split()
    if len(command) == 1:
        # user has passed a direction
        if command[0] == 'n':
            print("you chose n")
            player.room = player.room.n_to
        elif command[0] == 's':
            print("you chose s")
            player.room = player.room.s_to
        elif command[0] == 'e':
            print("you chose e")
            player.room = player.room.e_to
        elif command[0] == 'w':
            print("you chose w")
            player.room = player.room.w_to
        elif command[0] == 'q':
            print("Thanks for Playing!")
            break
        else:
            print("Not a valid direction!")

    elif len(command) == 2:
        # user has passed two word command to interact with items
        if command[0] == "get" or "take":
            print(player.room.name)
    else:
        print("Sorry, I don't know that command")
        continue
# # Write a loop that:
# # * Prints the current room name
# # * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.
# #
# # If the user enters a cardinal direction, attempt to move to the room there.
# # Print an error message if the movement isn't allowed.
# #
# # If the user enters "q", quit the game.
