from room import Room
from player import Player
from item import Item

# Items

item = [
    Item('Badass Sword of Unity'),
    Item('Killer Mace'),
    Item('Strong Shield'),
    Item('Potion of Healthyness')
]

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     None,
                     None,
                     None,
                     None,
                     [item[0],
                      item[1]
                      ]),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     None,
                     None,
                     None,
                     None,
                    [item[2],
                     item[3]
                     ]),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     None,
                     None,
                     None,
                     None,
                     [item[3],
                      item[0]
                      ]),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     None,
                     None,
                     None,
                     None,
                     [item[1],
                      item[3]
                      ]),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     None,
                     None,
                     None,
                     None,
                     [item[1],
                      item[2]
                      ]),
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

player = Player("Steve", room ['outside'])
def show_welcome_message():
    welcome_message = "Welcome to the game!"
    print(welcome_message)
def get_user_choice():
    choice = input("[n] north [s] south [e] east [w] west [q] quit\n")
    return choice_options[str(choice)]
choice_options = {
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
    "q": "quit"
}
show_welcome_message()
while True:
    current_room = player.current_room
    print(f"You are currently in {current_room.name}")
    print(f"{current_room.description}")
    move = input("Select N, S, E, or W >>> ")
    if move == "n":
        if current_room.n_to is not None:
            player.current_room = current_room.n_to
            print(f"You picked up {current_room.items[0]}")
            print(f"You picked up {current_room.items[1]}")
        else:
            print("You hit a dead end!  Try again.")
    elif move == "s":
        if current_room.s_to is not None:
            player.current_room = current_room.s_to
            print(f"You picked up {current_room.items[0]}")
            print(f"You picked up {current_room.items[1]}")
        else:
            print("You hit a dead end!  Try again.")
    elif move == "e":
        if current_room.e_to is not None:
            player.current_room = current_room.e_to
        else:
            print("You hit a dead end!  Try again.")
    elif move == "w":
        if current_room.w_to is not None:
            player.current_room = current_room.w_to
        else:
            print("You hit a dead end!  Try again.")
    elif move == "q":
        print("Game has quit")
        exit()