from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("outside", "Outside Cave Entrance",
                     "North of you, the cave mount beckons \n"),

    'foyer':    Room("foyer", "Foyer", """Dim light filters in from the south. Dusty
passages run north and east. \n"""),

    'overlook': Room("overlook", "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. \n"""),

    'narrow':   Room("narrow", "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air. \n"""),

    'treasure': Room("treasure", "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south. \n"""),
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
# test = room['outside'].s_to
# print(test)

name = input("\n Enter a name, adventurer: ")

playerStart = Player(name, room['outside'])
print(playerStart)
# Make a new player object that is currently in the 'outside' room.
directionInput = input("What direction would you like to go? n,e,s,w (q to quit): ")

currentRoom = 'outside'
while not directionInput == "q":

    ##User chose North
    if directionInput == "n":
        roomID = room[currentRoom].refID
        
        try:
            print(room[roomID].n_to)

            currentRoom = room[roomID].n_to.refID
            
        except AttributeError:
            print("That direction isn't available")

    ##User chose East
    elif directionInput == "e":
        roomID = room[currentRoom].refID

        try: 
            print(room[roomID].e_to)

            currentRoom = room[roomID].e_to.refID

        except AttributeError:
            print("That direction isn't available")

    ##User chose South
    elif directionInput == "s":
        roomID = room[currentRoom].refID
    
        try: 
            print(room[roomID].s_to)

            currentRoom = room[roomID].s_to.refID

        except AttributeError:
            print("That direction isn't available")

    ##User chose West
    elif directionInput == "w":
        roomID = room[currentRoom].refID

        try:
            print(room[roomID].w_to)

            currentRoom = room[roomID].w_to.refID

        except AttributeError:
            print("That direction isn't available")
    
    else:
        print("Invalid selection")

    ##Reselect promt
    directionInput = input("What direction would you like to go? n,e,s,w (q to quit): ")

print("Good job adventurer! See you next time \n")

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