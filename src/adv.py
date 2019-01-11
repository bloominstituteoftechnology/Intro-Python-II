from room import Room
from player import Player
from item import Item

# Declare all the rooms

items = {
    'sword': Item("Sword", "sword description"),
    'scissors': Item("Scissors", "scissors description"),
    'rock': Item("Rock", "Rock description"),
    'drill': Item("Drill", "drill description"),
    'taser': Item("Taser", "taser description"),
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['sword']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['rock']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['drill']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items['scissors']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items['taser']]),
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

name = input("enter player's name\n>")
player = Player(name, room["outside"])
print(player)

def try_direction(direction, room):
    attr = direction + "_to"
    if hasattr(room, attr):
        return getattr(room, attr)
    else:
        print("you cant go that way")
        return room 

while True:
    print(player.room.name)
    print(player.room.description)

    user_input = input("\n> ").lower().split()

    if len(user_input) == 1:
        user_input = user_input[0][0]
        player.room = try_direction(user_input, player.room)

    elif len(user_input) == 2:
        word = user_input[0]
        item = user_input[1]

        if word == "grab":
            if item == item.name:
                player.room.items.remove(item)
                player.inventory.append(item)
                print(f"{item.name} was added to the inventory")
        
        if word == "drop":
            if item == item.name:
                player.inventory.remove(item)
                player.room.items.append(item)
                print(f"{item.name} wass removed from the inventory")
    elif user_input == "q":
        break
    
    else:
        print("I don't understand that")
        
