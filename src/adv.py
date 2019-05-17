from room import Room
from player import Player
from item import Item


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

item = {
    "Laser": Item("Laser", "Makes cool sounds like 'beem! beem!' and 'bzow! bzow!"),
    "Invisible Hat": Item("Invisible Hat", "Features a really awesome secret logo that no one will be able to see!")

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

room["outside"].items = [item["Laser"], item["Invisible Hat"]]
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


currentRoom = room["outside"]

name = input("Please enter your name")
player = Player(name, room["outside"])

def describe(sub):
    print(f"\n{sub.name}, {sub.room}")
    if sub.room.items == []:
        print("Looks like there's no items to be found in this room.")
    elif len(sub.room.items) == 2:
        print(f"This room contains a {sub.room.items[0].name} as well as a {sub.room.items[1].name}.")
    else:
        print(f"This room contains a {sub.room.items[0].name}.")


action = ""

while action != "Q":
    describe(player)
    print(player.room.displayItems())
    action = input("[N] North [S] South [E] East [W] West [Q] Quit\n")

    if action == "N" or action == "S" or action == "E" or action == "W":
        if action == "N" and player.room.n_to != None:
            player.room = player.room.n_to
        elif action == "E" and player.room.e_to != None:
            player.room = player.room.e_to
        elif action == "S" and player.room.s_to != None:
            player.room = player.room.s_to
        elif action == "W" and player.room.w_to != None:
            player.room = player.room.w_to
        else:
            print("Your not allowed to take that path, friend :(")
    elif action == "Q":
        print("Farewell dear wanderer")
        break
    elif action.split()[0] == "GET" and player.room.items:
        player.inv.append(action.split()[1])
        player.room.items.remove(action.split()[1])
        print(f"{player.name} carefully observes the {item[action.split()[1]]}.")
        print(f"{item[action.split()[1]].description}")
    elif action.split()[0] == "DROP" and player_item_check(action.split()[1]):
        player.inv.remove(action.split()[1])
        player.room.items.append(item[action.split()[1]])
        print(f"\nYou have dropped the {action.split()[1]}.")
    else:
        print("Ummm no! Please choose one of the four directions: N, S, E, or W")