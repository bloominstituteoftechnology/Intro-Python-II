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
possDirections = {
    "n": "North",
    "s": "South",
    "e": "East",
    "w": "West",
    "x": "Exit"
}

player = Player("Kilroy", room['outside'])
direction = ''
printedLoc = ""

print("Welcome, {}! You are have found yourself near a spooky mansion.".format(player.name))

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


while direction != 'x':
    inputOpts = ""
    print(player.currentLoc)
    for opt in possDirections:
        inputOpts += '\n- %s (%s)' % (possDirections[opt], opt)

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
    while direction != 'x':
        direction = input(inputOpts + '\nWhich direction do you choose? :')
        try:
            youWent = "\nYou chose to move " + possDirections[direction]
            if direction == "n":
                player.currentLoc = player.currentLoc.n_to
                print(youWent)
                break
            elif direction == "w":
                player.currentLoc = player.currentLoc.w_to
                print(youWent)
                break
            elif direction == "e":
                player.currentLoc = player.currentLoc.e_to
                print(youWent)
                break
            elif direction == "s":
                player.currentLoc = player.currentLoc.s_to
                print(youWent)
                break
            elif direction == "x":
                print("\n\nThanks for playing!!")
            else:
                print("\n\n\nPlease enter a valid direction.")
        except KeyError:
            print('\nPlease choose a valid option: n, s, e, w, or x\n')
            print(player.currentLoc)
        except AttributeError:
            print("\nRead the description carefully and choose again.\n")
            print(player.currentLoc)


# If the user enters "q", quit the game.
