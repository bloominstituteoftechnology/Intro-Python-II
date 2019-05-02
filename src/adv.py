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
# Main - Developed by Ben Hakes
#

# Make a new player object that is currently in the 'outside' room.
player_name = str(input("Please enter the name of player\n"))

print("\n")
player = Player(player_name, room['outside'])
possibleMoves = {"n", "s", "e", "w"}
directionPrompt = "Press [n,s,e,w] to move in a direction"
print(f'Press a cardinal direction key [n,s,e,w] to move or press "q" to quit.')

# Write a loop that:
enteredValue = "c"

# gameplay loop
# If the user enters "q", quit the game.
while not enteredValue == "q":

    # Prints the current room name
    # Prints the current description (the textwrap module might be useful here).
    print("\n<****--------****>")
    print(f'You are {player.room.name}, Sir {player.name}.')
    print(f'{player.room.description}.')
    print("<****--------****>\n")

    # Waits for user input and decides what to do.
    enteredValue = str(input(f'{directionPrompt}\n'))

    if enteredValue == "q":
        break
    elif enteredValue in possibleMoves:

        # If the user enters a cardinal direction, attempt to move to the room there.
        if enteredValue == "n":
            if player.room.n_to == None:
                print("\n*****Error*****\nThere is no room in that direction. Try again.\n*****Error*****")
            else:
                player.room = player.room.n_to
        elif enteredValue == "s":
            if player.room.s_to == None:
                print("\n*****Error*****\nThere is no room in that direction. Try again.\n*****Error*****")
            else:
                player.room = player.room.s_to
        elif enteredValue == "e":
            if player.room.e_to == None:
                print("\n*****Error*****\nThere is no room in that direction. Try again.\n*****Error*****")
            else:
                player.room = player.room.e_to
        else:
            if player.room.w_to == None:
                print("\n*****Error*****\nThere is no room in that direction. Try again.\n*****Error*****")
            else:
                player.room = player.room.w_to
    else:
        # Print an error message if the movement isn't allowed.
        print("\n***** ERROR *****")
        print("The key you entered is not an allowed move.")
        print("Please try again with an allowed move [n,s,e,w].")
        print("***** ERROR *****\n")
        
        enteredValue = str(input(f'{directionPrompt}\n'))
  
