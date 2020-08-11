from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

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

user = Player("none", room['outside'])

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
start_input = input("Would you like to play a game? (y,n) \n")
while True:
    if start_input == 'q':
        break
    elif start_input == 'y':
        user.name = input("Choose a name: \n")
        while True:
            getnext = input("Would you like to move (m) to another room \n or get a description (d) of your current room \n or quit(q)? \n")
            if getnext == 'm' or 'move':
                while True:
                    move = input("Which direction would you like to go? (n,s,e,w) or stop moving? (s) \n")
                    if move == 'n':
                        if user.current_room.name == 'outside':
                            user.current_room = room['outside'].n_to
                            print(user.current_room.name)
                        elif user.current_room.name == 'foyer':
                            user.current_room = room['foyer'].n_to
                            print(user.current_room.name)
                    elif move == 's':
                        user.current_room = room['outside'].n_to
                        print(user.current_room.name)
                    elif move == 'e':
                        user.current_room = room['outside'].n_to
                        print(user.current_room.name)
                    elif move == 'w':
                        user.current_room = room['outside'].n_to
                        print(user.current_room.name)
                        
            elif getnext == 'd': 
                print(f"{user.name} looks around and {user.current_room.description}")
            else:
                break
                
        
    

# Write a loop that:
#
# * Prints the current room name
        print(user)
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
    
# If the user enters a cardinal direction, attempt to move to the room there.

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
