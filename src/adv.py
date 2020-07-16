from room import Room
from player import Player
from item import Item
import random

# Items Generator
items_ls = [
    Item("Axe", "vikings tool"), 
    Item("Stick", "tool for fires"), 
    Item("Sword", "big steak knife"), 
    Item("Grenade", "big boom"), 
]

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     random.sample(items_ls, 2)),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", random.sample(items_ls, 2)),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", random.sample(items_ls, 2)),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", random.sample(items_ls, 2)),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", random.sample(items_ls, 2)),
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
player = Player(room["outside"])
room_items = room["outside"].items

print("\n--------Game Starting----------")
print(f"\n{player.room}")
print(f"\nItems in this room: {[x.name for x in room_items]}")
print(f"\nYour Items: {player.items}")
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

while player.room != room["treasure"]:
    n = input("\nPress q to quit or choose North, East, South, West, get (item name), drop item: ")
    ls = [x.name.lower() for x in player.room.items]

    if n == "q":
        break

    elif (player.room == room['foyer']) & (n.lower().title() == "East"):
        print(f"Enetering a new area ... \n")
        player.room = room['foyer'].e_to
        print(player.room)
        room_items = room["narrow"].items
        print(f"Items in this room: {[x.name for x in room_items]}")

    elif (player.room == room['narrow']) & (n.lower().title() == "West"):
        print(f"Enetering a new area ... \n")
        player.room = room['narrow'].w_to
        print(player.room)
        room_items = room["foyer"].items
        print(f"Items in this room: {[x.name for x in room_items]}")

    elif (player.room == room['foyer']) & (n.lower().title() == "North"):
        print(f"Enetering a new area ... \n")
        player.room = room['foyer'].n_to
        print(player.room)
        room_items = room["overlook"].items
        print(f"Items in this room: {[x.name for x in room_items]}")

    elif (player.room == room['foyer']) & (n.lower().title() == "South"):
        print(f"Enetering a new area ... \n")
        player.room = room['foyer'].s_to
        print(player.room)
        room_items = room["outside"].items
        print(f"Items in this room: {[x.name for x in room_items]}")

    elif (player.room == room['overlook']) & (n.lower().title() == "South"):
        print(f"Enetering a new area ... \n")
        player.room = room['overlook'].s_to
        print(player.room)
        room_items = room["foyer"].items
        print(f"Items in this room: {[x.name for x in room_items]}")

    elif (player.room == room['outside']) & (n.lower().title() == "North"):
        print(f"Enetering a new area ... \n")
        player.room = room['outside'].n_to
        print(player.room)
        room_items = room["foyer"].items
        print(f"Items in this room: {[x.name for x in room_items]}")

    elif (player.room == room['narrow']) & (n.lower().title() == "North"):
        print(f"Enetering a new area ... \n")
        player.room = room['narrow'].n_to
        print(player.room)
    
    elif len(n.split()) == 2:
        n1 = n.lower().split()[0]
        n2 = n.lower().split()[1]

        if n1 == "get":
            item_obj = [x for x in player.room.items if x.name.lower() == n2][0]
            player.items.append(item_obj)
            print(f"You have picked up the {item_obj.name} the {item_obj.description}")
            print(f"Your items: {[x.name for x in player.items]}")
        
        elif n1 == "drop":
            item_obj = [x for x in player.items if x.name.lower() == n2]
            print("Removing items..")
            player.items.remove(item_obj[0])
            print(f"your items: {[x.name for x in player.items]}")

        else:
            pass




# --------GET ITEM----------
    # elif ((n.lower().split()[0] == "get") & (n.lower().split()[1] == n.lower().split()[1] in ls)):
    #     item_obj = [x for x in player.room.items if x.name.lower() == n.lower().split()[1]]
    #     if input(f"Would you like to pick up the {item_obj[0].name} the {item_obj[0].description} y/n?: ") == "y":
    #         print(f"You picked up the {item_obj[0].name}")
    #         player.items.append(item_obj[0])
    #         print(f"Your inventory: {[x.name for x in player.items]}")
    #     else:
    #         print(f"You decided not to pick up the {item_obj[0].name}")

# -------DROP ITEM--------- WIP
    # elif (n.lower().split()[0] == "drop"):
    #     print("dropped")
        # item_obj = [x for x in player.room.items if x.name.lower() == n.lower().split()[1]]
        # if input(f"Would you like to pick up the {item_obj[0].name} the {item_obj[0].description} y/n?: ") == "y":
        #     print(f"You picked up the {item_obj[0].name}")
        #     player.items.remove(item_obj[0])
        #     print(f"Your inventory: {[x.name for x in player.items]}")
        # else:
        #     print(f"You decided not to pick up the {item_obj[0].name}")

    else:
        ls = ["The way is blocked..", "I wouldn't go that way...", "Try Again...", "You shall not pass.."]
        print(random.sample(ls, 1)[0])