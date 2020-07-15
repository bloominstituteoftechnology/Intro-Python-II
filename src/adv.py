from room import Room
from player import Player
import sys

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

player_1 = Player(name='Serina', current_room=room['outside'])

# Write a loop that:

# Prints the current room name
# Prints the current description (the textwrap module might be useful here).
print(f'Hello, stranger. You are currently in the {player_1.current_room.name}. {player_1.current_room.description}. \n')

# Waits for user input and decides what to do.
output = ('Choose a direction to travel in order to find the treasure.', 
f'But beware, there are many wrong paths to take:\n'
'[n] North  [s] South  [e] East  [w] West  [q] Quit\n')

direction = input('\n'.join(output))




# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

while not direction == 'q': 

    # You are here 
    print(f'You are in the {player_1.current_room.name}. \n{player_1.current_room.description}.')

    # Where do you want to go?
    direction = input('\n'.join(output))

    # If the player attempts to go north
    if direction == 'n':

        # This will test whether the resulting room is no longer a class object location (meaning it doesn't exist)
        if isinstance(player_1.current_room.n_to, list) is True:
            error_message = ("-------------------------------------------------------------",
            "Wrong way, cowboy. You can't go north here.",
            "Try a new direction!",
            "-------------------------------------------------------------\n")
            print('\n'.join(error_message))

        else:
            # Move player north
            player_1.current_room = player_1.current_room.n_to
            congratulatory_message = ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
            "You're getting closer to the treasure! Or maybe further away. Don't get lost now :)",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print('\n'.join(congratulatory_message))
    
    # If the player attempts to go south
    elif direction == 's':

        # This will test whether the resulting room is no longer a class object location (meaning it doesn't exist)
        if isinstance(player_1.current_room.s_to, list) is True:
            error_message = ("-------------------------------------------------------------",
                "Uh oh. There's no way to go south here so keep your pants on.",
            "Try a new direction!",
            "-------------------------------------------------------------\n")
            print('\n'.join(error_message))

        else:
            # Move player south
            player_1.current_room = player_1.current_room.s_to
            print('\n'.join(congratulatory_message))

    elif direction == 'e':

        # This will test whether the resulting room is no longer a class object location (meaning it doesn't exist)
        if isinstance(player_1.current_room.e_to, list) is True:
            error_message = ("-------------------------------------------------------------", 
            "Going east? Just because it's easy doesn't make it right.",
            "Try a new direction!",
            "-------------------------------------------------------------\n")
            print('\n'.join(error_message))
        else:
            # Move player east
            player_1.current_room = player_1.current_room.e_to
            print('\n'.join(congratulatory_message))

    elif direction == 'w':

        # This will test whether the resulting room is no longer a class object location (meaning it doesn't exist)
        if isinstance(player_1.current_room.w_to, list) is True:
            error_message = ("-------------------------------------------------------------",
            "Going west? You're the best. Just not at this game.",
            "Try a new direction!",
            "-------------------------------------------------------------\n")
            print('\n'.join(error_message))

        else:
            # Move player east
            player_1.current_room = player_1.current_room.w_to
            print('\n'.join(congratulatory_message))
    
    else:
        print("ValueError: Please enter an string input of length 1.")
        

        
# If the user enters "q", quit the game.