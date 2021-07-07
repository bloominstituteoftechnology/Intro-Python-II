from room import *
from player import *
from item import *
import sys
import os
import time
from colorama import init
init()
from colorama import Fore, Back, Style
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

# Items
sword = Item("sword", "pointy sword")
lantern = Item("lantern", "light source")
rock = Item("rock", "for weightlifting")
chest = Item("chest", "pot of gold")
rope = Item("rope", "this might be useful")


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].add_item(sword)
room['treasure'].add_item(lantern)
room['foyer'].add_item(rope)

# Code to get the message to print char by char
def typewriter( message):
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

# Code to print all adjacent rooms
def cheat_map (current_room):
    print("North: ", current_room.get_n_to())
    print("East:  ", current_room.get_e_to())
    print("South: ", current_room.get_s_to())
    print("West:  ", current_room.get_w_to())

def prompt_action():
    return input("\nEnter in a selection\n[N] move North \n[E] move East \n[S] move South\
         \n[W] move West\n[H] for Help \n[Q] to Quit\n ")

def print_move(current_room):
    print("\nCurrent Room: " + current_room.name)
    print(f"Room Description: {current_room.description}")
#items = [Item(item[0], item[1]) for item in items]
# Main
#


def main():
    # Make a new player object that is currently in the 'outside' room.
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    print('back to normal now')

    # Write a loop that:
    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    print()
    typewriter("******** WELCOME TO THE *********\n")
    typewriter("**** ULTIMATE ADVENTURE GAME ****")
    player = Player("Mario", room['outside'])
    current_room = player.current_room
    print("\nCurrent Room: " + current_room.name)
    print(f"Room Description: {current_room.description}")
    print("\n\n" + player.get_current_room())
    
    action_input = prompt_action()

    while action_input.lower() != 'q':
        if action_input.lower() == 'n':
            try:
                print(current_room.n_to.name)
                player.current_room = current_room.n_to
                current_room = player.current_room
                print_move(current_room)
                print("**************************")
                typewriter("       Going North       ")
                print("\n**************************")
                
            except:
                print("Nope. Can't go that way.")
        elif action_input.lower() == 'e':
            try:
                print(current_room.e_to.name)
                player.current_room = current_room.e_to
                current_room = player.current_room
                print_move(current_room)
                print("**************************")
                typewriter("        Going East        ")
                print("\n**************************")
            except:
                print("Uh-oh edge of the Earth. Choose another direction.")
        elif action_input.lower() == 's':
            try:
                print(current_room.s_to.name)
                player.current_room = current_room.s_to
                current_room = player.current_room
                print_move(current_room)
                print("**************************")
                typewriter("       Going South       ")
                print("\n**************************")
            except:
                print("An immovable wall blocks you pass.")
        elif action_input.lower() == 'w':
            try:
                print(current_room.w_to.name)
                player.current_room = current_room.w_to
                current_room = player.current_room
                print_move(current_room)
                print("**************************")
                typewriter("        Going West        ")
                print("\n**************************")
            except:
                print("Nah brah.")        
        elif action_input.lower() == 'c':
            cheat_map(current_room)
        elif action_input.lower() == 'l':
            print("Current Room: " + current_room.name)
        elif action_input.lower() == 'i':
            current_room.get_inventory()
        elif " " in action_input:
            words = action_input.split()
            if len(words) > 2:
                print("Action is not valid")
            elif words[0].lower() == "take" or words[0].lower == "get":
                print("Taking")
            elif words[0].lower() == "drop":
                print("Dropping")
            else:
                print("Invalid Action")
        else:
            print("Action is not valid.")

        
        action_input = input("\nEnter in a cardinal direction\n[N] for North, [E] for East, [S] for South, [W] for West\n ")
    print("Thanks for playing. Have a nice life...")

main()



"""
# Items
items = [
    ["sword", "pointy sword"],
    ["lantern", "light source"],
    ["rock", "for weightlifting"],
    ["chest", "pot of gold"],
    ["rope", "this might be useful"]
]
items =[Item(item[0], item[1]) for thing in items]
"""