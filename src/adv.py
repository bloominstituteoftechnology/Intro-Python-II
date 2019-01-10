from room import Room
from player import Player
# from item import Item
import textwrap as textwrap

# Declare all the rooms!

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
player = Player(room['outside'])

# Write a loop that:
#
while True:
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    print(textwrap.dedent(
        f"""\
        You are in room: {player.current_room.name}
        {player.current_room.description}!\
        """))
    # * Waits for user input and decides what to do.
    #

    print(textwrap.dedent('''
            What would you like to do?
            [n] Go North [s] Go South [e] Go East [w] Go West
            [take out <item>] or [return <item>]
            [drop <item>] Remove item from bag
            [b] look in bag
            [q] Quit
        '''))

    s = input("\n>").lower().split()
    # print('your input:{s}')

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    if len(s) == 1:
        # user has passed a direction
        if s == 'n':
            player.current_room = player.current_room.n_to
        elif s == 's':
            player.current_room = player.current_room.s_to
        elif s == 'e':
            player.current_room = player.current_room.e_to
        elif s == 'w':
            player.current_room = player.current_room.w_to
        elif s == 'q':
            print('see you later!')
            break
        else: 
            print("Not a valid direction!")

    elif len(s) == 2:
        # user has passed two word command to interact with items
        print("you're trying to interact with items, I can't do that yet")
    else:
        print("Sorry, I don't know that command")
        continue






# while True:
#     choice = input()

#     if choice.count(" ") > 1:
#         choice = input("\nMove not allowed.\n")
#     else:
#         action = choice

#     if action == "take out" or action == "return":
#         ## do item action stuff
#     elif action == "drop":
#         if isinstance(itemName, str):
#             if itemName in items:
#                 item = items[itemName]
#                 if item in player.inventory:
#                     player.drop_item(item)