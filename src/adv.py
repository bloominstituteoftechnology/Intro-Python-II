#!/usr/bin/env python3

# import Item
from item import Item
from room import Room
from player import Player
from colors import Colors
import textwrap


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



# Room Items
room_items = {
    'outside' : [Item("Flashlight", "This will help light your way."), Item("Batteries", "They power things.")],
    'foyer' : [Item("Walkman", "Listen to some jams"), Item("Pencil", "No. 2")],
    'overlook' : [Item("Sword", "Are you worthy?"), Item("Binoculars", "See things at a great distance")],
    'narrow' : [Item("Twinkie", "Get some energy!"), Item("Vile", "Gives you a boost"), Item("Cloak", "Makes you invisible")],
    'treasure' : [Item("Watch", "It appears to be broken"), Item("flask", "To take the edge off in case things get wild.")]
}

room['outside'].items = room_items['outside']
room['foyer'].items = room_items['foyer']
room['overlook'].items = room_items['overlook']
room['narrow'].items = room_items['narrow']
room['treasure'].items = room_items['treasure']


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

# Helper Strings
unrecognized_str = "Command not recognized. Try again and remember, you can always type'h' for help."

# PLAYER - Make a new player object that is currently in the 'outside' room.
p = Player(input("What is the name of your character: "), room['outside'])



# If player needs help:
def help_hud():
    help_str = """
[l] Locate Me / [la] Look Around / [m] Move Options / [ci] Check Inventory: """
    
    help_cmd = input(textwrap.dedent(help_str))
    
    if help_cmd ==  "l":
        print(p.current_room)
        print()
    elif help_cmd == "la":
        look_around_action()
    elif help_cmd == "m":
        print(p.current_room.get_exits())
    elif help_cmd == "ci":
        print(p.get_items())
    
def look_around_action():
    unrecognized_command_str = "Command/action is not recognized. Try again."
    if p.current_room.get_room_items:
        print(f"There are {len(p.current_room.get_room_items())} items:\n")
        print(f"Visible items: {p.current_room.get_room_items()}\n")
        print("Use 'pickup' [item name] to grab the item or 'drop' [item name] to put back down...")
        cmd = input("What would you like to do? ~~> ").lower()
        cmd = cmd.split(" ")
        if len(cmd) == 2:
            perform_action = cmd[0]
            item = cmd[1]
                
            if perform_action == 'pickup':
                for i in p.current_room.items:
                    if i.name == item:
                        p.pick_up_item(i)
                        p.current_room.items.remove(i)
            else:
                print(unrecognized_command_str)
                            
            if perform_action == 'drop':
                for i in p.items:
                    if i.name == item:
                        p.drop_item(item)
            else:
                print(unrecognized_command_str)
        else:
            print(unrecognized_command_str)
        

def travel(command, directions):
    if command in directions:
        p.travel(command)
    elif command == "q":
        print("Goodbye")
        exit(1)
    else:
        print(unrecognized_str)



# HUD for player
def hud(player):
    print("\n•-•-•-•-•-•-••-•-•-•-•-•-••-•-•-•-•-•-••-•-•-•-•-•-••-•-•-•-•-•-•-•-••-•-•-•-•-•-•")
    print(textwrap.dedent(Colors.RED + "\nHUD DISPLAY" + Colors.END))
    print("Player: " + Colors.BOLD + Colors.PURPLE + f"{player.name}" + Colors.END + Colors.BOLD + "::: Current Room: " + Colors.BOLD + Colors.PURPLE + f"{player.current_room.name}" + Colors.END + Colors.BOLD + "::: Inventory Count: " + Colors.PURPLE + f"{player.items}\n" + Colors.BLUE)
    print(textwrap.dedent(Colors.DARKCYAN + player.current_room.description + Colors.END))


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


directions = ["n", "w", "s", "e"]


# Write a loop that:
flag = True

while flag:    
    room = p.current_room
    hud(p)
    # print(room.name)
    print(textwrap.dedent("\n•-•-•-•-•-•-••-•-•-•-•-•-••-•-•-•-•-•-••-•-•-•-•-•-••-•-•-•-•-•-•-•-••-•-•-•-•-•-•"))
    m = input("~~> ").lower()

    if m == "h":
        help_hud()

    elif m in directions:
        p.travel(m)
        
    elif m ==  "l":
        print(p.current_room)
        
    elif m == "la":
        print(p.current_room.get_room_items())
        look_around_action()
        
    elif m == "m":
        print(p.current_room.get_exits())
        
    elif m == "ci":
        print(p.get_items())

    elif m == "q":
        print("Goodbye")
        exit(1)
        
    else:
        print(unrecognized_str)

        
    
    
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.