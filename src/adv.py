from room import Room
from item import Item
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",  "Coin"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",  "Lamp"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "Sword"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "Gold"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",  "Treasures"),
}


# Link rooms together

room['outside'].n = room['foyer']
room['foyer'].s = room['outside']
room['foyer'].n = room['overlook']
room['foyer'].e = room['narrow']
room['overlook'].s = room['foyer']
room['narrow'].w = room['foyer']
room['narrow'].n = room['treasure']
room['treasure'].s = room['narrow']



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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


name = input("Enter your name: ")
room = room['outside']
player = Player(name, room)

print(f'Welcome {player.name}!')  

choice = input("To move, enter a direction n/s/e/w; to get your inventory list, enter i; to quit, enter q ").lower()

while not choice == 'q':
    # # user chooses North
    if choice == 'n':
        # room = room['foyer']
        print(f'Your location is {player.room.name}!')
        print(player.room.description)
        choice = input("To move, enter a direction n/s/e/w; to get your inventory list, enter i; to quit, enter q ").lower()
        break
    else:
        print("Invalid direction")
        break

    # user chooses East
    if choice == 'e':
         room = room['narrow']
         print(f'Your location is {player.room.name}!')
         print(player.room.description)
         choice = input("To move, enter a direction n/s/e/w; to get your inventory list, enter i; to quit, enter q ").lower()
         break
    # user chooses North
    if choice == 'n': 
         room['overlook']
         print(f'Your location is {player.room.name}!')
         print(player.room.description)
         choice = input("To move, enter a direction n/s/e/w; to get your inventory list, enter i; to quit, enter q ").lower()
         break
    # user chooses South
    if choice == 's': 
         room['outside']
         print(f'Your location is {player.room.name}!')
         print(player.room.description)
         choice = input("To move, enter a direction n/s/e/w; to get your inventory list, enter i; to quit, enter q ").lower()
         break
    else:
         print("Invalid direction")
         break        
                    
