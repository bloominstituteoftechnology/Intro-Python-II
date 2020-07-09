# python adv.py

from room import Room
from player import Player

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

'kitchen': Room("Kitchen", """You've found the great dining hall! 
Grab a snack to keep up your energy."""),

'lake': Room("Great Lake", """You've found the great lake! Be cautious;
these waters are very dangerous for swimmers."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].s_to = room['lake']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['kitchen']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['kitchen'].e_to = room['foyer']
room['lake'].n_to = room['outside']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("Hey! What's your name...?\n>>>")
new_player = Player(name, room["outside"])
print(f"              WELCOME TO THE PARTY, {new_player.name.upper()}!")
print("------------------------------------------------------")
print("------------------------------------------------------")

# Write a loop that:
while True:
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    current_room = new_player.current_room
    print(f"Current room: {current_room.name}")
    print(f"Description: {current_room.description}")
    
    # * Waits for user input and decides what to do.
    print("---------------------------")
    print("       Which direction would you like to go?")
    direction = input("[n] North  [s] South   [e] East   [w] West  [q] Quit\n>>>")

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if direction == "n":
        print("You selected North.".upper())
        if current_room.n_to is not None:
            new_player.current_room = current_room.n_to
            print(f"You are now entering the {new_player.current_room.name}!!")
            print("---------------------------")
        else:
            print(":( Im sorry, you've reached a dead end...")  
            print("---------------------------")
    elif direction == "s":
        print("You selected South.".upper())
        if current_room.s_to is not None:
            new_player.current_room = current_room.s_to
            print(f"You are now entering the {new_player.current_room.name}!!")
            print("---------------------------")
        else:
            print(":( Im sorry, you've reached a dead end...") 
            print("---------------------------")
    elif direction == "e":
        print("You selected East.".upper())
        if current_room.e_to is not None:
            new_player.current_room = current_room.e_to
            print(f"You are now entering the {new_player.current_room.name}!!")
            print("---------------------------")
        else:
            print(":( Im sorry, you've reached a dead end...") 
            print("---------------------------")
    elif direction == "w":
        print("You seleected West.".upper())
        if current_room.w_to is not None:
            new_player.current_room = current_room.w_to
            print(f"You are now entering the {new_player.current_room.name}!!")
            print("---------------------------")
        else:
            print(":( Im sorry, you've reached a dead end...".upper()) 
            print("---------------------------")
    elif direction == "q":
        # If the user enters "q", quit the game.
        print("Ciao Bella! o.0")
        break
    else:
        print("Not a valid input")
        
    
    