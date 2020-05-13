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
name = input('\nWelcome to Adventure game, what shall we call you...? \n\n')

# Make a new player object that is currently in the 'outside' room.

player = Player(name, room['outside'])

print(f'\nWelcome {player.name} to the mysterious adventure lands... You are currently located {player.current_room} \n\n')
print(f'\nTo play the game you may select a direction using N, S, E, W, and to quit the game use Q')

# Write a loop that:
while True:

# * Prints the current room name

# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
    selection = input("\nEnter a direction or q to escape:\n")

    user_selection = selection.lower().split(" ")
    print(user_selection)

    if len(user_selection) == 1 and selection == "q":
        print("We shall meet again...")
        break
    elif selection == "n" or selection == "s" or selection == "e" or selection == "w":
            player.move(selection)
            print(f'You are now located {player.current_room}\n')
    else:
        print(f'{selection} is not a valid command, try using N, S, E, W... or Q to quit.\n')

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
