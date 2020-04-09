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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items
item = {
    'torch': Item("Torch", "This is perfect to light the dark cave!"),
    'shield': Item("Shield", "You can defend yourself with this."),
    'sword': Item("Sword", "Legend says it wields great power."),
    'bottle': Item("Bottle", "Great to hold things in.")
}

room['outside'].addItem(item['torch'])
room['outside'].addItem(item['shield'])
room['overlook'].addItem(item['sword'])
room['treasure'].addItem(item['bottle'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print("========================================")
playerOne = Player('Aaron', room['outside'])
print(playerOne.current_room)
print("====================")
print("Items: \n")
for roomItem in playerOne.current_room.items:
    print(roomItem)
print("====================")
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

print("What do you want to do?")
command = input(
    "[n] north  [s] south  [e] east  [w] west  [q] quit \n[take item-name]  [drop item-name]\n[i] [inventory] Inventory\n\n")

while command != 'q':
    print("========================================")
    if len(command.split()) == 2:

        handleItem = command.split()
        print(handleItem)

        if handleItem[0] == 'take':
            try:
                selectedItem = item[handleItem[1].lower()]
                if selectedItem in playerOne.current_room.items:
                    playerOne.takeItem(selectedItem)
                    playerOne.current_room.removeItem(selectedItem)
                else:
                    print("Invalid item")
            except:
                print("Invalid item")

        elif handleItem[0] == 'drop':
            try:
                selectedItem = item[handleItem[1].lower()]
                if selectedItem in playerOne.inventory:
                    playerOne.current_room.addItem(selectedItem)
                    playerOne.dropItem(selectedItem)
                else:
                    print("Invalid item")
            except:
                print("Invalid item")

    elif command == 'n':
        if hasattr(playerOne.current_room, 'n_to'):
            print("moving north ...")
            playerOne.current_room = playerOne.current_room.n_to
        else:
            print("can't move any further north")

    elif command == 's':
        if hasattr(playerOne.current_room, 's_to'):
            print("moving south ...")
            playerOne.current_room = playerOne.current_room.s_to
        else:
            print("can't move any further south")

    elif command == 'e':
        if hasattr(playerOne.current_room, 'e_to'):
            print("moving east ...")
            playerOne.current_room = playerOne.current_room.e_to
        else:
            print("can't move any further east")

    elif command == 'w':
        if hasattr(playerOne.current_room, 'w_to'):
            print("moving west ...")
            playerOne.current_room = playerOne.current_room.w_to
        else:
            print("can't move any further west")

    elif command == 'i' or command == 'inventory':
        print("Inventory: \n")
        for inventoryItem in playerOne.inventory:
            print(inventoryItem)

    else:
        print("invalid command")

    print("========================================")
    print(playerOne.current_room)
    print("====================")
    print("Items: \n")
    for roomItem in playerOne.current_room.items:
        print(roomItem)
    print("====================")

    print("\nWhat next?")
    command = input(
        "[n] north  [s] south  [e] east  [w] west  [q] quit \n[take item-name]  [drop item-name]\n[i] [inventory] Inventory\n\n")
