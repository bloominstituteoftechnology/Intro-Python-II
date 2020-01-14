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
player = Player("player1", room['outside'])

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

def get_room_and_input():
    print(f"Room: {player.current_room.name}, description: {player.current_room.description}")
    move = input("What direction would you like to go? (n, e, w, s)")
    return move

def bad_direction():
    print()
    print("There is no room in that direction. Please choose another direction.")
    print()

if __name__ == "__main__":
    directions = ['n', 's', 'e', 'w']
    move = get_room_and_input()

    while not move == 'q':
        if move in directions:
            if move == 'n':
                if (hasattr(player.current_room, "n_to")):
                    print("You went north.")
                    player.current_room = player.current_room.n_to
                else:
                    bad_direction()

            elif move == 'e':
                if (hasattr(player.current_room, "e_to")):
                    print('You went east.')
                    player.current_room = player.current_room.e_to
                else:
                    bad_direction()

            elif move == 's':
                if (hasattr(player.current_room, "s_to")):
                    print('You went south.')
                    player.current_room = player.current_room.s_to
                else:
                    bad_direction()

            else:
                if (hasattr(player.current_room, "w_to")):
                    print('You went west')
                    player.current_room = player.current_room.w_to
                else:
                    bad_direction()               

            print()
            move = get_room_and_input()
            # print(f"Room: {player.current_room.name}, description: {player.current_room.description}")
            # move = input("What direction would you like to go? (n, e, w, s)")
