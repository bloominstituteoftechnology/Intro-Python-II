from player import Player
from room import Room
import time
import textwrap

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

def attempt_move(direction):
    """ attempts to move the player in the given direction """

    if direction == "north":
        if player.current_room.n_to is None:
            print("There is no room to the north")
            time.sleep(1)  # pause for a moment to let player see the message
        else:
            player.current_room = player.current_room.n_to

    elif direction == "south":
        if player.current_room.s_to is None:
            print("There is no room to the south")
        else:
            player.current_room = player.current_room.s_to

    elif direction == "east":
        if player.current_room.e_to is None:
            print("There is no room to the east")
        else:
            player.current_room = player.current_room.e_to

    elif direction == "west":
        if player.current_room.w_to is None:
            print("There is no room to the west")
        else:
            player.current_room = player.current_room.w_to


def print_wrapped(message, width=50):
    """ Prints a message using the textwrap module """
    wrapper = textwrap.TextWrapper(width) 
    message = wrapper.wrap(message) 
    for line in message: 
        print(line)


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

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

print("--- Welcome to Lambda adventure! ---")
print("To move, enter a direction")
print('To quit, enter "q" or "quit"')

game_over = False
while not game_over:
    # Print the current room name and description
    print("\n----------------------------------")
    print_wrapped(player.current_room.name)
    print_wrapped(player.current_room.description)

    # Ask for player input
    #print("\nWhich direction would you like to go?")
    command = input("\nWhich direction would you like to go? ")

    # Convert to lower case to understand more input options
    command = command.lower()

    # Handle player input
    # quit command
    if command in ["q", "quit"]:
        game_over = True
    
    # 4 movement commands
    elif command in ["n", "north"]:
        attempt_move("north")
    
    elif command in ["s", "south"]:
        attempt_move("south")
    
    elif command in ["e", "east"]:
        attempt_move("east")
    
    elif command in ["w", "west"]:
        attempt_move("west")
    
    else:
        print("Sorry, I don't know that command")
    
    time.sleep(.3)  # pause for a moment, helps player see what happens better

# Out of the loop, game is over
print("Thanks for playing!")
