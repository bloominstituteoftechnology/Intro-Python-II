from room import Room
from player import Player
from item import Item
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
def my_adv_game():
    print("Adventure Game")

# Make a new player object that is currently in the 'outside' room.
    player_input = input("If you want Treasure, enter [P]lay or [Q]uit if you don't want Treasure.")
    if player_input.lower() == 'p':
        new_player = Player(input("Please enter your name adventurer: "), room['outside'])
        print("*" * 50)
        print("*" * 50)
        print(f"            Adventurer {new_player.name}            ")
        print("*" * 50)
        print("*" * 50)

# Write a loop that:
        card_directions = ['n', 's', 'e', 'w', 'q']
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

    print("You may choose to travel [N]orth, [S]outh, [E]ast, or [W]est")
    while True:
        print(f"You current location is: {new_player.current_room.name}.")
        print(f"{new_player.current_room.description}.")
        print("*" * 50)
        player_choice = input(f"Choose a direction to travel in your hunt for the Treasure!")
        print("*" * 50)

        if player_input.lower() == 'q':
            print("Please play again soon!")
            sys.exit()
        elif player_choice.lower() in card_directions:
            new_player.move_player(player_choice.lower())
        else:
            print(f"That is not a valid direction to travel")


my_adv_game()