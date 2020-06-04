from room import Room
from player import Player
from item import Item
import textwrap
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

dournbrood = Player(room["outside"])

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

# Declare all the items

item = {
    "sword": Item('Sword', 'a plain-looking sword known as the Sword of Resolute Destruction "Hakai\'s Embrace". \nThis item will instantly kill any enemy it comes into contact with. No traces of the body or being will be left behind.'),
    "shield": Item('Shield', 'a plain-looking shield known as the Shield of Universal Entropy "Hakai\'s Dissolution". \nThis item blocks all incoming damage to the bearer, regardless of its position.')
}

# Assign items to rooms

room["outside"].addItem(item["sword"])
room["outside"].addItem(item["shield"])

# Create commands list
commands = {
    "move": [
        "move",
        "walk",
        "run",
        "climb",
        "swim",
        "swing",
        "crawl",
        "jump"
    ],
    "pickup": [
        "get",
        "take"
    ],
    "place": [
        "drop"
    ]
}

# Other global variables
lastCommand = None

while 1:
    if lastCommand == None or lastCommand in commands["move"]:
        dournbrood.room.printStats()

    if lastCommand in commands["pickup"] or lastCommand in commands["place"]:
        dournbrood.room.printInventory()

    print("Your command: ", end="")
    commandArgs = str.lower(input()).split(" ")

    lastCommand = commandArgs[0]

    if str(commandArgs[0]) == "q":
        quit()

    elif str(commandArgs[0]) in commands["move"]:
        if commandArgs.__len__() <= 1:
            print("Please specify a cardinal direction.")
        else:
            for direction in commandArgs[1::1]:
                dournbrood.moveTo(direction)

    elif str(commandArgs[0]) in commands["pickup"]:
        if commandArgs.__len__() <= 1:
            print("Please specify item(s) to pick up!")
        else:
            for item in commandArgs[1::1]:
                dournbrood.takeItem(item)

    elif str(commandArgs[0]) in commands["place"]:
        if commandArgs.__len__() <= 1:
            print("Please specify item(s) to drop!")
        else:
            for item in commandArgs[1::1]:
                dournbrood.dropItem(item)

    else:
        print(f"Command '{commandArgs[0]}' not found!")
