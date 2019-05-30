from room import Room
from player import Player
from item import Item

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

# items descriptions

items = {
    'basket':  Item("basket",
                     "This contains fruits for energy."),

    'bike':    Item("bike", """The player can bike through the exit."""),

    'stool': Item("stool", """You can use the stool to put your valuables on."""),

    'chair':   Item("chair", """Relax in the room, sit in the chair."""),

    'jug': Item("jug", """I hope it has plenty of water for you!"""),
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
player = Player(room['outside'])

"""
this method takes two inputs
direction is the direction the user provides
current room is the place player current is
this method returns the new room if there was a room to move
means it the move was successful or returns the current room 
if the move wasn't successful
"""
def diff_directions(direction, current_room):
    move = direction + '_to'
    # to check if the direction is valid
    if hasattr(current_room, move):
        # if the direction is valid it returns the new current room
        return getattr(current_room, move)
    else:
        print("There is'nt a room in that direction!")
        return current_room

     
   
# Write a loop that:
while True:
    # * Prints the current room name
    print(player.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
    # * Waits for user input and decides what to do.
    # Input choices 
    s = input("\n> ").lower()[0]
    if s == "q":
        print("See you again!")
        break
    player.current_room = diff_directions(s, player.current_room)  

    # print(s)
    # if s == 'n':
    #     player.current_room = player.current_room.n_to
    # elif s == 's':
    #     player.current_room = player.current_room.s_to
    # elif s == 'e':
    #     player.current_room = player.current_room.e_to
    # elif s == 'w':
    #     player.current_room = player.current_room.w_to
    # else:
    #     print("Please provide a valid direction!")


    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    