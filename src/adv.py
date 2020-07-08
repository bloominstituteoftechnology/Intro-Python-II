import sys
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

is_playing = False

# Welcome message: 
print("Welcome to Adventure Quest!")
# Ask if user wants to play game:
player_start = input("Do you want to go an adventure to find some hidden treasure (Y = yes, N = no)?: ")

if player_start.upper() == 'N':
    print("That's too bad. Well, if you change your mind, we'll be around. Tata for now!")
    sys.exit()
elif player_start.upper() == 'Y':
    is_playing = True
    print("Yay! That's great news. We're going to be rich. Before we get started, if at anytime you need to go home, enter 'Q' to quit the game. Now let's get started.")
#TODO: invalid response (not y or n)

# Collect player's name and instantiate player...by default, player starts in 'outside' room
player_name = input("First things first. Tell me, what is your name? ")
current_player = Player(player_name, room['outside'])

print("It's nice to meet you ", current_player.name.capitalize(), "!", current_player.current_room)

# Main game loop: 
while is_playing: 
    # print(current_player.current_room)
    action = input("Where would you like to go next? (N = north, E = east, S = south, W = west): ")

    if action.upper() == 'Q': 
        is_playing = False
        print("Goodbye! Hope to see you again some time soon.")
    
    elif action.upper() == 'N':
        if (hasattr(current_player.current_room, 'n_to')):
            current_player.current_room = current_player.current_room.n_to
            print(current_player.current_room)
        else: 
            print("Nothing's there. Let's go somewhere else.")

    elif action.upper() == 'E':
        if (hasattr(current_player.current_room, 'e_to')):
            current_player.current_room = current_player.current_room.e_to
            print(current_player.current_room)
        else: 
            print("You must not go that way! Try again.")

    elif action.upper() == 'S':
        if (hasattr(current_player.current_room, 's_to')):
            current_player.current_room = current_player.current_room.s_to
            print(current_player.current_room)
        else: 
            print("Doesn't look like anything's that way.")        

    elif action.upper() == 'W':
        if (hasattr(current_player.current_room, 'w_to')):
            print(current_player.current_room.w_to)
        else: 
            print("Looks like a wall with no doors. Head in a different direction.")

    else: 
        print("That's not an option. Please enter a valid direction. Remember, N = north, E = east, S = south, W = west.")