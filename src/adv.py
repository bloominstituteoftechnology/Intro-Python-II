from room import Room
from player import Player
import os

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

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

player = Player("Nick", room['outside'])


print(style.BLUE + "Welcome to the Adventure Game!")
print(style.BLUE +"Please choose a direction to move.")

game_running = True

while game_running:

    print(style.YELLOW + "Current room:", player.current_room.name)
    print(style.YELLOW + "Description:", player.current_room.description)

    user = input(style.CYAN + "[n] north [s] south [e] east [w] west [q] quit\n")
    wrong_alert = (style.RED + "Wrong direction,follow the hint in description!!!")
    if user == "n":
        if player.current_room.n_to == None:
            print(wrong_alert)
        else:
            player.current_room = player.current_room.n_to
    elif user == "s":
        if player.current_room.s_to == None:
            print(wrong_alert)
        else:
            player.current_room = player.current_room.s_to
    elif user == "e":
        if player.current_room.e_to == None:
            print(wrong_alert)
        else:
            player.current_room = player.current_room.e_to
    elif user == "w":
        if player.current_room.w_to == None:
            print(wrong_alert)
        else:
            player.current_room = player.current_room.w_to
    # If the user enters "q", quit the game
    elif user == "q":
        print("Game Over!")
        quit()
