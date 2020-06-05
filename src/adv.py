from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("---Outside Cave Entrance",
                     "---North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """---Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("---Grand Overlook", """---A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("---Narrow Passage", """---The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("---Treasure Chamber", """---You've found the long-lost treasure
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
welcome_quote = """--Welcome to The Castle Of Treasures! You are in the outside room,
--to find your way to the treasure room,
--you can move around the castle by typing
--'up', 'down', 'right', 'left'
-- and 'quit' to exit game."""

# Make a new player object that is currently in the 'outside' room.
player_name = input("Enter Your Name:")
player1 = Player(player_name , room['outside'])
print(player1)
# Write a loop that:
# # * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
movement = ['up', 'down', 'right', 'left', 'quit']
selection = ['y', 'n']

answer = ""

while answer not in selection:
    answer = input(f"Would you like to start your adventure?:{selection}")

    if answer.lower().strip() == 'y':
        print(welcome_quote)

        user_input = ""

        while user_input not in movement:
            user_input = input(f'please select: {movement}')

            if user_input.lower().strip() == 'up':
                player1.cardinal_dir(user_input)
                print(f'---Welcome to {player1.current_room}')
                user_input = ""
            
            elif user_input.lower().strip() == 'down':
                player1.cardinal_dir(user_input)
                print(f'---Welcome to {player1.current_room}')
                user_input = ""

            elif user_input.lower().strip() == 'left':
                player1.cardinal_dir(user_input)
                print(f'---Welcome to {player1.current_room}')
                user_input = ""
            
            elif user_input.lower().strip() == 'right':
                player1.cardinal_dir(user_input)
                print(f'---Welcome to {player1.current_room}')
                user_input = ""
            
            elif user_input.lower().strip() == 'quit':
                print('----The game will now quit----')
                exit(0)
            
            else:
                print('Incorrect input, Please try again!')
                user_input = ""

    elif answer.lower().strip() == 'n':
        print('----Game Over----')
        exit(0)

    else:
        print('Incorrect input, Please try again!')
        answer = ""
