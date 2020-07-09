from room import Room
from player import Player
from item import Item, items, description

# Declare all the rooms   ;)

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

#
# Main
#
print("Welcome Adventurer!")
# Make a new player object that is currently in the 'outside' room.
player_one = Player("Frodo", room["outside"], ["cape", "ring"])
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


while player_one.awake:
    print("If you'd like to take a nap at anytime think of the letter 'q'")
    print(f"{player_one.current_room.name}\n{player_one.current_room.description}")
    player_one_input = input("Explore the area to find the treasure.") 

    if player_one_input == "q":
        player_one.awake = False 
    
    #Outside--->Foyer
    elif player_one_input == "n":
        player_one.current_room = player_one.current_room.n_to
        print(player_one.current_room)
    
    #Foyer--->Overlook
    elif player_one_input == "n":
        player_one.current_room = player_one.current_room.n_to
        print(player_one.current_room)
    #Foyer--->Narrow
    elif player_one_input == "e":
        player_one.current_room = player_one.current_room.e_to
        print(player_one.current_room)
    #Foyer--->Outside
    elif player_one_input == "s":
        player_one.current_room = player_one.current_room.s_to
        print(player_one.current_room)

    #Overlook--->Foyer
    elif player_one_input == "s":
        player_one.current_room = player_one.current_room.s_to
        print(player_one.current_room)

    #Narrow--->Foyer
    elif player_one_input == "w":
        player_one.current_room = player_one.current_room.w_to
        print(player_one.current_room)
    #Narrow--->Treasure
    elif player_one_input == "n":
        player_one.current_room = player_one.current_room.n_to
        print(player_one.current_room)
    
    #Treasure--->Narrow
    elif player_one_input == "s":
        player_one.current_room = player_one.current_room.s_to
        print(player_one.current_room)

    #check if None = blocked    
    else:
        print("The path seems to be blocked")
