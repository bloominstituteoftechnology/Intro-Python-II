#!/usr/bin/env python3

from room import Room
from player import Player
import textwrap
import Item

name = input("What is the name of your character: ")

print(f"Let's begin your adventure, {name}!")

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

def print_move_options(current_room):
    if current_room == "Outside Cave Entrance":
        return "Move: [n] North [q] Quit: "
    elif current_room == "Foyer":
        return "Move: [n] North [s] South [e] East [q] Quit: "
    elif current_room == "Grand Overlook":
        return "Move: [s] South [q] Quit: "
    elif current_room == "Narrow Passage":
        return "Move: [n] North [w] West [q] Quit: "
    else:
        return "Move: [s] South [q] Quit: "


def help_hud():
    help_str = """
[l] Locate Me / [la] Look Around / [m] Move Options / [ci] Check Inventory: """
    
    usr_input = input(textwrap.dedent(help_str))
    
    if usr_input ==  "l":
        print(p.current_room)
    elif usr_input == "la":
        print("")
    
# def move_options():

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
p = Player(name, room['outside'])

# Write a loop that:
flag = True

while flag:    
    room = p.current_room
    print(room.name)
    
    m = input("What would you like to do?       hint: (Press 'h' for help): ")

    if m == "h":
        help_hud()
    
    if m == "n":
        if  room.n_to: 
            p.move_to_room(room.n_to)
            print(p.current_room.name)
        else:
            print("Can't move there. Try again.")
            
    elif m == "s":
        if  p.current_room.s_to:
            print(p.current_room.name)
            p.current_room = p.current_room.s_to
            print(p.current_room.name)
        else:
            print("Can't move there. Try again.")
            
    elif m == "w":
        if  p.current_room.w_to:
            print(p.current_room.name)
            p.current_room = p.current_room.w_to
            print(p.current_room.name)
        else:
            print("Can't move there. Try again.")
            
    elif m == "e":
        if  p.current_room.e_to:
            print(p.current_room.name)
            p.current_room = p.current_room.e_to
            print(p.current_room.name)
        else:
            print("Can't move there. Try again.")
        

        
    
    
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.