from room import Room
from player import Player 
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}



# Link rooms together

room['outside'].connections["n"] = room['foyer']
room['foyer'].connections["s"] = room['outside']
room['foyer'].connections["n"] = room['overlook']
room['foyer'].connections["e"] = room['narrow']
room['overlook'].connections["s"] = room['foyer']
room['narrow'].connections["w"] = room['foyer']
room['narrow'].connections["n"] = room['treasure']
room['treasure'].connections["s"] = room['narrow']

maps = Item("maps", "Map for the location of the gold")
key = Item("key", "Keys for the other locations")
light = Item("light", "Makes it easier to move in dark")
gem = Item("gem", "Unlocks the final door")
one_piece = Item("one Piece", "The most valuable treasure in the world")

#link items to rooms

room['outside'].items = maps
room['foyer'].items = key
room['overlook'].items = light
room['narrow'].items = gem
room['treasure'].items = one_piece



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Sunil", room['outside'])
# print(player1)
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

user_is_playing = True
possible_choices = ["n", "e", "s", "w"]



player_input = ''
while user_is_playing:
    #prints name of the room

    print("We are currenly at " + player.current_room.name)
    #prints description of the room

    print(player.current_room.description)
    print(player.current_room.items.name)
    #gets input from the player
    player_input = input("Chose between (n/s/e/w): ")

    if player_input == "q":
        user_is_playing: False
        break
        
       #evaluates player input
    if player_input in possible_choices:
        player.move(player_input)
    
        user_choice = input("Would you like to take or drop an item: ")
        if user_choice == "take":
            player.addItem()
        else:
            player.dropItem()
    else:
        print("you have entered invalid character")

    



















# while user_is_playing:
#     # prints out the current room
#     print(player1.current_room.name)
#     # prints outs the descripiton of the room 
#     for line in textwrap.wrap(player1.current_room.description, 40):
#         print(line)
#     # gets user input 
#     user_input = input("Which direction would you like to go? (n,s,w,e): ")
#     # print("This is the user_input:" + user_input)
#     #if input matches the route then move the player
#     if user_input in ["n", "e", "s", "w"]:
#         player1.move(user_input)
#     else:
#         print("Please choose between n,s,w,e")
#         user_is_playing = False
        
