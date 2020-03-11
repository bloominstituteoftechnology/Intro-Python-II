from room import Room
from item import Item


# Declare an item or two
item = {
    'Flashlight' : Item('Flashlight', 'helps with lighting the way worth 50pts')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['Flashlight']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['Flashlight']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['Flashlight']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",  [item['Flashlight']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item['Flashlight']]),
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

from player import Player
player = Player("You", room['outside'], items=[])


#validator for the item:

if len(player.currentRoom.items) > 0:
    print("\nFound:")
    for item in player.currentRoom.items:
        print(item.name)
else:
    print("\nThere is nothing there!")




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


play = True

justOnce = True

# declaring actions for moving 

# 0 represents the word typed in and 1 represents the item name 

def getInput():
    action = input("What would you like to do? Action: ")
    print("\n")
    if action[0] == "q":
        global play 
        global justOnce
        play = False
        foundItems = False

    elif action[0] == "n":
        if player.currentRoom.playerMove("n") == True:
            player.currentRoom = player.currentRoom.n_to
        if len(player.currentRoom.items) > 0:
            print("\nFound:")
            for item in player.currentRoom.items:
                print(item.name)
        else:
            print("\nThere is nothing there!")
            
    elif action[0] == "e":
        if player.currentRoom.playerMove("e") == True:
            player.currentRoom = player.currentRoom.e_to
        if len(player.currentRoom.items) > 0:
            print("\nFound:")
            for item in player.currentRoom.items:
                print(item.name)
        else:
            print("\nThere is nothing there!")
    elif action == "s":
        if player.currentRoom.playerMove("s") == True:
            player.currentRoom = player.currentRoom.s_to
        if len(player.currentRoom.items) > 0:
            print("\nFound:")
            for item in player.currentRoom.items:
                print(item.name)
        else:
            print("\nThere is nothing there!")
    elif action[0] == "w":
        if player.currentRoom.playerMove("w") == True:
            player.currentRoom = player.currentRoom.w_to
        if len(player.currentRoom.items) > 0:
            print("\nFound:")
            for item in player.currentRoom.items:
                print(item.name)
        else:
            print("\nThere is nothing there!")
           # trying to pick up an item here
    elif action[0] == "take" or action[0] == "get":
        foundItems = False
        for item in player.currentRoom.items:
            if action == item.name:
            # remove from room and add to player
                player.currentRoom.items.remove(item)
                player.items.append(item)
                print(f"{player.name} picked up {action[0]} from {player.currentRoom.name}")
                foundItems = True
            if foundItems == False:
                print(f"could not find {action[0]}")

    else:
        print (f"\n'{action}' is not valid input")
        getInput()
        
        
while play:

    if justOnce:

        justOnce = False
        print("Use\n" +
        "'n' 'e' 's' or 'w' to go north, east, south, or west.\n" +
        "'q' to quit 'c' to show controls again")
    print("\n" + player.currentRoom.__str__())

    getInput()
