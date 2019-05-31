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
    "Staff": Item("Staff", "For walking and fighting"),
    "Health Potion": Item("Health Potion", "For preventing death")

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

room["outside"].items = [str(item["Staff"]), str(item["Health Potion"])]

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

name = input("Enter your player name choice\n")

player = Player(name, room["outside"])

while True:
    print(f"you are in room: {player.room.name}\n carrying items: {player.items}\n and the room has items: {player.room.items}\n {player.room.description}")
    moveChoice = input("choose a move: n, s, e or w, or enter q to quit\n")
    print(f"you chose {moveChoice}\n")
    if moveChoice == 'n' or moveChoice == 's' or moveChoice == 'w' or moveChoice == 'e' or moveChoice == 'q':
        if moveChoice == "n":
            player.room = player.room.n_to
        elif moveChoice == "s":
            player.room = player.room.s_to
        elif moveChoice == "w":
            player.room == player.room.w_to
        elif moveChoice == "e":
            player.room == player.room.e_to
        elif moveChoice == "q":
            print("exiting the game now, goodbye")
            break
        #this ability to grab items not working yet    
        # elif moveChoice == 'get':
        #     player.items.append(moveChoice)
        #     print("Item grabbed, good job!")
        else:
            print("c'mon, enter a correct direction choice, man!")