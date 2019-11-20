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

'secret': Room("Secret Chamber", """CONGRATULATIONS! You have found the secret 
chamber! There may be no treasures left but, grab a bottle of 
our oldest bourbon and relax in triumph knowing you found the real treasure"""),
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
room['treasure'].e_to = room['secret']
room['secret'].w_to = room['treasure']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

currentRoom = "outside"
playerName = input("Enter Player Name: ")

while True:
    player = Player(playerName, currentRoom)
    playerRoom = Room(room[currentRoom].playerName, room[currentRoom].description)
    print(playerRoom)
    print(player)

    path = input("Which way do you go (n,s,w,e)? Enter your decision: ")

    if path == "q":
        exit()

    elif currentRoom == "outside":
        if path == "n":
            currentRoom = "foyer"
        else:
            print("Sorry, that path is not available")    
            continue

    elif currentRoom == "foyer":
        if path == "n":
            currentRoom = "overlook"
        elif path == "s":
            currentRoom = "outside"
        elif path == "e":
            currentRoom = "narrow"    
        else:
            print("Sorry, that path is not available")    
            continue

    elif currentRoom == "overlook":
        if path == "s":
            currentRoom = "foyer"
        else:
            print("Sorry, that path is not available")    
            continue

    elif currentRoom == "narrow":
        if path == "n":
            currentRoom = "treasure"
        elif path == "w":
            currentRoom = "foyer"   
        else:
            print("Sorry, that path is not available")    
            continue

    elif currentRoom == "treasure":
        if path == "s":
            currentRoom = "narrow"
        elif path == "e":
            currentRoom = "secret"    
        else:
            print("Sorry, that path is not available")    
            continue

    elif currentRoom == "secret":
        if path == "w":
            currentRoom = "treasure"    
        else:
            print("Sorry, that path is not available")    
            continue
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
