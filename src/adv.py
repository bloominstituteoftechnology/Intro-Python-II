# Name of game is called Explore

from room import Room
from player import Player
from item import Item
import argparse
import time
import sys

# Argument Parser
explore_parser = argparse.ArgumentParser()
explore_parser.add_argument("-n", "--north", help="Moves player north")
explore_parser.add_argument("-w", "--west", help="Moves player west")
explore_parser.add_argument("-s", "--south", help="Moves player south")
explore_parser.add_argument("-e", "--east", help="Moves player east")
explore_parser.add_argument("-bp", "--backpack", help="Stores items for player")
explore_parser.add_argument("-q", "--quit", help="Quits the game")

args = explore_parser.parse_args()

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("at the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("at the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("at the Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("in the Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['outside'].s_to = None
room['outside'].e_to = None
room['outside'].w_to = None

room['foyer'].n_to = room['overlook']
room['foyer'].s_to = room['outside']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = None

room['overlook'].n_to = None
room['overlook'].s_to = room['foyer']
room['overlook'].e_to = None
room['overlook'].w_to = None

room['narrow'].n_to = room['treasure']
room['narrow'].s_to = None
room['narrow'].e_to = None
room['narrow'].w_to = room['foyer']

room['treasure'].n_to = None
room['treasure'].s_to = room['narrow']
room['treasure'].e_to = None
room['treasure'].w_to = None

# Declare all items
item = {
    'note': Item("a Note", "A note from past explorers. It reads, 'Found the treasure first! You suck!'"),

    'knife': Item("a Knife", "An instrument composed of a blade fixed into a handle."),

    'gold': Item("a bag of Gold", "A yellow precious metal.")
}

# Link item to room
room['outside'].item = None

room['foyer'].item = [item['gold']]

room['overlook'].item = [item['knife']]

room['narrow'].item = None

room['treasure'].item = [item['note']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print("Welcome to Explore!")
print("What is your name explorer?")
player = input("> ")
new_player = Player(player, room["outside"])

user_input = ""
while user_input != "q":
    print("{}, you are {}, {}".format(new_player.name, new_player.room.name, new_player.room.description))
    # if new_player.room.item != None:
    #     print(f"This room has {new_player.room.item.name}: {new_player.room.item.description}")
    #     print("""What would you like to do? Enter 'take'/'drop' [item] to take/drop the item.""")
    #     decision = input("> ")
    #     if decision == 'y':

    print("What would you like to do? Enter n, s, e, or w to move, l to look, ")
    print("i for inventory, drop [item] to drop item or q to quit.")
    user_input = input("> ")
    # North
    if user_input == 'n':
        if new_player.room.n_to != None:
            print("Moving. Heading North.")
            time.sleep(2)
            new_player.room = new_player.room.n_to
        else:
            print("You cannot go that way.")
    # South
    elif user_input == 's':
        if new_player.room.s_to != None:
            print("Moving. Heading South.")
            time.sleep(2)
            new_player.room = new_player.room.s_to
        else:
            print("You cannot go that way.")
    # East
    elif user_input == 'e':
        if new_player.room.e_to != None:
            print("Moving. Heading East.")
            time.sleep(2)
            new_player.room = new_player.room.e_to
        else:
            print("You cannot go that way.")
    # West
    elif user_input == 'w':
        if new_player.room.w_to != None:
            print("Moving. Heading West")
            time.sleep(2)
            new_player.room = new_player.room.w_to
        else:
            print("You cannot go that way.")
    # Quit
    elif user_input == 'q':
        print("Well...")
        time.sleep(2)
        print("You have decided to end your quest.")
        time.sleep(1)
        print("Farewell!")
        quit()
    # Look
    elif user_input == 'l':
        print("Looking around the room...")
        time.sleep(2)
        sys_length = len(sys.argv)
        if new_player.room.item != None:
            print(f"This room has {new_player.room.item[0].name}: {new_player.room.item[0].description}")
            print("Would you like to take it? Enter 'take [item]' to add to inventory or 'n' to leave it.")
            decision = input("> ").lower()
            arg_length = decision.split(" ")
            if len(arg_length) == 1:
                if arg_length[0] == 'n':
                    print("You leave the item in the room.")
            elif len(arg_length) == 2:
                if arg_length[0] == "take" and arg_length[1] == new_player.room.item[0].name:
                    print(f"You pick up {new_player.room.item[0].name}")
                    time.sleep(2)
                    new_player.item = new_player.room.item
                    print(f"You now have {new_player.item[0].name} in your inventory.")
                    time.sleep(2)
                    new_player.room.item = None
            # if decision == f"take {new_player.room.item[0].name}":
            #     print(f"You pick up {new_player.room.item[0].name}")
            #     time.sleep(2)
            #     new_player.item = new_player.room.item
            #     new_player.room.item = None
            # elif decision == "n":
            #     print("You leave the item in the room.")
            else:
                print("Please enter a valid response.")
        else:
            print("There is nothing in this room.")
            time.sleep(2)
    else:
        print("Please enter a valid response.")

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
