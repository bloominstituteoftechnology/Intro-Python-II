from room import Room
from player import Player
from item import Item
import random

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
# Declare Items
sword = Item("sword", "The sword glows and radiates heat from the blade")
shield = Item("shield", "The shield was crafted in a magic forge")
armor = Item("armor", "Inpenetrable armor crafted by elves")

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# choose a room to place items
room['overlook'].items = [shield]
room['foyer'].items = [sword]
room['narrow'].items = [armor]
# Main
#
player_name = input("Welcome traveler. What is your name?: ")
# Make a new player object that is currently in the 'outside' room.
new_player = Player(player_name, room['outside'])
# Write a loop that:
#
# * Prints the current room name
print(f"Current location: { new_player.current_room.name }")
# * Prints the current description (the textwrap module might be useful here).
print(new_player.current_room.description)
# * Waits for user input and decides what to do.
#
# def update_location():
#     print(f"Current location: { new_player.current_room.name }")
#     print(new_player.current_room.description)
#     if len(new_player.current_room.items) == 0:
#         print("No Items in this room.")
#     else:
#         print(f"Available Items: { new_player.current_room.items }")
def getitem():
    item_choice = input("What do you want to do? Ex: get sword: ").split()
    #check if item choice 2 is equal to one of the item.names in the players current room's items.
    for i in new_player.current_room.items:
        if item_choice[1] == i.name and item_choice[0] == "get":
            new_player.items.append(i)
            new_player.current_room.items.remove(i)
        else:
            print("Option not available.")

def update_location():
    print(new_player.current_room)
    if len(new_player.current_room.items) > 0:
        getitem()
        print(new_player)

def invalid_direction():
    print("Cannot move in that direction.")
    
user_choice = ''
while user_choice != 'q':
    user_choice = input("Choose a direction to move.  Enter n, s, e, or w: ")
    if user_choice == 'n':
        if hasattr(new_player.current_room, 'n_to'):
            new_player.current_room = new_player.current_room.n_to
            update_location()
        else:
            invalid_direction()
    elif user_choice == 's':
        if hasattr(new_player.current_room, 's_to'):
            new_player.current_room = new_player.current_room.s_to
            update_location()
        else:
            invalid_direction()
    elif user_choice == 'e':
        if hasattr(new_player.current_room, 'e_to'):
            new_player.current_room = new_player.current_room.e_to
            update_location()
        else:
            invalid_direction()
    elif user_choice == 'w':
        if hasattr(new_player.current_room, 'w_to'):
            new_player.current_room = new_player.current_room.w_to
            update_location()
        else:
            invalid_direction()
    elif user_choice == 'q':
        print("Thanks for playing. Exiting game.")
    else:
        print("Not a valid direction.")
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
