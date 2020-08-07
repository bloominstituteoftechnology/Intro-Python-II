from room import Rooms
from player import Player
from item import Item
from roominv import Roominv

# Declare all the rooms

room = {
    'outside':  Rooms("Outside Cave Entrance",
                     "North of you, the cave mount beckons",  [Item("HealthPotion", "Refills health")]),

    'foyer':    Rooms("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("ManaPotion", "Refills mana")]),

    'overlook': Rooms("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("ShortSword", "dull rusty blade")]),

    'narrow':   Rooms("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("BrokenShield", "broken but still usable")]),

    'treasure': Rooms("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("GoldCoin", "remnants of what was once left here")]),
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
player = Player(room['outside'])
roominv = Player(room['outside'])
starting_room = 1
current_room = 1
outside = 1
overlook_room = 3
foyer_room = 2
treasure_room = 5
narrow_room = 4
# Write a loop that:

outside_room = Player(room['outside'])
print(outside_room.location)

roominv.outside = room['outside']
roominv.outside.add_to_inventory_room(room['outside'].items[0])
roominv.foyer = room['foyer']
roominv.foyer.add_to_inventory_room(room['foyer'].items[0])
roominv.overlook = room['overlook']
roominv.overlook.add_to_inventory_room(room['overlook'].items[0])
roominv.narrow = room['narrow']
roominv.narrow.add_to_inventory_room(room['narrow'].items[0])
roominv.treasure = room['treasure']
roominv.treasure.add_to_inventory_room(room['treasure'].items[0])



while True:
   # Prints the current room name

    command = input("> Input n, e, s, or w to move that direction ").split(',')

    if command[0] == 'q':
        break     
    elif command[0] == 'n':
        if current_room == 2:
            current_room = 3
            player.this_room = room['overlook']
            print(player.this_room)
        elif current_room == 1:
            player.foyer_room = room['foyer']
            current_room = 2
            print(player.foyer_room)
        elif current_room == 5:
            print('You can only go south')         
        elif current_room == 4:
            current_room = 5
            player.treasure_room = room['treasure']
            print(player.treasure_room)
        elif current_room == 3:
            print("You can only move South")
    elif command[0] == 's':
        if current_room == 1:
            print('You can only move North')
            current_room = 1
        elif current_room == 2:
            current_room = 1
            player.outside_room = room['outside']
            print(player.outside_room)
        elif current_room == 5:
            current_room = 4
            player.narrow_room = room['narrow']
            print(player.narrow_room)
        elif current_room == 4:
            print('You can only move north or West')
        elif current_room == 3:
            current_room = 2
            player.foyer_room = room['foyer']
            print(player.foyer_room)
    

    elif command[0] == 'e':
        if current_room == 2:
             current_room = 4
             narrow_room = Player(room['narrow'])
             print(narrow_room.location)
        else:
            print("You can't move east")


    elif command[0] == 'w':
        if current_room == 4:
            current_room = 2
            foyer_room = Player(room['foyer'])
            print(foyer_room.location)
        else:
            print("You can't move West")

    if current_room == 1:
        item_selection = (input("grab or leave an item, press 1 or 2:"))
        if item_selection == '1':
            #search it as a string
            #loop through the array to find it
            selected_inventory = room['outside']
            player.add_to_inventory(selected_inventory.items[0])
            roominv.outside_room = room['outside']
            roominv.outside_room.remove_from_inventory_room(selected_inventory.items[0])
        else:
            try:
                player.remove_from_inventory(selected_inventory.items[0])
                roominv.outside_room.add_to_inventory_room(selected_inventory.items[0])
            except:
                print("No HealthPotion to remove")
                continue
    elif current_room == 2:
        item_selection = (input("grab or leave an item, press 1 or 2:"))
        if item_selection == '1':
            #search it as a string
            #loop through the array to find it
            selected_inventory = room['foyer']
            player.add_to_inventory(selected_inventory.items[0])
            roominv.foyer = room['foyer']
            roominv.foyer.remove_from_inventory_room(selected_inventory.items[0])
        else:
            try:
                player.remove_from_inventory(selected_inventory.items[0])
                roominv.foyer.add_to_inventory_room(selected_inventory.items[0])
            except:
                print("No ManaPotion to remove")
                continue
    elif current_room == 3:
        item_selection = (input("grab or leave an item, press 1 or 2:"))
        if item_selection == '1':

                    
                #search it as a string
                #loop through the array to find it
            selected_inventory = room['overlook']
            player.add_to_inventory(selected_inventory.items[0])
            roominv.overlook = room['overlook']
            roominv.overlook.remove_from_inventory_room(selected_inventory.items[0])
        else:
            try:
                player.remove_from_inventory(selected_inventory.items[0])
                roominv.overlook.add_to_inventory_room(selected_inventory.items[0])
            except:
                print("No ManaPotion to remove")
                continue

    elif current_room == 4:
        item_selection = (input("grab or leave an item, press 1 or 2:"))
        if item_selection == '1':
            #search it as a string
            #loop through the array to find it
            selected_inventory = room['narrow']
            player.add_to_inventory(selected_inventory.items[0])
            roominv.narrow = room['narrow']
            roominv.narrow.remove_from_inventory_room(selected_inventory.items[0])
        else:
            try:
                player.remove_from_inventory(selected_inventory.items[0])
                roominv.narrow.add_to_inventory_room(selected_inventory.items[0])
            except:
                print("No ManaPotion to remove")
                continue

    elif current_room == 5:
        item_selection = (input("grab or leave an item, press 1 or 2:"))
        if item_selection == '1':
            #search it as a string
            #loop through the array to find it
            selected_inventory = room['treasure']
            player.add_to_inventory(selected_inventory.items[0])
            roominv.treasure = room['treasure']
            roominv.treasure.remove_from_inventory_room(selected_inventory.items[0])
        else:
            try:
                player.remove_from_inventory(selected_inventory.items[0])
                roominv.treasure.add_to_inventory_room(selected_inventory.items[0])
            except:
                print("No ManaPotion to remove")
                continue