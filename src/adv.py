from room import Room
from player import Player 
from item import Item
import sys



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


# Main

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

player = Player("player1", room['outside'])

room['treasure'].item_list.append(Item("sword", "Level 1 sword"))
room['overlook'].item_list.append(Item("map", "Level 1 map"))

while True:
    print(f"Current room: {player.current_room.name}")
    print(f"Description: {player.current_room.description}")

    print("Items in the room: ")
    for item in player.current_room.item_list: 
        print(f"{item.name} - {item.description}")

    print("Player inventory: ")
    for item in player.inventory:
        print(f"{item.name} - {item.description}")

    move = input("Enter a move: ")

    if len(move.split()) == 1:
        if move != "s" and move != "n" and move != "e" and move != "w" and move != "q":
            print("Invalid move!!!")
            print("Enter 's' to move south")
            print("Enter 'n' to move north")
            print("Enter 'w' to move west")
            print("Enter 'e' to move east")
            print("Enter 'q' to quit the game")

        elif move == "q":
            print("The player quit the game!")
            sys.exit()
            
        elif move == "s":
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
            else:
                print("Unable to move in that direction!")

        elif move == "n":
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
            else:
                print("Unable to move in that direction!")

        elif move == "w":
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
            else:
                print("Unable to move in that direction!")

        elif move == "e":
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
            else:
                print("Unable to move in that direction!")

    elif len(move.split()) == 2: 
        if move.split()[0] == "get":
            if len(player.current_room.item_list) > 0:
                for item in player.current_room.item_list:
                    if item.name == move.split()[1]:
                        player.current_room.item_list.remove(item)
                        player.inventory.append(item)
                    else:
                        print(f"There is no {move.split()[1]} in this room!")
            else:
                print("There are no items in this room!")

        elif move.split()[0] == "take":
            if len(player.current_room.item_list) > 0:
                for item in player.current_room.item_list:
                    if item.name == move.split()[1]:
                        player.current_room.item_list.remove(item)
                        player.inventory.append(item)
                    else:
                        print(f"There is no {move.split()[1]} in this room!")
            else:
                print("There are no items in this room!")

        elif move.split()[0] == "drop":
            if len(player.inventory) > 0:
                for item in player.inventory:
                    if item.name == move.split()[1]:
                        player.inventory.remove(item)
                        player.current_room.item_list.append(item)
                    else:
                        print(f"You do not have {move.split()[1]} in your inventory!")

            else: 
                print("You have no items in your inventory!")

        else:
            print("Invalid move!!!")

    else:
        print("Invalid move!!!")







