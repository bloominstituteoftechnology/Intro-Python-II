from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
"""North of you, the cave mount beckons"""),

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
room['overlook'].e_to = room['treasure']
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
directions = ['n', 's', 'e', 'w']

player = Player("Fady", room['outside'])

print(f"Game Instructions: q is to quit, directions are n, e, s, & w.\nIf you find an item you like in a room, type get (item name).\nIf you want to drop an item from your inventory, type drop (item name)")

room['outside'].item_list.append(Item("fishing-rod", "used for fishing"))
room['foyer'].item_list.append(Item("binoculars", "used to see afar"))
room['overlook'].item_list.append(Item("sword", "sword resting in a rock, there's something weird about this thing"))
room['narrow'].item_list.append(Item("fire-wood", "sometimes nights get cold, this will keep you warm!"))
room['treasure'].item_list.append(Item("gold", "so dusty, looks like the looters didn't find everything!"))



while True:


    
    print(player.current_room.name)
    print(player.current_room.description)

    if len(player.current_room.item_list) > 0:
        print("items in the room: ")
        for item in player.current_room.item_list:
            print(f'Item name: {item.name}\nItem description: {item.description}')

    

    user_input = input(f"{player.name} What would you like to do?? >>>>>")

    if len(user_input.split()) == 1:

        if user_input == 'n':
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
            else:
                print("There's nothing in that direction, try again!")
        if user_input == 's':
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
            else:
                print("There's nothing in that direction, try again!")
        if user_input == 'e':
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
            else:
                print("There's nothing in that direction, try again!")
        if user_input == 'w':
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
            else:
                print("There's nothing in that direction, try again!")

        if user_input == 'q':
            exit(0)
        
        if user_input == 'i' or 'inventory':
            if len(player.inventory) > 0:
                for item in player.inventory:
                    print(f"Item name: {item.name}\nItem description: {item.description}")
            else:
                print(f"No items in you inventory")    

        # if user_input == 'inventory':
        #     if len(player.inventory) > 0:
        #         for item in player.inventory:
        #             print(f"Item name: {item.name}\nItem description: {item.description}")
        #     else:
        #         print(f"No items in you inventory")        

    elif len(user_input.split()) == 2:

        if user_input.split()[0] == 'get':
            if len(player.current_room.item_list) > 0:
                for item in player.current_room.item_list:
                    if item.name == user_input.split()[1]:
                        player.current_room.item_list.remove(item)
                        player.inventory.append(item)
                    else:
                        print(f"{user_input.split()[1]} was not found in the {player.current_room.name}")
            else:
                print(f"No items are available to take in {player.current_room.name}")

        if user_input.split()[0] == 'drop':
            if len(player.inventory) >0:
                for item in player.inventory:
                    if item.name == user_input.split()[1]:
                        player.inventory.remove(item)
                        player.current_room.item_list.append(item)
                    else:
                        print(f"{user_input.split()[1]} in not in the your inventory")
            else:
                print(f"There are no items to drop!")
    else:
        print("Your input is invalid")
