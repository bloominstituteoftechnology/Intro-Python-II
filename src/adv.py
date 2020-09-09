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
username = input("Please put in your name: ")
# Make a new player object that is currently in the 'outside' room.
player = Player(username, room['outside'])
# Write a loop that:

while player.current_room:
    # * Prints the current room name
    print(f"Current room: {player.current_room.name}")
# * Prints the current description (the textwrap module might be useful here).
    print(f"{player.current_room.description}")
    print("-------------------------------------------------------------------------")
# * Waits for user input and decides what to do.
    selection = input("Please pick a direction to go in (North = n, South = s, West = w, East = e): ")
    print('-------------------------------------------------------------------------')
# If the user enters a cardinal direction, attempt to move to the room there.
    if selection == 'n':
        if player.current_room.n_to is None:
            print(f"There is nothing north of {player.current_room.name}. Please pick another direction.")
        else:
            player.current_room = player.current_room.n_to
    elif selection == 's':
        if player.current_room.s_to is None:
            print(f"There is nothing south of {player.current_room.name}. Please pick another direction.")
        else:
            player.current_room = player.current_room.s_to
    elif selection == 'w':
        if player.current_room.w_to is None:
            print(f"There is nothing west of {player.current_room.name}. Please pick another direction.")
        else:
            player.current_room = player.current_room.w_to
    elif selection == 'e':
        if player.current_room.e_to is None:
            print(f"\nThere is nothing east of {player.current_room.name}. Please pick another direction.")
        else:
            player.current_room = player.current_room.e_to
    elif selection == 'q':
        print("Thank you for playing!")
        player.current_room = False # Get out of game
# Print an error message if the movement isn't allowed.
    else:
        print(selection + " wasn't allowed. Please pick another valid direction.")
# If the user enters "q", quit the game.