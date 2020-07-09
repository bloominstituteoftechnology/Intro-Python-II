"""
Old version of parser / refactoring attempt
"""

if __name__ == "__main__":
    

    # Make a new player object that is currently in the 'outside' room.

    player1 = Player("Mercedes", room['outside'])
    print(f"Hello {player1.name}! Welcome to The Adventure Game ...")

    choices = ["n","s","e","w"]
    # outside_choices = []
    foyer_choices = ["n","e","s"]
    # overlook_choices = []
    narrow_choices = ["w","n"]
    # treasure_choices = []


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
        #     print(f"\nUSER SELECTION: {action}")

        #     # # Apply parser function
        #     # parser(player1.current_room, action)

        #     # Rules for outside
        #     if player1.current_room == room["outside"] and action == "n":
        #         player1.current_room = player1.current_room.n_to
        #     elif player1.current_room == room["outside"] and action != "n":
        #         print("\nINVALID MOVE: Can only go N from outside ... or quit if you're afraid.")

        #     # Rules for foyer
        #     elif player1.current_room == room["foyer"]:
        #         # Foyer - north
        #         if action == "n":
        #             player1.current_room = player1.current_room.n_to
        #         # Foyer - east
        #         elif action == "e":
        #             player1.current_room = player1.current_room.e_to
        #         # Foyer - south
        #         elif action == "s":
        #             player1.current_room = player1.current_room.s_to
        #         elif action not in foyer_choices and action != "q":
        #             print("\nINVALID MOVE: Can only go N, E or S from foyer ... or quit if you're afraid.")   

        #     # Rules for overlook
        #     elif player1.current_room == room["overlook"] and action == "s":
        #         player1.current_room = player1.current_room.s_to
        #     elif player1.current_room == room["overlook"] and action != "s":
        #         print("\nINVALID MOVE: Can only go S from overlook ... or quit if you're afraid.")

        #     # Rules for narrow
        #     elif player1.current_room == room["narrow"]:
        #         # Narrow - west
        #         if action == "w":
        #             player1.current_room = player1.current_room.w_to
        #         # Narrow - north
        #         elif action == "n":
        #             player1.current_room = player1.current_room.n_to
        #         # Narrow - invalid
        #         elif action not in narrow_choices and action != "q":
        #             print("\nINVALID MOVE: Can only go W or N from narrow ... or quit if you're afraid.")

        #     # Rules for treasure
        #     elif player1.current_room == room["treasure"] and action == "s":
        #         player1.current_room = player1.current_room.s_to
        #     elif player1.current_room == room["treasure"] and action != "s":
        #         print("\nINVALID MOVE: Can only go S from treasure room ... or quit if you're over it.")

        # Print an error message if the movement isn't allowed.
        elif action not in choices and action != "q":
            print("\nERROR: invalid movement")

        # If the user enters "q", quit the game.
        elif action == "q":
            sys.exit("\nThanks for playing!")



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

### PARSER FUNCTION

def parser(player_loc, action):
    """
    REPL parser to receive user directional commands to move between rooms.

    Params: 

        player_loc: player location, ex. `player1.current_room`

        action: user directional command, ex. "n"
    """

    # Link rooms together
    room['outside'].n_to = room['foyer']
    room['foyer'].s_to = room['outside']
    room['foyer'].n_to = room['overlook']
    room['foyer'].e_to = room['narrow']
    room['overlook'].s_to = room['foyer']
    room['narrow'].w_to = room['foyer']
    room['narrow'].n_to = room['treasure']
    room['treasure'].s_to = room['narrow']

    # Rules for outside
    if player_loc == room["outside"] and action == "n":
        player_loc = player_loc.n_to
    elif player_loc == room["outside"] and action != "n":
        print("\nINVALID MOVE: Can only go N from outside ... or quit if you're afraid.")

    # Rules for foyer
    elif player_loc == room["foyer"]:
        # Foyer - north
        if action == "n":
            player_loc = player_loc.n_to
        # Foyer - east
        elif action == "e":
            player_loc = player_loc.e_to
        # Foyer - south
        elif action == "s":
            player_loc = player_loc.s_to
        elif action not in foyer_choices and action != "q":
            print("\nINVALID MOVE: Can only go N, E or S from foyer ... or quit if you're afraid.")   

    # Rules for overlook
    elif player_loc == room["overlook"] and action == "s":
        player_loc = player_loc.s_to
    elif player_loc == room["overlook"] and action != "s":
        print("\nINVALID MOVE: Can only go S from overlook ... or quit if you're afraid.")

    # Rules for narrow
    elif player_loc == room["narrow"]:
        # Narrow - west
        if action == "w":
            player_loc = player_loc.w_to
        # Narrow - north
        elif action == "n":
            player_loc = player_loc.n_to
        # Narrow - invalid
        elif action not in narrow_choices and action != "q":
            print("\nINVALID MOVE: Can only go W or N from narrow ... or quit if you're afraid.")

    # Rules for treasure
    elif player_loc == room["treasure"] and action == "s":
        player_loc = player_loc.s_to
    elif player_loc == room["treasure"] and action != "s":
        print("\nINVALID MOVE: Can only go S from treasure room ... or quit if you're over it.")


    return player_loc





if __name__ == "__main__":
    
    # Link rooms together

    room['outside'].n_to = room['foyer']
    room['foyer'].s_to = room['outside']
    room['foyer'].n_to = room['overlook']
    room['foyer'].e_to = room['narrow']
    room['overlook'].s_to = room['foyer']
    room['narrow'].w_to = room['foyer']
    room['narrow'].n_to = room['treasure']
    room['treasure'].s_to = room['narrow']

    # Make a new player object that is currently in the 'outside' room.

    player1 = Player("Mercedes", room['outside'])
    print(f"Hello {player1.name}! Welcome to The Adventure Game ...")

    choices = ["n","s","e","w"]
    # outside_choices = []
    foyer_choices = ["n","e","s"]
    # overlook_choices = []
    narrow_choices = ["w","n"]
    # treasure_choices = []


    # Write a loop that:
    while True:
        # * Prints the current room name
        print(f"\nYOUR CURRENT {player1.current_room}")

        # * Waits for user input and decides what to do.
        action = input("\nPlease enter a directional move (n, s, e or w; q to quit): ")

        # If the user enters a cardinal direction, attempt to move to the room there.
        if action in choices:
            print(f"\nUSER SELECTION: {action}")

            # Apply parser function
            parser(player1.current_room, action)

        # Print an error message if the movement isn't allowed.
        elif action not in choices and action != "q":
            print("\nERROR: invalid movement")

        # If the user enters "q", quit the game.
        elif action == "q":
            sys.exit("\nThanks for playing!")
