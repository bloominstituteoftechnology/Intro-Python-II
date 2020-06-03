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

'''Runs the game when called from main'''


def _run_game():
    running = True  # let's us know if the game is running

    # takes in user name first
    user_input = input('Greetings adventurer! What is your name?\n>> ')

    # Make a new player object that is currently in the 'outside' room.
    player1 = Player(user_input, room['outside'])  # todo, verify string??

    # game logic
    # Write a loop that:
    while (running is not False):
        # * Prints the current room name
        # * Prints the current description (the textwrap module might be useful here).
        player1._print_current_location()

        # * Waits for user input and decides what to do.
        user_input = input(
            'What would like to do next? [o] for options.\n >> ')

        # cardinal directions
        cardinal_directions = ['n', 's', 'e', 'w']

        # If the user enters a cardinal direction, attempt to move to the room there.
        if user_input in cardinal_directions:
            try:
                player1._move(user_input)
        # Print an error message if the movement isn't allowed.
            except ValueError:
                print('Sorry.')  # Todo: create real errors

        # If the user enters "q", quit the game.
        if user_input is 'q':
            running = False
            print('Goodbye!')


if __name__ == "__main__":
    _run_game()
