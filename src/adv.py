from room import Room
from player import Player
from item import Item
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", [Item("cup"), Item("pencil"), Item("tea-cups"), Item("coins")]),

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

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
player_name = input("Hello, Please Enter Your Name >>> ")
player = Player(player_name, room['outside'])
print("Where Am I now? ")
print(player)

directions = "Enter your directions>>>\n" + "1) S or South "  + "2) N or North "  +"3) E or East " + "4) W or West"

def try_directions(direction, current_room):
    attribute = direction + '_to'
    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
        print("CAUTION:You cannot go that direction")
        return current_room

user_input = ''        
# Write a loop that:
while user_input != "q":
    # * Prints the current room name
    print(player.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
    # * Waits for user input and decides what to do.
    print(directions)    
    user_input = input(">").lower()
    user_input = user_input.split()
    # If the user enters a cardinal direction, attempt to move to the room there.
    if len(user_input) == 1:
        user_input = user_input[0][0]    # Print an error message if the movement isn't allowed.    
    # If the user enters "q", quit the game.
        if user_input == 'i':
            player.show_items()
        elif user_input == 'q':
            print("See you next time!")
            break
            player.current_room = try_directions(user_input, player.current_room)        
    elif len(user_input) == 2:
        method = user_input[0].lower()
        item = user_input[1].lower()
        print(user_input)
        if method == "add":
            player.add_items(item)

        elif method == "get":
            player.show_items()  

        elif method == "drop":
            player.delete_items(item)      
            


                
