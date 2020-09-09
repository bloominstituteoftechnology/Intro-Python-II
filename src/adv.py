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


# Link rooms together #.n_to is creating a map (connecting the rooms)
# n represents north of the current room. (north, south , east, west)

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
sword = Item("Sword", "Sword of power.")
book = Item("Book", "Book of knowledge.")
helmet = Item("Helmet", "Helmet of power.")
boots = Item("Boots", "Metal Boots of power.")
gloves = Item("Gloves", "Gloves of power.")
coins = Item("Coins", "Gold coins.")

room['outside'].add_item_to_room(sword)
room['outside'].add_item_to_room(coins)
room['foyer'].add_item_to_room(book)
room['overlook'].add_item_to_room(helmet)
room['narrow'].add_item_to_room(boots)
room['treasure'].add_item_to_room(gloves)

# room['outside'].add_item_to_room(sword.name, sword.description)
# room['outside'].add_item_to_room(coins.name, coins.description)
# room['foyer'].add_item_to_room(book.name, book.description)
# room['overlook'].add_item_to_room(helmet.name, helmet.description)
# room['narrow'].add_item_to_room(boots.name, boots.description)
# room['treasure'].add_item_to_room(gloves.name, gloves.description)

# tries to move th player in the specified direction
def try_direction(player, direction):
    attribute = direction + '_to'
    # Python has a handy mehtod called 'hasattr'
    # allows us to check if a class has an attribute.
    if hasattr(player.location, attribute): # checks
        # this is a valid direction
        # use getattr to fetch the value associated with the attribute.
        print(f"You left: {player.location}")
        player.location = getattr(player.location, attribute)
        list_items_in_room(player.location)
    else: 
        print("There's nothing in that direction!")

def list_items_in_room(room):
    print("\n")
    print("Items in room:")
    for item in room.items:
        print(f"{item}")

    print("\n")

def list_player_items(player):
    print("---- Your Items ----")
    for itemName in player.items:
        print(itemName.name)

def check_item_in_room_status(action, itemPassed, room):
# If the user enters get or take followed by an Item name, look at the contents 
# of the current Room to see if the item is there.
#  if hasattr(room.items, )
    print("-------")

    if itemPassed in room.items:
        #do something with the item
        if action == "take" or "get":
            player.items.append(itemPassed)
            itemPassed.on_take(itemPassed.name)
            room.items.remove(itemPassed)
            print("---- Your Items ----")
            for itemName in player.items:
                print(itemName.name)
    elif action == "drop":
        room.items.append(itemPassed)
        itemPassed.on_drop(itemPassed)
        player.items.remove(itemPassed)
        for itemName in player.items:
                print(itemName.name)
    else:
        print("Item not in this room!")
        for itemName in player.items:
                print(itemName.name)

    print("---- Items Left In Room ----\n")    
    for item in room.items:
            print(item)

    # for item in room.items:
    #     print(hex(id(itemPassed)))
    #     print(hex(id(item)))
    #     if itemPassed == item.name:
    #         print(f"Can have {itemPassed}")
    #     else: 
    #         print("Can Not have")


player = Player("Kelson", room['outside'])

while True:

    print("\n")
    print(f"Current Location: {player.location}")

    command = input("\nCommand: ").strip().lower().split()

# check if their was two commands or one command entered.
    print(len(command))
    if len(command) == 1:
        first_command = command[0]
        first_char = first_command[0]

        # run the directional element
        if first_char[0] == "q":
                break

        if first_char == 'n':
            try_direction(player, first_char)
        elif first_char == 's':
            try_direction(player, first_char)
        elif first_char == 'e':
            try_direction(player, first_char)
        elif first_char == 'w':
            try_direction(player, first_char)
        elif first_char == 'i':
            list_player_items(player)

    elif len(command) == 2:
        first_command = command[0]
        second_command = command[1]

        if first_command == "get" or "take" or "drop":
            if second_command == "sword":
                check_item_in_room_status(first_command, sword, player.location)
            elif second_command == "book":
                check_item_in_room_status(first_command, book, player.location)
            elif second_command == "helmet":
                check_item_in_room_status(first_command, helmet, player.location)
            elif second_command == "boots":
                check_item_in_room_status(first_command, boots, player.location)
            elif second_command == "gloves":
                check_item_in_room_status(first_command, gloves, player.location)
            elif second_command == "coins":
                check_item_in_room_status(first_command, coins, player.location)
            else:
                print("Invalid Item entered, Please try again.")
                continue
    else:
        print("Error")
        continue
    
