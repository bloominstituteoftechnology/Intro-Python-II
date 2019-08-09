from room import Room
from player import Player
from item import Item

item = {
    "cane": Item("cane", "typical walking cane made of wood"),
    "candlestick": Item("candlestick", "made of brass with a small nub of a candle left")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item["cane"], item["candlestick"]]),

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
currentLocation = room['outside']
character = Player(currentLocation)
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
playing = True
print("Type look to see if there are any items in the room")
print("Type q to quit")
while(playing):
    print(f"\n{character}")
    request = input("What would you like to do?\n\n").lower().split(' ')

    if len(request) == 1:
        if request [0] == 'q' or request[0] == 'quit':
            print("\nThanks for Playing!")
            playing = False
        elif request[0] == 'look':
            print(f"\nItems in room: {currentLocation.print_items()}")
        else:
            if request.count('north') > 0 or request.count('n') > 0:
                if hasattr(currentLocation, 'n_to'):
                    currentLocation = currentLocation.n_to
                    character.move_location(currentLocation)
                else:
                    print("\nInvalid Request")
            elif request.count('east') > 0 or request.count('e') > 0:
                if hasattr(currentLocation, 'e_to'):
                    currentLocation = currentLocation.e_to
                    character.move_location(currentLocation)
                else:
                    print("\nInvalid Request")
            elif request.count('south') > 0 or request.count('s') > 0:
                if hasattr(currentLocation, 's_to'):
                    currentLocation = currentLocation.s_to
                    character.move_location(currentLocation)
                else:
                    print("\nInvalid Request")
            elif request.count('west') > 0 or request.count('w') > 0:
                if hasattr(currentLocation, 'w_to'):
                    currentLocation = currentLocation.w_to
                    character.move_location(currentLocation)
                else:
                    print("\nInvalid Request")
            else:
                print("\nInvalid Request")



