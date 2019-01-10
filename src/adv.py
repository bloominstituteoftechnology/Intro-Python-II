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

room['treasure'].items.append(Item("ladder", "Used to climb, or perhaps use as a bridge."))
#room['foyer'].items.append(Item("10 coins", "Can be used to trade for better goods, or purchase more lives."))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

player.inventory.append(Item("wallet", "A wallet with a hole in it."))

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

while True:
    currentRoom = player.currentRoom
    
    print(f"You are in {currentRoom.name}")
    print(textwrap.fill(currentRoom.description, width = 80))
    print()    # extra line
    action = input("=> What would you like to do? ")
    print("")    # extra line
    
    if action == "q" or action == "quit":
        print("> You have escaped with your wits, for now...")
        break
    elif action == "n" or action == "go north":
        try:
            player.currentRoom = currentRoom.n_to
            print("> You go north.")
        except:
            print("> You cannot go north from here.")
    elif action == "e" or action == "go east":
        try:
            player.currentRoom = currentRoom.e_to
            print("> You go east.")
        except:
            print("> You cannot go east from here.")
    elif action == "s" or action == "go south":
        try:
            player.currentRoom = currentRoom.s_to
            print("> You go south.")
        except:
            print("> You cannot go south from here.")
    elif action == "w" or action == "go west":
        try:
            player.currentRoom = currentRoom.w_to
            print("> You go west.")
        except:
            print("> You cannot go west from here.")
    elif action == "l" or action == "look around":
        if len(currentRoom.items) == 0:
            print("> There is nothing of interest here.")
        else:
            print("> You see the following items:")
            for item in currentRoom.items:
                print(f"    {item.name}: {item.description}")
    elif action.startswith("take "):
        grabbedSomething = False
        verbObject = action[5:]
        
        for item in currentRoom.items:
            if verbObject == item.name:
                player.inventory.append(item)
                print(f"> You took the {item.name}.")
                currentRoom.items.remove(item)
                item.on_take()
                grabbedSomething = True
                break
        
        if not grabbedSomething:    # if user didn't grab anything that is valid
            print(f"> There is no {verbObject}. Are you losing your sanity?")
    elif action.startswith("drop "):
        droppedSomething = False
        verbObject = action[5:]
        
        for item in player.inventory:
            if verbObject == item.name:
                currentRoom.items.append(item)    # drop the item user doesn't want
                print(f"> You dropped the {item.name}.")
                player.inventory.remove(item)    # remove the item user dropped
                item.on_drop()
                droppedSomething = True
                break
        
        if not droppedSomething:    # if user didn't drop anything that is valid
            print(f"> You have no {verbObject}. Are you losing your marbles? Here are 5 marbles!")
            player.inventory.append(Item("marbles", "Some marbles because you keep forgetting."))
    elif action == "i" or action == "inventory":
        if len(player.inventory) == 0:
            print("> You have nothing on you.")
        else:
            print("> You find the following items on your person:")
            for item in player.inventory:
                print(f"    {item.name}: {item.description}")
    
    
    elif action == "h" or action == "help":
        print("> You remember that you can take the following actions:")
        print("    - go north, n: Go north")
        print("    - go east, e: Go east")
        print("    - go south, s: Go south")
        print("    - go west, w: Go west")
        print("    - look around, l: Look around")
        print("    - take <item>: Take an item")
        print("    - inventory, i: Check your inventory")
        print("    - drop <item>: Drop an item")
        print("    - quit, q: Exit the cave")
        print("    - help, h: Ask for help")
            
    else:
        print("> You tremble inside as you realize you have no free will. Try another command, or maybe just ask for `help`.")

            
            
    print("")    # extra line
        
