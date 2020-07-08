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
new_player = Player("Krishna", room['outside'])
# Write a loop that:
while True:
    
# Prints the current room name
    current_room = new_player.location
    print(f"Hey, you're {current_room.name}.")

# * Prints the current description (the textwrap module might be useful here).
    print(f"Hey, your room {current_room.name} is described as: {current_room.description}")

# * Waits for user input and decides what to do.
    player_input = input("Enter your next movement n, s, w, e or q for quit: ")

# If the user enters a cardinal direction, attempt to move to the room there.
    if player_input == "n":
        if current_room.n_to is not None:
            new_player.current_room = current_room.n_to
            print(f"You selected North. Now entering {new_player.current_room.name}")
        else:
            print(f"No room on that side. Try another side")
    elif player_input == "s":
        if current_room.s_to is not None:
            new_player.current_room = current_room.s_to
            print(f"You selected South. Now entering {new_player.current_room.name}")
        else:
            print(f"No room on that side. Try another side")
    elif player_input == "w":
        if current_room.w_to is not None:
            new_player.current_room = current_room.w_to
            print(f"You selected West. Now entering {new_player.current_room.name}")
        else:
            print(f"No room on that side. Try another side")
    elif player_input == "e":
        if current_room.e_to is not None:
            new_player.current_room = current_room.e_to
            print(f"You selected East. Now entering {new_player.current_room.name}")
        else:
            print(f"No room on that side. Try another side")

# If the user enters "q", quit the game.
    elif player_input == "q":
        print("You selected to quit. Bye!")
        exit()

# Print an error message if the movement isn't allowed.
    else:
        print("Please check controls. n, s, w, s or q for quit only allowed")
