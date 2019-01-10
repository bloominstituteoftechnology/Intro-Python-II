from room import Room
from player import Player
from item import Item
import sys
import os
import cmd
import textwrap
import time
import random

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook",
     """A steep cliff appears before you, falling
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

starting_knight = [Item("Steel Sword", "Something To Slice With."), Item("Lions Mane", "Increases Health Slightly")]
starting_magi = [Item("Magic Spell Book", "Provides Knowledge Of Ancient Spells"), Item("Lions Mane", "Increases Health Slightly")]
starting_assassin = [Item("Steel Dagger", "Something To Stab With."), Item("Lions Mane", "Increases Health Slightly")]



#
# Main
#
def main():
    print(os.environ)
    os.system('clear')
    print("Welcome To Troy's Text Adventure Game\n")
    print("1.) Start")
    print("2.) Load")
    print("3.) Exit")
    option = input("-> ")
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        sys.exit()
    else:
        print("Requires 1, 2, or 3 inputs")
        main()


def class_define(player_name):
    print("Which Class Would You Like To Be {}: ".format(player_name))
    print("1.) Knight")
    print("2.) Magi")
    print("3.) Assassin")

    player_class = input('Class: \n').upper()
    if player_class == "1" or player_class == "KNIGHT":
        global starting_knight
        default_inventory = starting_knight
        class_name = "Knight"
    elif player_class == "2" or player_class == "MAGI":
        global starting_magi
        default_inventory = starting_magi
        class_name = "Magi"
    elif player_class == "3" or player_class == "ASSASSIN":
        global starting_assassin
        default_inventory = starting_assassin
        class_name = "Assassin"
    else:
        print("Requires 1, 2, or 3 inputs or specify as `knight`, `magi`, or `assassin`\n")
        class_define(player_name)
    
    default_location = room['outside']
    
    global PlayerIG
    PlayerIG = Player(player_name, default_location, default_inventory)
    start1(class_name)

def start():
    os.system('clear')
    print("Hello, what is your name?")
    global room
    # print(room['outside'])
    options = input('-->')

    class_define(options)

def start1(x):
    os.system('clear')
    print("Hello {} {}, how are you?".format(x ,PlayerIG.name))


main()
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
