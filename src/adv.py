from room import Room 
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("",""), Item("gold", "A pile of gold"), Item("sword", "A rusty sword"), Item("bone", "just some old bones")]),
}


# Link rooms together

room['outside'].north_to = room['foyer']
room['foyer'].south_to = room['outside']
room['foyer'].north_to_to = room['overlook']
room['foyer'].east_to = room['narrow']
room['overlook'].south_to = room['foyer']
room['narrow'].west_to = room['foyer']
room['narrow'].north_to = room['treasure']
room['treasure'].south_to = room['narrow']

# Main
# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).   
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.

def cmdToParts(cmd):
    return (cmd[0].split())
def locateItemRoom(item):
    for k, v in enumerate(player.current_room.items):
        if v.name == item:
            return k

def locateItemInventory(item):
    for k, v in enumerate(player.inventory):
        if v.name == item:
            return k

player = Player(input("Please enter your name: "), room['outside'], [])
direction = ["north", "south", "east", "west"]
verbs = ["go","take", "get", "drop", "inventory", "look"]

print(f"Current Room: {player.current_room.name}")
print(f"{player.current_room.description}")
while True:
    cmd = input("~~>")
    ## Breaks the cmd into a list of words, verb being the first word and obj being the second word
    parsedCmd = cmdToParts([cmd])
    verb = parsedCmd[0].lower()
    # If the command is greater than one word, it drops the second word to lower case. This prevents breaking if they only type one word.
    if len(parsedCmd) > 1:
        obj = parsedCmd[1].lower()
    if verb == "test":
        if player.inventory[locateItemInventory(obj)]:
            currentItem = player.inventory[locateItemInventory(obj)]
            print(currentItem.name)
        else:
            print("Nothing here")

    # Verbs[0] is go, obj would be the direction.
    elif verb == verbs[0] and obj in (direction):
        player.travel(obj)
    

    # Verbs[1/2] are take/get. locateItem finds the index number of the object if it's in the inventory or current room. 
    elif (verb == verbs[1] or verb == verbs[2]) and locateItemRoom(obj):
        currentItem = player.current_room.items[locateItemRoom(obj)]
        player.inventory.append(currentItem)
        currentItem.on_take(f"{currentItem.name}")
        player.current_room.items.pop(locateItemRoom(obj))

    # Verb[3] is drop. locateItemInventory finds the index number of the object if its in the inventory or current room
    elif verb == verbs[3] and locateItemInventory(obj):
        currentItem = player.inventory[locateItemInventory(obj)]
        player.current_room.items.append(currentItem)
        currentItem.on_drop(f"{currentItem.name}")
        player.inventory.pop(locateItemInventory(obj))
        print(f"Dropping {currentItem.name}")

    # Verb[4] is inventory and checks the inventory
    elif verb == verbs[4]:
        for i in player.inventory:
            print(f"{i.name}, {i.description}")

    # Verbs[5] is look and reprints the room and items in the room
    elif verb == verbs[5]:
        print(f"Current Room: {player.current_room.name}")
        print(f"{player.current_room.description}")
        if len(player.current_room.items) > 1:
            print("This room contains:")
            for i in player.current_room.items[1:]:
                print(f"{i.name}, {i.description}")
    
    # q quits the program
    elif verb == "q":
        break
    else:
        print("I don't recognize that command.")


    # if cmd in ("n", "s", "e", "w"):
    #     player.travel(cmd)
    # elif cmd == "q":
    #     break
    # else:
    #     print("Please enter n, s, e, w, or q")






