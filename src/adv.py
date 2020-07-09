import sys
from room import Room
from player import Player
# from parser import parser

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


if __name__ == "__main__":
    

    # Make a new player object that is currently in the 'outside' room.

    player1 = Player("Mercedes", room['outside'])
    print(f"Hello {player1.name}! Welcome to The Adventure Game ...")

    choices = ["n","s","e","w"]

    # Write a loop that:
    while True:
        # * Prints the current room name
        print(f"\nYOUR CURRENT {player1.current_room}")

        # * Prints the current description (the textwrap module might be useful here).
        # print(f"\nLOCATION INFO: {player1.current_room.description}")

        # * Waits for user input and decides what to do.
        action = input("\nPlease enter a directional move (n, s, e or w; q to quit): ")
        action = action.strip().lower().split()[0]
        action = action[0]

        
        # If the user enters a cardinal direction, attempt to move to the room there.
        if action in choices:
        #   print(f"\nUSER SELECTION: {action}")
            player1.try_direction(action)  

        # Print an error message if the movement isn't allowed.
        elif action not in choices and action != "q":
            print("\nERROR: invalid movement")

        # If the user enters "q", quit the game.
        elif action == "q":
            sys.exit("\nThanks for playing!")
