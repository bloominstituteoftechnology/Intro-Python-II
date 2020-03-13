
from room import Room
from player import Player
from item import Item


# Declare all the rooms
import os 

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Chair", "throw it"), Item("table", "throw it")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Gems", "bag of gems")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Coat", "keep the coat")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Water", "Drink water for power")]),
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


# item = {
#     "chair": Item("Chair", "throw it"),
#     "gems": Item("Gems", "bag of gems"),
#     "coat": Item("Coat", "keep the coat"),
#     "water": Item("Water", "Drink water for power")
# }
#
# Main
#
# Make a new player object that is currently in the 'outside' room.

player = Player(input('\nwhat is your name? '),room['outside'])
os.system("clear")
print(player.current_room)


while True:
    cmd = input("Cardinal direction ").lower()
    if cmd in ["n", "s", "e", "w"]:
        player.travel(cmd)
    elif cmd == 'i':
        player.item_inventory()
    elif cmd == 'l':
        player.current_room.room_inventory()
    elif cmd == 'p':
        item_to_add=input('Please enter item to add to your inventory ')
        player.add_item(item_to_add)
    elif cmd == 'd':
        player.item_inventory()
        remove_item=input('please enter item to remove ')
        player.drop_item(remove_item)
    elif cmd == 'q':
        print('goodbye come again')
        exit()  
    else:
        print('Command not valid!')



# print(f"Welcome, {player.name}.\n\nYou are {player.current_room}")
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